.. _cloud-google:

Google Cloud Image
==================

If you would like to deploy Security Onion in Google Cloud Platform (GCP), choose the Security Onion 2 image listed on the Google Marketplace:
https://securityonion.net/google/?ref=_ptnr_soc_docs_230824

.. warning::

   Existing 2.4 RC1 or newer Security Onion Google Image installations should use the :ref:`soup` command to upgrade to newer versions of Security Onion. Attempting to switch to a newer image from the Google Marketplace could cause loss of data and require full grid re-installation. Upgrading from Security Onion 2.3 or beta versions of 2.4 is unsupported.

.. note::

   This section does not cover network connectivity to the Security Onion node. This can be achieved through configuring an external IP for the node’s management interface, or through the use of a VPN connection via OpenVPN.

.. note::

   This section does not cover all aspects of how to set up a VPC in GCP, as each deployments is typically unique for the user. For more details about setting up a VPC, please see https://cloud.google.com/vpc/docs/vpc. Ensure that all Security Onion nodes can access the manager node over the necessary ports. This could require adding rules to your GCP Virtual Private Cloud and/or VMs in order to satisfy the Security Onion :ref:`firewall` Node Communication requirements.


Requirements
############

Before proceeding, determine the grid architecture desired. Choose from a single-node grid versus a distributed, multi-node grid. Additionally, determine if the lower latency of local instance storage is needed (typically when there is high-volume of traffic being monitored, which is most production scenarios), or if persistent disks can be used for increased redundancy.

Single Node Grid
----------------

For simple, low-volume production monitoring, a single node grid can be used. Persistent disks must be used for :ref:`elasticsearch` data storage if used for production purposes. Single node grids cannot use local disks without being at risk of losing :ref:`elasticsearch` data. However, for temporary evaluation installations, where there is little concern for data loss, local disks can be used. 

Listed below are the minimum suggested single-node instance quantities, sizes, and storage requirements for either standalone or evaluation installations (choose one, not both). Note that when using virtual machines with the minimum RAM requirements you may need to enable memory swapping.

Standalone:

- Quantity: 1
- Type: n2-standard-4
- Storage: 256GB Balanced Persistent Disk

Evaluation*:

- Quantity: 1
- Type: n2-standard-8
- Storage: 256GB SSD Persistent Disk

* Assuming evaluation of performance as well as functionality, therefore higher minimums compared to standalone.
  
Distributed Grid
----------------

For high volume production monitoring, choose a multi-node grid architecture. At least two search nodes must be used in this architecture. This is required due to the use of local disks for :ref:`elasticsearch` data storage, where each of the search nodes retains a replica of another search node, for disaster recovery.

Listed below are the minimum suggested distributed grid instance quantities, sizes, and storage requirements. Prefer increasing VM memory over enabling swap memory, for best performance. High volume networks will need more powerful VM types with more storage than those listed below.

VPN Node

- Quantity: 1
- Type: e2.micro
- Storage: 50GB Balanced Persistent Disk
  
Manager

- Quantity: 1
- Type: n2-standard-4
- Storage: 300GB Balanced Persistent Disk

Search Nodes

- Quantity: 2 or more
- Type: n2-standard-4
- Storage: 256GB Balanced Persistent Disk
- Storage: 375GB Local Disk (NVMe)
  
Sensor monitoring the VPN ingress

- Quantity: 1
- Type: n2-standard-4
- Storage: 500GB Balanced Persistent Disk

Setup Traffic Mirroring
#######################

To accomplish traffic mirroring in GCP, a packet mirroring policy must be created and assigned to an internal load balancer. Google supports multiple methods for selecting what traffic to mirror. For example, a special tag keyword can be configured on the mirror policy, such as "so-mirror", and any VM that should have its traffic monitored can be given that special tag. The mirrored traffic will be forwarded to the internal load balancer, and a Security Onion sensor VM will be a member of that load balancer's instance group.

Follow the steps below to setup a traffic mirroring configuration. You will need to be logged into the Google Cloud Console, and somewhat familiar with GCP and how zones and regions are used. Note that these steps are only one of many ways to do this. For example, your scenario may require more advanced configuration, such as packet filtering, or additional VPCs.

Create a VPC for the Monitored Network
--------------------------------------

Create a new Virtual Private Cloud (VPC) network for collection of monitored network traffic. This will be referred to below as the Monitored VPC network. Define one subnet within this VPC that will be dedicated to receiving monitored traffic. 

Add a new firewall rule to this VPC network to allow all incoming mirrored traffic. Specify a target tag of ``so-collector`` and a source tag of ``so-mirror``. This will allow all mirrored traffic originating from a VM NIC tagged with ``so-mirror``, and residing in this same VPC network, to be delivered to the sensor VM's monitoring NIC tagged with ``so-collector``.


