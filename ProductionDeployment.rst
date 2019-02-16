Production Deployment
=====================

If you're going to be deploying Security Onion in production, please use the following steps.

Hardware Requirements
---------------------

First, check the `Hardware Requirements <Hardware>`__ page.

Download and Verify
-------------------

| `Download and verify the Security Onion ISO image <https://github.com/Security-Onion-Solutions/security-onion/blob/master/Verify_ISO.md>`__ 
| OR
| download and verify the ISO image for your preferred flavor of Ubuntu 16.04 64-bit.

Install
-------

If deploying a `distributed <Elastic-Architecture#distributed>`__ environment, you’ll need to perform the remaining steps on the server, as well as all forward and storage nodes, but make sure you install and configure the master server first. For best performance, the master server should be dedicated to just being a server for the other nodes (the master server should have no sniffing interfaces of its own). Please note that `forward <Elastic-Architecture#forward-node>`__ and `heavy <Elastic-Architecture#heavy-node>`__ nodes need to connect to the `master server <Elastic-Architecture#master>`__ on ports ``22`` and ``7736``. If you choose to enable salt for node management, nodes will need to be able to connect to the master server on ports ``4505`` and ``4506``.

#. Using the downloaded ISO, install the operating system. If prompted with an ``encrypt home folder`` option, DO NOT enable this feature. If asked about ``automatic updates``, DO NOT enable automatic updates. If prompted to install any additional packages, leave ``standard system utilities`` selected and also select ``OpenSSH Server`` (openssh-server). Do NOT choose ``MySQL`` at this point. All other required dependencies will be installed automatically.
#. When asked about partitioning, there are a few things to keep in mind:

   -  If you have more than 2TB of disk space, you will probably want to create a dedicated ``/boot`` partition at the beginning of the disk to ensure that you don’t have any Grub booting issues. Choosing the ``LVM`` option should do this automatically.
   -  Check to see if the installer allocates a large amount of space to ``/home``. If this is the case, you may want to shrink ``/home`` to give more space to ``/``.
   -  The Sguil database on the server (doesn’t exist on other node types) can grow fairly large (100GB or more for decent-size networks). It’s stored at ``/var/lib/mysql/``, so you may want to put ``/var`` on a dedicated partition or disk and assign a good amount of disk space to it. Also see the ``DAYSTOKEEP`` instructions on the `Post-Installation page <PostInstallation>`__.
   -  Forward, Heavy, and Standalone nodes store full packet captures at ``/nsm/sensor_data/``, so you may want to put ``/nsm`` on a dedicated partition/disk and assign as much disk space as possible (1TB or more). For larger volumes you might also consider using XFS for the ``/nsm`` partition.
   -  For Heavy, Standalone, and Storage Nodes, it is highly recommended to place ``/nsm/elasticsearch`` and ``/nsm/logstash`` on SSD or fast spinning disk in a RAID 10 configuration. See `Hardware Requirements <Hardware#elastic-stack>`__ for more details.

#. When installation completes, reboot into your new installation and login with the credentials you specified during installation.
#. If you’re running a VM, now would be a good time to snapshot it so you can revert later if you need to.
#. Verify that you have Internet connectivity. If necessary, configure your `proxy <Proxy>`__ settings.
#. If you installed from the Security Onion 16.04 ISO image, run ``sudo soup``. If you get any errors relating to MySQL, please see `MySQL-Upgrade-Errors <MySQL-Upgrade-Errors>`__. Reboot if prompted. Skip to the Setup section below.
#. Install all Ubuntu updates and reboot:
   ``sudo apt update && sudo apt dist-upgrade && sudo reboot``
#. Log back in and configure MySQL not to prompt for root password (Setup will generate a random password later):
   ``echo "debconf debconf/frontend select noninteractive" | sudo debconf-set-selections``
#. Install software-properties-common if it's not already installed:
   ``sudo apt -y install software-properties-common``
#. Add the Security Onion stable repository:
   ``sudo add-apt-repository -y ppa:securityonion/stable``
#. Update:
   ``sudo apt update``
#. Install the ``securityonion-all`` metapackage (or one of the more focused `metapackages <MetaPackages>`__). This could take 15 minutes or more depending on the speed of your CPU and Internet connection.
   ``sudo apt -y install securityonion-all syslog-ng-core``
#. OPTIONAL: If you want to use `Salt <Salt>`__ to manage your deployment, also install ``securityonion-onionsalt``. You can do this before or after Setup, but it's much easier if you do it before Setup.
   ``sudo apt -y install securityonion-onionsalt``
#. | Update all packages:
   | ``sudo soup``

   .. rubric:: Setup
      :name: setup

