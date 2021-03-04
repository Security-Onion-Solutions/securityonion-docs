Updating
========

soup
----

We recommend using our ``soup`` script to update. ``soup`` will automatically install **all** available package updates (from both Ubuntu and Security Onion) and **all** updated Docker images.

::

    sudo soup

Please pay attention to the output of this command as it may request that you take specific action, such as manually restarting services. Also refer to the relevant blog entry for the update at https://blog.securityonion.net as there may be additional information there.

Snort/Suricata
--------------

Snort package upgrades will back up each of your existing ``snort.conf`` files to ``snort.conf.bak`` and migrate your ``HOME_NET`` and ``EXTERNAL_NET`` variables.

Suricata package upgrades will back up each of your existing ``suricata.yaml`` files to ``suricata.yaml.bak`` and migrate your ``HOME_NET`` and ``EXTERNAL_NET`` variables.

You'll then need to do the following:

-  re-apply any other local customizations to your ``snort.conf``/``suricata.yaml`` file(s)

-  update ruleset and restart Snort/Suricata as follows:

   ::

       sudo rule-update

Zeek
----

If you upgrade from Bro to Zeek, then Bro will automatically stop before Zeek is installed and so you may need to restart Zeek after the upgrade is complete.  If you upgrade from Zeek to a newer version of Zeek, Zeek will not automatically stop.

Zeek package upgrades will attempt to migrate your Zeek config. You should double-check your config and see if there are any local customizations that you need to manually re-apply. Then restart Zeek as follows:

::

    sudo so-zeek-restart

Elastic
-------

If ``soup`` upgrades the Elastic stack, and you then try to login to Kibana and it says ``Kibana server is not ready yet`` even after waiting a few minutes for Kibana to fully initialize, then check ``/var/log/kibana/kibana.log``. You may see something like:

::

    Another Kibana instance appears to be migrating the index. Waiting for that migration to complete. If no other Kibana instance is attempting migrations, you can get past this message by deleting index .kibana_6 and restarting Kibana
    
If that's the case, then you can do the following (replacing ``.kibana_6`` with the actual index name that was mentioned in your Kibana log):

::

    curl -XDELETE localhost:9200/.kibana_6

    sudo so-kibana-restart

Once you're logged into Kibana, check your Kibana dashboards. If they weren't reloaded automatically, you can manually reload them:

::

    sudo so-elastic-configure-kibana

If you've previously added any external Elastic components (such as filebeat, winlogbeat, etc.), be sure to upgrade them to match the version of your upgraded Elastic components.

Wazuh
-----

Wazuh package upgrades will back up ``/var/ossec/etc/ossec.conf`` and put the new ``ossec.conf`` in place.  You'll then need to do the following:

-  re-apply any other local customizations to ``/var/ossec/etc/ossec.conf``

-  restart Wazuh as follows:

   ::

       sudo so-ossec-restart
       
-  update any existing OSSEC/Wazuh agents to the Wazuh agent version matching your Wazuh server version

MySQL
-----

If you get any errors relating to MySQL, please see the `MySQL-Upgrade-Errors <MySQL-Upgrade-Errors>`__ section.

Initiating an update over SSH
-----------------------------

If you're updating your Security Onion box over an SSH connection and your connection drops, then your update process may be left in an inconsistent state. It is therefore recommended to run ``byobu`` so that your session will continue to run on the Security Onion box even if your connection drops. ``Byobu`` is very handy and we recommend running it all the time to avoid forgetting about it before an update.

::

    # install byobu
    sudo apt-get install byobu

    # enable byobu
    byobu-enable

    # you're now ready to update

For more information about ``byobu``, please see https://help.ubuntu.com/community/Byobu.

Distributed deployments
-----------------------

If you have a distributed deployment with a master server and separate sensor boxes and/or storage nodes, always update the master server first before updating other boxes. Then make sure to update the remaining boxes shortly thereafter. This will help to ensure that all boxes in your deployment are running the same code versions and help to avoid any incompatibilities.

Using salt and soup to update your entire deployment
----------------------------------------------------

`salt and
soup <Salt#using-salt-to-install-updates-across-your-entire-deployment>`__

Content Inspection
------------------

If your Security Onion box(es) go through a firewall, proxy, or other network security device that does content inspection, you may need to add an exception for ``ppa.launchpad.net``.

Standard Ubuntu package management tools
----------------------------------------

The ``soup`` command described above is the recommended method to install updates. If you instead choose to use standard Ubuntu package management tools to install updates, there are some caveats to be aware of:

-  Docker - Ubuntu package management tools don't update our Docker images (used for the Elastic Stack currently)

-  MySQL - if you've already run Setup, please see the `recommended procedure for updating the MySQL packages <MySQLUpdates>`__.

-  | PF-RING and new kernel packages
   | You may be prompted to update your kernel packages and PF-RING at the same time. If you do so, the PF-RING kernel module may get built for your current kernel and not for the newly installed kernel and upon reboot services will fail. To avoid this, you should install just the PF-RING kernel module by itself and then install the kernel and any other remaining package updates. Here's a one-liner that will do that:

   ::

       sudo apt-get update ; sudo apt-get install securityonion-pfring-module ; sudo apt-get dist-upgrade

   If you accidentally install both the kernel and PF-RING packages at the same time and then reboot and find out that PF-RING services (Snort and Suricata) are failing, you can reinstall the ``securityonion-pfring-module`` package:

   ::

       sudo apt-get install --reinstall securityonion-pfring-module

   .. rubric:: Security Onion 14.04
      :name: security-onion-14.04

   .. note::
   
   If you're still running the old Security Onion 14.04, ``soup`` will continue to install Ubuntu updates until Ubuntu    stops releasing updates for 14.04. However, there won't be any more Security Onion updates for version 14.04 as all development will be on version 16.04 moving forward.

Upgrades
--------

To upgrade from Security Onion 14.04 to Security Onion 16.04, please see the `Upgrading-from-14.04-to-16.04 <Upgrading-from-14.04-to-16.04>`__ section.
