.. _cloud-amazon:

Amazon Cloud Image
==================

If you would like to deploy Security Onion in Amazon Web Services (AWS), we have an Amazon Machine Image (AMI) that is already built for you:
https://securityonion.net/aws/?ref=_ptnr_soc_docs_230525

.. warning::

   Existing 2.4 RC1 or newer Security Onion AMI installations should use the :ref:`soup` command to upgrade to newer versions of Security Onion. Attempting to switch to a newer AMI from the AWS Marketplace could cause loss of data and require full grid re-installation. Upgrading from Security Onion 2.3 or beta versions of 2.4 is unsupported.
    
.. note::

   This section does not cover network connectivity to the Security Onion node. This can be achieved through configuring an external IP for the node’s management interface, or through the use of a VPN connection via OpenVPN. For more details about VPN connections, please see https://medium.com/@svfusion/setup-site-to-site-vpn-to-aws-with-pfsense-1cac16623bd6.

.. note::

   This section does not cover how to set up a VPC in AWS. For more details about setting up a VPC, please see https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html. Ensure that all Security Onion nodes can access the manager node over the necessary ports. This could require adding rules to your AWS security groups in order to satisfy the Security Onion :ref:`firewall` Node Communication requirements.

Requirements
############

Before proceeding, determine the grid architecture desired. Choose from a single-node grid versus a distributed, multi-node grid. Additionally, determine if the lower latency of ephemeral instance storage is needed (typically when there is high-volume of traffic being monitored, which is most production scenarios), or if network-based storage, EBS, can be used for increased redundancy.

Single Node Grid
----------------

For simple, low-volume production monitoring, a single node grid can be used. EBS must be used for :ref:`elasticsearch` data storage if used for production purposes. Single node grids cannot use ephemeral instance storage without being at risk of data loss. However, for temporary evaluation installations, where there is little concern for data loss, ephemeral instance storage can be used. 

Listed below are the minimum suggested single-node instance quantities, sizes, and storage requirements for either standalone or evaluation installations (choose one, not both). Note that when using virtual machines with the minimum RAM requirements you may need to enable memory swapping.

Standalone:

- Quantity: 1
- Type: t3a.xlarge
- Storage: 256GB EBS (Optimized) gp3

Evaluation

- Quantity: 1
- Type: t3a.2xlarge
- Storage: 256GB EBS (Optimized) gp3
- Storage: 100GB Instance Storage (SSD/NVMe)
  
Distributed Grid
----------------

For high volume production monitoring, choose a multi-node grid architecture. At least two search nodes must be used in this architecture. This is required due to the use of ephemeral instance storage for :ref:`elasticsearch` data storage, where each of the search nodes retains a replica of another search node, for disaster recovery.

Listed below are the *minimum* suggested distributed grid instance quantities, sizes, and storage requirements. Prefer increasing VM memory over enabling swap memory, for best performance. High volume networks will need more powerful VM types with more storage than those listed below.

VPN Node

- Quantity: 1
- Type: t3a.micro (Nitro eligible)
- Storage: 50GB EBS (Optimized) gp3
  
Manager

- Quantity: 1
- Type: m5a.xlarge
- Storage: 300GB EBS (Optimized) gp3
  
Search Nodes

- Quantity: 2 or more
- Type: m5ad.xlarge
- Storage: 200GB EBS (Optimized) gp3
- Storage: 150GB Instance Storage (SSD/NVMe)
  
Sensor monitoring the VPN ingress

- Quantity: 1
- Type: c5a.2xlarge
- Storage: 500GB EBS (Optimized) gp3

Create Monitoring Interface 
###########################

To setup the Security Onion AMI and VPC mirror configuration, use the steps below.

Create a Security Group for Sniffing Interface 
----------------------------------------------

Security Groups act like a firewall for your Amazon EC2 instances controlling both inbound and outbound traffic. You will need to create a security group specifically for the interface that you will be using to sniff the traffic.  This security group will need to be as open as possible to ensure all traffic destined to the sniffing interface will be allowed through.  To create a security group, follow these steps:

- From the EC2 Dashboard Select: ``Security Groups`` under the Network & Security sections in the left window pane.
- Select: ``Create Security Group``
- Provide a Security Group Name and Description.
- Select the appropriate VPC for the security group. 
- With the inbound tab selected, select: ``Add Rule`` 
- Add the appropriate inbound rules to ensure all desired traffic destined for the sniffing interface is allowed.
- Press the ``Create security group`` button.

Create Sniffing Interface
-------------------------

Prior to launching the Security Onion AMI you will need to create the interface that will be used to monitor your VPC.  This interface will be attached to the Security Onion AMI as a secondary interface.  To create a sniffing interface, follow these steps:

- From the EC2 Dashboard Select: ``Network Interfaces`` under the Network & Security section in the left window pane. 
- Select: ``Create Network Interface``
- Provide a description and choose the appropriate subnet you want to monitor.
- Select the security Group that you created for the sniffing interface.
- Select: ``Create``

Create Security Onion Instances
###############################

Instance Creation
-----------------

To configure a Security Onion instance (repeat for each node in a distributed grid), follow these steps:

- From the EC2 dashboard select: ``Launch Instance``
- Search the AWS Marketplace for ``Security Onion`` and make sure you get the latest version of the Security Onion official AMI.
- Choose the appropriate instance type based on the desired hardware requirements and select ``Next: Configure Instance Details``.  For assistance on determining resource requirements please review the AWS Requirements section above.
- From the subnet menu select the same subnet as the sniffing interface.
- Under the Network interfaces section configure the eth0 (management) interface.
- (Distributed "Sensor" node or Single-Node grid only) Under the Network interfaces section select: ``Add Device`` to attach the previously created sniffing interface to the instance.
- (Distributed "Sensor" node or Single-Node grid only) From the Network Interface menu for eth1 choose the sniffing interface you created for this instance.  Please note if you have multiple interfaces listed you can verify the correct interface by navigating to the Network Interfaces section in the EC2 Dashboard.
- Select: ``Next: Add Storage`` and configure the volume settings.
- Select: ``Next: Add Tags`` and add any additional tags for the instance.
- Select: ``Next: Configure Security Group`` and add the appropriate inbound rules.
- Select: ``Review and Launch``
- If prompted, select the appropriate SSH keypair that will be used to ssh into the Security Onion instance for administration 
- The default username for the Security Onion AMI is: ``onion``

Prepare Nodes with Ephemeral Storage
------------------------------------

For distributed search nodes, or an evaluation node if using ephemeral storage, SSH into the node and cancel out of the setup. Prepare the ephemeral partition by executing the following command:

::

    sudo so-prepare-fs

By default, this command expects the ephemeral device to be located at ``/dev/nvme1n1`` and will mount that device at ``/nsm/elasticsearch``. If this fails run ``lsblk`` to determine which disk to use. To override either of those two defaults, specify them as arguments. For example:

::

	sudo so-prepare-fs /dev/nvme3n0 /nsm/elasticsearch

Restart the Security Onion setup by running the following command:

::

	cd /securityonion
	sudo ./so-setup-network

Manager Setup
#############

If this is an ephemeral evaluation node, ensure the node has been prepared as described in the preceding section. 

After SSH'ing into the node, setup will begin automatically. Follow the prompts, selecting the appropriate install options. Most distributed installations will use the ``hostname`` or ``other`` web access method, due to the need for both cluster nodes inside the private network, and analyst users across the public Internet to reach the manager. This allows for custom DNS entries to define the correct IP (private vs public) depending on whether it's a cluster node or an analyst user. Users evaluating Security Onion for the first time should consider choosing the ``other`` option and specifying the node's public cloud IP.

AWS provides a built-in NTP server at IP ``169.254.169.123``. This can be specified in the SOC Configuration screen after setup completes. By default the server will use the time servers at ``ntp.org``.

For distributed manager nodes using ephemeral storage, go to SOC Configuration. Search for ``number_of_replicas`` and change to 1. This will double the storage cost but will ensure at least two VMs have the data, in case of an ephemeral disk loss.

Optionally, adjust :ref:`elastalert` indices so that they have a replica. This will cause them to turn yellow but that will be fixed when search nodes come online:

::

    so-elasticsearch-query elastalert*/_settings -X PUT -d '{"index" : { "number_of_replicas" : 1 }}'