Create a VPC for the Security Onion Network
-------------------------------------------

Create a new Virtual Private Cloud (VPC) network where the Security Onion grid will communicate. Configure the subnets as desired, however, at least one subnet is required, and this VPC cannot overlap IP space with the above Monitored VPC network. Ensure that SSH access (port TCP/22) and HTTPS (port TCP/443) is enabled so that you have the ability to connect to VMs from your external network. For security purposes it's recommended to limit inbound access from trusted IPs.

Add a new firewall rule to allow all traffic originating from any VM instance within the Security Onion VPC network. Choose a source IP range that encapsulates the IP ranges of the subnet(s) created above. This is necessary for connectivity between the manager and minion nodes. You can also choose to be more specific about traffic within the VPC however the rules must satisfy the Security Onion :ref:`firewall` Node Communication requirements.

Create Sensor Instance Group
----------------------------

Create an unmanaged Instance Group. This is found under the Compute Engine section of the Google Cloud Console. Use the Security Onion VPC as the selected network. Leave the VM instances blank; later in this document the Security Onion sensor node will be added to this group. Port mapping is not required for this group.

Create Internal Load Balancer
-----------------------------

Under Network services, within the Google Cloud Console, create a Load Balancer. Choose TCP Load Balancer and select the ``Only between my VMs`` option. Click Continue and then select the Monitoring VPC network.

For the Backend configuration, choose the Instance Group created above. Ignore the informative box that explains the need to use additional NICs in the group instances. Specify that the backend is a failover group for backup. Create a new Health check that uses port TCP/22 (SSH) as the health test, with the following timing settings:

- Check Interval: 300
- Timeout: 1
- Healthy Threshold: 1
- Unhealthy Threshold: 1

Note that this health check is put in place only to satisfy the GCP requirement that all backends have a health check assigned. Since the backend group is marked as a failover, it will always forward traffic, regardless of the health check result.

For the Frontend configuration, select the subnet in the Monitoring VPC network that you created specifically for receiving monitored traffic. Choose non-shared IP. If there you would like to forward all traffic, choose All ports and enable global access. Under Advanced Configurations, enable the ``Load Balancer for Packet mirroring`` checkbox.

Create Packet Mirroring Policy
------------------------------

Traffic mirroring allows you to copy the traffic to/from an instance (or multiple instances) and send it to the sniffing interface of a network security monitoring sensor or a group of interfaces using a network load balancer.  For more details about GCP Traffic Mirroring please see: https://cloud.google.com/vpc/docs/packet-mirroring

Create a Packet Mirroring policy. This can be found in the Google Cloud Console under the VPC network section. When selecting the VPC network, choose the option that denotes the mirrored source and collector destination are in the same VPC network and select the Mirrored VPC network created earlier.

Under Select mirrored source, check the box next to the "Select with network tag" label. Then enter a tag named ``so-mirror``. Once completed with the grid setup, you can later tag all your VMs, whose traffic you want monitored, with the same ``so-mirror`` tag.

Under Select collector destination, choose the front end forwarding rule that was created during the Load Balancer setup earlier.

Finally, choose to mirror all traffic, unless you prefer to filter specific traffic for mirroring.

Create Security Onion Instances
###############################

Instance Creation
-----------------

To configure a Security Onion instance (repeat for each node in a distributed grid), follow these steps:

- Access the Google Cloud Marketplace at https://console.cloud.google.com/marketplace.
- Ensure you have a means of authenticating to VM instances over SSH. One method to authenticate is via a project-wide SSH key, which can be defined in Compute Engine -> Metadata -> SSH Keys.
- Search the Marketplace for ``Security Onion`` and Launch the latest version of the Security Onion 2 official VM image.
- Choose the appropriate machine type based on the desired hardware requirements.  For assistance on determining resource requirements please review the Requirements section above.
- Under the Networking interfaces section, expand the pre-added Network interface and select the Security Onion VPC network and desired subnet. External ephemeral IP is sufficient, unless you are planning to use a VPN to access the Security Onion Console, in which case no external ephemeral IP is necessary. Using a VPN is recommended, but setup of a VPN in GCP is out of scope of this guide.
- (Distributed "Sensor" node or Single-Node grid only) Add a second Network interface and select the monitoring VPC network, and the appropriate subnet. No external ephemeral IP is necessary for this interface. Specify the network tag ``so-collector`` for this VM.
- (Distributed "Manager" node or Single-Node grid only) If not using a VPN, enable the Allow HTTPS traffic from the Internet checkbox, and specify allowed source IP ranges. Under network tags, type ``https-server`` and press <ENTER>.
- Adjust the boot disk size and type as necessary, using the guidance in the above Requirements section and elsewhere in the Security Onion documentation.
- (Distributed "Search" node or Evaluation grid only) Under Disks, click ``Add Local SSD``. Choose NVMe and select the desired disk capacity based on anticipated log/event retention.
- If requested, review GCP Marketplace Terms, and if acceptable click the corresponding checkbox.
- Select: ``Create``

