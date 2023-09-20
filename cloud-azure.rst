.. _cloud-azure:

Azure Cloud Image
=================

If you would like to deploy Security Onion 2.3 in Azure, we have an Azure compatible image that is already built for you. As this is an older Security Onion version, it must be accessed via the Azure CLI rather than the Azure Marketplace.

.. warning::

   Existing Security Onion installations in Azure should use the :ref:`soup` command to upgrade to newer versions of Security Onion. Attempting to switch to a newer image from the Azure Marketplace could cause loss of data and require full grid re-installation.
    
.. note::

   Azure has put on hold their Virtual TAP preview feature, which means in order to install a Security Onion sensor in the Azure cloud you will need to use a packet broker offering from the Azure Marketplace. See more information here: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview

.. note::

   This section does not cover network connectivity to the Security Onion node. This can be achieved through configuring an external IP for the node’s management interface, or through the use of a VPN connection via OpenVPN. 

.. note::

   This section does not cover how to set up a virtual network in Azure. For more details about setting up a virtual network, please see https://docs.microsoft.com/en-us/azure/virtual-network/.

Requirements
############

Before proceeding, determine the grid architecture desired. Choose from a single-node grid versus a distributed, multi-node grid. 

While Azure has recently begun offering ephemeral storage, which potentially could offer increased disk performance for search nodes, the setup required for configuring them is out of scope of this documentation. We recommend using either Premium SSD disks, or the more expensive Ultra SSD disks, with suitable IOPS and throughput matched to your expected network monitoring requirements.

Single Node Grid
----------------

For simple, low-volume production monitoring, a single node grid can be used.

Listed below are the minimum suggested single-node instance quantities, sizes, and storage requirements for either standalone or evaluation installations (choose one, not both). Note that when using virtual machines with the minimum RAM requirements you may need to enable memory swapping.

Standalone:

- Quantity: 1
- Type: Standard_D4as_v4
- Storage: 200GB Premium SSD

Evaluation

- Quantity: 1
- Type: Standard_D8as_v4
- Storage: 200GB Premium SSD
  
Distributed Grid
----------------

For high volume production monitoring, choose a multi-node grid architecture. At least two search nodes are recommended for redundancy purposes.

Listed below are the minimum suggested distributed grid instance quantities, sizes, and storage requirements. Note that when using virtual machines with the minimum RAM requirements you may need to enable memory swapping.

VPN Node

- Quantity: 1
- Type: Option 1: Standard_B1s - Lower cost for use with low vpn traffic volume
- Type: Option 2: Standard_D4as_v4 w/ accelerated networking - Higher cost for high vpn traffic volume
- Storage: 64GB Premium SSD
  
Manager

- Quantity: 1
- Type: Standard_D4as_v4
- Storage: 256GB Premium SSD
  
Search Nodes

- Quantity: 2 or more
- Type: Standard_D4as_v4
- Storage: 256GB Premium SSD
  
Sensor monitoring the VPN ingress

- Quantity: 1
- Type: Standard_D4as_v4
- Storage: 512GB Premium SSD

Create Monitoring Interface 
###########################

To setup a Security Onion sensor node in Azure, follow the prerequisite steps below prior to creating the sensor VM.

Create a Security Group for Sniffing Interface 
----------------------------------------------

Security Groups act like a firewall for your Azure virtual machines, controlling both inbound and outbound traffic. You should consider whether a security group is needed for your virtual network, and specifically for the interface that you will be using to sniff the traffic.  This security group will need to be as open as possible to ensure all traffic destined to the sniffing interface will be allowed through.  To create a security group, follow these steps:

- In the Azure Dashboard search for: ``Network security groups``.
- Select: ``Create``
- Provide a name, such as ``so-monitoring-security-group``.
- Select the appropriate resource group and region. 
- Select ``Review + Create``
- Review the summary
- Select: ``Create``
- Select: ``Go to resource``
- Adjust the Inbound security rules to ensure that all incoming monitoring traffic is allowed.

Create Sniffing Interface
-------------------------

Prior to launching the Security Onion sensor virtual machine you will need to create the interface that will be used to monitor your virtual network.  This interface will be attached to the Security Onion sensor virtual machine as a secondary interface.  To create a sniffing interface, follow these steps:

- In the Azure Dashboard search for: ``Network interfaces``. 
- Select: ``Create``
- Provide a name, such as ``so-monitoring-interface``.
- Choose the resource group, region, virtual network, subnet, security group from the steps above, and IP settings.
- Select: ``Review + Create``
- Review the summary
- Select: ``Create``