This is an optional step due to the ElastAlert indices being used primarily for short-term/recent alert history. In the event of a data loss when ElastAlert 2 restarts the indices will be regenerated. 

Search Node Setup
#################

Follow standard Security Onion search node installation, answering the setup prompts as applicable. If you are using ephemeral storage be sure to first prepare the instance as directed earlier in this section.

AWS Sensor Setup
################

SSH into the sensor node and run through setup to set this node up as a sensor. Choose ``eth0`` as the main interface and ``eth1`` as the monitoring interface.

Remote Sensor Setup
###################

Setup the VPN (out of scope for this guide) and connect the sensor node to the VPN. During the Security Onion setup of the Sensor, when prompted to choose the management interface, select the VPN tunnel interface, typically ``tun0``.

If connecting sensors through the VPN instance you will need to add the inside interface of your VPN concentrator to the ``sensor`` firewall hostgroup. For instance, assuming the following architecture:

::

    SO Sensor        -> VPN Endpoint     -> Internet -> VPN Endpoint  -> SO Manager
    Location: Remote    Location: Remote                Location: AWS    Location: AWS
    192.168.33.13       192.168.33.10                   10.55.1.10       10.55.1.20

In order to add the Remote Network Forward Node to the Grid, you would have to add ``10.55.1.10`` to the ``sensor`` firewall hostgroup.

This change can be done in the SOC Configuration screen. Then, either wait up to 15 minutes for the scheduled configuration sync to run, or force a synchronization immediately via the SOC Configuration Options. Once the firewall hostgroup configuration has been synchronized your Manager will be ready for remote minions to start connecting.

AWS Traffic Mirroring
#####################

Traffic mirroring allows you to copy the traffic to/from an instance and send it to the sniffing interface of a network security monitoring sensor or a group of interfaces using a network load balancer. For more details about AWS Traffic Mirroring please see: https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html

.. tip::

    You can only mirror traffic from an EC2 instance that is powered by the AWS Nitro system.  For a list of supported Nitro systems, please see https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances.


Create Mirror Target
--------------------

A mirror target in AWS refers to the destination for the mirrored traffic.  This can be a single interface or a group of interfaces using a network load balancer.  To configure a mirror target, follow these steps:

- From the VPC dashboard select: ``Mirror Targets`` under the Traffic Mirroring section in the left window pane.
- Select: ``Create traffic mirror target``
- Under the Choose target section select the appropriate target type and choose the sniffing interface connected to the Security Onion instance.  For more details about traffic mirror targets please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-targets.html
- Select: ``Create``

Create Mirror Filter
--------------------

A mirror filter allows you to define the traffic that is copied to in the mirrored session and is useful for tuning out noisy or unwanted traffic.  To configure a mirror filter, follow these steps:

- From the VPC dashboard select: ``Mirror Filters`` under the Traffic Mirroring section in the left window pane.
- Select: ``Create traffic mirror filter``
- Add the appropriate inbound and outbound rules.  For mor details about traffic mirror filters please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filters.html
- Select: ``Create``

Create Mirror Session
---------------------

A traffic mirror session defines the source of the traffic to be mirrored based on the selected traffic mirror filters and sends that traffic to the desired traffic mirror target.  For more details about traffic mirror sessions please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html

- From the VPC dashboard select: ``Mirror Sessions`` under the Traffic Mirroring section in the left window pane.
- Select: ``Create traffic mirror session``
- Under the Mirror source section, choose the interface that you want to be mirrored.
- Under the Mirror target section, choose the interface or load balancer you want to send the mirrored traffic to.
- Assign a session number under the Additional settings section for the mirror session.
- In the filters section under Additional settings choose the mirror filter you want to apply to the mirrored traffic.
- Select: ``Create``

Verify Traffic Mirroring
------------------------

To verify the mirror session is sending the correct data to the sniffing interface run the following command on the Security Onion AWS Sensor instance:

::

    sudo tcpdump -nni <interface> 


You should see ``VXLAN`` tagged traffic being mirrored from the interface you selected as the Mirror Source.

To verify :ref:`zeek` is properly decapsulating and parsing the VXLAN traffic you can verify logs are being generated in the ``/nsm/zeek/logs/current`` directory:

::

    ls -la /nsm/zeek/logs/current/