Prepare Nodes with Ephemeral, Local Disk Storage
------------------------------------------------

For distributed search nodes, or an evaluation node if using local disk storage, SSH into the node and cancel out of the setup. Prepare the local disk partition by executing the following command:

::

    sudo so-prepare-fs

By default, this command expects the local disk device to be located at ``/dev/nvme1n1`` and will mount that device at ``/nsm/elasticsearch``. If this fails run ``lsblk`` to determine which disk to use. To override either of those two defaults, specify them as arguments. For example:

::

    sudo so-prepare-fs /dev/nvme0n1 /nsm/elasticsearch

Restart the Security Onion setup by running the following command:

::

    cd /securityonion
    sudo ./so-setup-network

Manager Setup
#############

If this is an evaluation node with a local disk, ensure the node has been prepared as described in the preceding section. 

After SSH'ing into the node, setup will begin automatically. Follow the prompts, selecting the appropriate install options. Most distributed installations will use the ``hostname`` or ``other`` web access method, due to the need for both cluster nodes inside the private network, and analyst users across the public Internet to reach the manager. This allows for custom DNS entries to define the correct IP (private vs public) depending on whether it's a cluster node or an analyst user. Users evaluating Security Onion for the first time should consider choosing the ``other`` option and specifying the node's public cloud IP.

GCP provides a built-in NTP server at hostname ``metadata.google.internal``. This can be specified in the SOC Configuration screen after setup completes. By default the server will use the time servers at ``ntp.org``.

For distributed manager nodes using ephemeral storage, go to SOC Configuration. Search for ``number_of_replicas`` and change to 1. This will double the storage cost but will ensure at least two VMs have the data, in case of an ephemeral disk loss.

Optionally, adjust :ref:`elastalert` indices so that they have a replica. This will cause them to turn yellow but that will be fixed when search nodes come online:

::

    so-elasticsearch-query elastalert*/_settings -X PUT -d '{"index" : { "number_of_replicas" : 1 }}'

This is an optional step due to the ElastAlert indices being used primarily for short-term/recent alert history. In the event of a data loss when ElastAlert 2 restarts the indices will be regenerated. 

Search Node Setup
#################

Follow standard Security Onion search node installation, answering the setup prompts as applicable. If you are using local disk storage be sure to first prepare the instance as directed earlier in this section.

GCP Sensor Setup
################

In the GCP console, under Compute Engine go to the Instance Group page and edit the instance group that was created earlier. Use the dropdown list to add the new sensor VM instance to this group.

SSH into the sensor node and run through setup to set this node up as a sensor. Choose ``ens4`` as the main interface and ``ens5`` as the monitoring interface.

Remote Sensor Setup
###################

Setup the VPN (out of scope for this guide) and connect the sensor node to the VPN.
When prompted to choose the management interface, select the VPN tunnel interface, such as ``tun0``. Use the internal IP (not the ephemeral IP) address of the manager inside GCP when prompted for the manager IP.


If connecting sensors through the VPN instance you will need to add the inside interface of your VPN concentrator to the ``sensor`` firewall hostgroup. For instance, assuming the following architecture:

::

    SO Sensor        -> VPN Endpoint     -> Internet -> VPN Endpoint  -> SO Manager
    Location: Remote    Location: Remote                Location: Googe  Location: Google
    192.168.33.13       192.168.33.10                   10.55.1.10       10.55.1.20

In order to add the Remote Network Forward Node to the Grid, you would have to add ``10.55.1.10`` to the ``sensor`` firewall hostgroup.

This change can be done in the SOC Configuration screen. Then, either wait up to 15 minutes for the scheduled configuration sync to run, or force a synchronization immediately via the SOC Configuration Options. Once the firewall hostgroup configuration has been synchronized your Manager will be ready for remote minions to start connecting.

Verifying Traffic Mirroring
###########################

Deploy a temporary test VM instance, using a e2.micro, debian-based instance in the Monitored VPC network, and in the same region used in the rest of this guide. Add the ``so-mirror`` network tag to the VM.

SSH into the sensor node created earlier in this guide, and run the following command to watch mirrored traffic:

``tcpdump -nni ens5``

While that is running, in another terminal, SSH into this new test VM and run a curl command to a popular website. You should see that HTTP/HTTPS traffic appear in the tcpdump output.

Login to Security Onion and verify that the traffic also appears in the Hunt user interface.

Delete the temporary test VM instance when the verification is completed.