#. Run the Setup wizard. If you are locally on the box, you can run the GUI:
   ``sudo sosetup``
   Otherwise, if you are remote and logged in over ssh, you can run CLI-only Setup using ``sosetup.conf``. For more information, please see ``/usr/share/securityonion/sosetup.conf``.
#. The Setup wizard will walk you through configuring ``/etc/network/interfaces`` and will then reboot.
#. When prompted whether you would like to configure ``/etc/network/interfaces`` now, choose “Yes, configure
   /etc/network/interfaces!.”
#. If you have more than one network interface, you’ll be asked to specify which one should be the management interface.
#. You’ll then be asked to choose DHCP or static addressing for the management interface. It is highly recommended you choose static.
#. Choosing static, you’ll be prompted to enter a static IP address for your management interface, the network’s subnet mask, gateway IP address, DNS server IP addresses (separated by spaces), and your local domain.
#. You’ll then be prompted to select any additional interfaces that will be used for sniffing/monitoring network traffic.
#. When prompted, choose “Yes, make changes!"
#. If you need to adjust any network settings manually (e.g. ``MTU``), you may edit ``/etc/network/interfaces`` before rebooting.
#. When ready to reboot, click "Yes, reboot!”
#. After rebooting, log back in and start the Setup wizard again (GUI if local, sosetup.conf CLI if remote). It will detect that you have already configured ``/etc/network/interfaces`` and will walk you through the rest of the configuration.
#. Select ``Production Mode``.
#. Select ``New`` or ``Existing`` (``New`` if this is a master or standalone, and ``Existing`` for forward, heavy, and storage nodes).

-  New

   #. Provide a username and password for the analyst user.
   #. Select ``Best Practices``.
   #. Choose your IDS ruleset.
   #. Choose your IDS engine (`<Snort>`_ or `<Suricata>`_).
   #. Choose whether or not to enable sensor services.  If this is going to be a standalone box with no other nodes connected, you can enable sensor services. Otherwise, if this going to be a distributed deployment with multiple nodes connected, we recommend disabling sensor services on this master server.
   #. Choose whether or not to use storage nodes for log storage.  Please note that, if you choose to use storage nodes, then until a storage node is configured and Logstash has intialized on the storage node, you will not be able to review log data for configured forward nodes.
   #. Select ``Yes`` to proceed with your changes.

-  Existing

   #. Provide the hostname or IP address of the master server (some folks may want to specify the IP/hostname of the master server in ``/etc/hosts`` and use the specified hostname during setup -- this may help in the event the master server IP changes.)
   #. Provide a username to SSH to the master for the node (should have
      already been created on the master and added to the sudo group).
      Please make sure that your server has been set up and you have
      network connectivity and no firewall rules that would block this
      traffic. Additionally, consider creating a separate SSH account on
      the master server for each node so that if a node is ever
      compromised, its individual account can be disabled without
      affecting the other nodes.

      *On the Master, the following or similar should have been run
      (where ``$nodeuser`` is your specified user):*

      ``sudo adduser $nodeuser && sudo adduser $nodeuser sudo``

      | The new account must have a full home directory. If you do not
        create it when you create the account, copy
      | ``/etc/skel`` to ``/home/$nodeuser`` and do
        ``chown -R $nodeuser:$nodeuser /home/$nodeuser``. This is needed
        so the .ssh directory may be created to manage the connection.

      *NOTE: This user should be removed from the sudo group on the
      master server after setup*.

   #. Select Node Type:

      -  Forward Node

         -  Select ``Best Practices``.
         -  Keep the default for PF\_RING min\_num\_slots, unless you
            would like to change it.
         -  Modify the selected sniffing interfaces if necessary --
            otherwise, continue.
         -  Modify HOME\_NET as desired.
         -  Select ``Yes`` to proceed with your changes.

      *Please note: If you chose to use one or more storage nodes with
      your master server, you will be able to receive IDS alerts and
      pull PCAPs from the forward node once setup completes, however,
      you will not be able to review other logs (i.e. Bro logs in
      Kibana) from the node until a storage node has been configured for
      the master server and Logstash on the storage node has
      initialized.*

      -  Heavy Node

         -  Select ``Best Practices``.
         -  Keep the default for PF\_RING min\_num\_slots, unless you
            would like to change it.
         -  Modify the selected sniffing interfaces if necessary --
            otherwise, continue.
         -  Modify HOME\_NET as desired.
         -  Provide amount of disk space to be used for Elasticsearch to
            store logs (default is half of available disk space).
         -  Select ``Yes`` to proceed with your changes.

      -  Storage Node

         -  Provide amount of disk space to be used for Elasticsearch to
            store logs (default is half of available disk space).
         -  Select ``Yes`` to proceed with your changes.

   #. | Remove ``$nodeuser`` from the sudo group on the master server:
      | ``sudo deluser $nodeuser sudo``

Proceed to `PostInstallation <PostInstallation>`__