Create Security Onion Instances
###############################

Instance Creation
-----------------

As this is an older Security Onion version, it must be accessed via the Azure CLI rather than the Azure Marketplace. To configure a Security Onion instance (repeat for each node in a distributed grid), follow these steps:

- Using the Azure CLI (available in the Azure web portal if not installed locally) run the following commands to launch a new Security Onion 2.3 instance, adjusting the parameters as needed:

::

  az vm image terms show --urn securityonionsolutions:securityonion:so2:2.3.260
  az vm image terms accept --urn securityonionsolutions:securityonion:so2:2.3.260
  az group create --name mySOGroup --location eastus
  az vm create \
    --resource-group mySOGroup \
    --name so-vm-manager \
    --admin-username onion \
    --generate-ssh-keys \
    --image securityonionsolutions:securityonion:so2:2.3.260 \
    --plan-name so2 \
    --plan-product securityonion \
    --plan-publisher securityonionsolutions \
    --size Standard_D8ds_v4

- Choose the appropriate Size based on the desired hardware requirements. For assistance on determining resource requirements please review the Requirements section above.
- Ensure you have access to the generated SSH private key, or copy the key locally if using the Azure CLI in the web portal
- Stop the new VM after deployment completes.
- Edit the VM and:

  - Adjust the OS disk size to be at least 100GB in size.
  - For single-node grids, distributed sensor nodes, or distributed search nodes: If you would like to separate the ``/nsm`` partition into its own disk, create and attach a data disk for this purpose, with a minimum size of 100GB, or more depending on predicted storage needs. Note that the size of the ``/nsm`` partition determines the rate that old packet and event data is pruned. Separating the /nsm partition can provide more flexibility with scaling up the grid node sizes, but requires a little more setup, which is described later.
  - If this VM is a single-node grid, or is sensor node, attach the monitoring network interface created earlier.
  - Adjust public IP, virtual networks, etc as necessary.
  
- Start the VM.

Note that you'll need to reference the SSH public key when using SSH to access the new VMs. For example:

::

    chmod 600 ~/Downloads/onion.pem
    ssh -i ~/Downloads/onion.pem onion@11.22.33.44

Manager Setup
#############

After SSH'ing into the node, setup will begin automatically. Follow the prompts, selecting the appropriate install options. Continue instructions below for applicable nodes.

.. note::

  As Security Onion 2.3 approaches EOL, new cloud images are no longer being released. However, maintenance releases are available for cloud installation. After the manager completes setup it is important to run ``sudo soup`` to apply all newer maintenance releases and patches. This only is necessary on the manager node.

All Distributed Manager Nodes
-----------------------------

For distributed manager nodes, if connecting sensors through the VPN instance, adjust the Security Onion firewall as shown in the below commands:

Run ``so-firewall includehost minion <inside interface of your VPN concentrator>``. Ex:

::

	so-firewall includehost minion 10.99.1.10

Run ``so-firewall includehost sensor <inside interface of your VPN concentrator>``. Ex:

::

	so-firewall --apply includehost sensor 10.99.1.10

At this time your Manager is ready for remote minions to start connecting.

Search Node Setup
#################

Follow standard Security Onion search node installation, answering the setup prompts as applicable. 

Remote Sensor Setup
###################

Setup the VPN (out of scope for this guide) and connect the sensor node to the VPN.
When prompted to choose the management interface, select the VPN tunnel interface, such as ``tun0``. Use the internal IP address of the manager inside Azure when prompted for the manager IP.

Azure Sensor Setup
##################

SSH into the sensor node and run through setup to set this node up as a sensor. Choose ``eth0`` as the main interface and ``eth1`` as the monitoring interface.

.. note::

   Azure has put on hold their Virtual TAP preview feature, which means in order to install a Security Onion sensor in the Azure cloud you will need to use a packet broker offering from the Azure Marketplace. See more information here: https://docs.microsoft.com/en-us/azure/virtual-network/virtual-network-tap-overview

Verify Monitoring Traffic
-------------------------

To verify the Azure sensor is receiving the correct data on the sniffing interface run the following command on the Security Onion Azure sensor instance:

::

    sudo tcpdump -nni eth1 


To verify :ref:`zeek` is properly decapsulating and parsing the traffic you can verify logs are being generated in the ``/nsm/zeek/logs/current`` directory:

::

    ls -la /nsm/zeek/logs/current/
