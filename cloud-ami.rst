Cloud AMI
=========

Security Onion VPC Traffic Mirroring Configuration

.. warning::

    THE CLOUD AMI IS STILL IN TESTING!  IF IT BREAKS YOU CAN KEEP ALL THE PIECES.

This section covers configuring a Security Onion 16.04 cloud image hosted in Amazon Web Services (AWS) to receive mirrored/spanned traffic from other instances hosted within an Amazon Virtual Private Cloud (VPC). 

.. note::

    You can only mirror traffic from an EC2 instance that is powered by the AWS Nitro system.  For a list of supported Nitro systems please see: 
    
    https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances

.. note::

    This section does not cover network connectivity to the Security Onion node. This can be achieved through
configuring an external IP for the node’s management interface, or through the use of a VPN connection
via OpenVPN, PfSense etc.
    
    For more details about vpn connections please see:
    
    https://medium.com/@svfusion/setup-site-to-site-vpn-to-aws-with-pfsense-1cac16623bd6

.. note::

    This guide does not cover how to set up a VPC in AWS.
    
    For more details about setting up a VPC please see:
    
    https://docs.aws.amazon.com/directoryservice/latest/admin-guide/gsg_create_vpc.html

################
Getting Started 
################

**********
Terraform 
**********
To quickly setup a VPC, mirror configuration, and test the Security Onion AMI using Terraform, see the following:   
https://github.com/Security-Onion-Solutions/securityonion-cloud/tree/dev

*******
Manual 
*******
To setup the Security Onion AMI and VPC mirror configuration manually, use the steps below.

Create a Security Group for Sniffing Interface 
-----------------

Security Groups act like a firewall for your Amazon EC2 instances controlling both inbound and outbound traffic. We will need to create a security group specifically for the interface we will be using to sniff the traffic.  This security group will need to be as open as possible to ensure all traffic destined to the sniffing interface will be allowed through.  To create a security group, follow these steps:

- From the EC2 Dashboard Select: ``Security Groups`` under the Network & Security sections in the left window pane.
- Select: ``Create Security Group``
- Provide a Security Group Name and Description.
- Select the appropriate VPC for the security group. 
- With the inbound tab selected, select: ``Add Rule`` 
- Add the appropriate inbound rules to ensure all desired traffic destined for the sniffing interface is allowed.
- Select: ``Create``

Create Sniffing Interface
----------------

Prior to launching the Security Onion AMI you will need to create the interface that will be used to monitor your VPC.  This interface will be attached to the Security Onion AMI as a secondary interface.  To create a sniffing interface, follow these steps:

- From the EC2 Dashboard Select: ``Network Interfaces`` under the Network & Security section in the left window pane. 
- Select: ``Create Network Interface``
- Provide a description and choose the appropriate subnet you want to monitor.
- Select the security Group that you created for the sniffing interface.
- Select: ``Create``


Create a Security Onion EC2 instance in Amazon Web Services (AWS)
---------------------------------
To configure a Security Onion instance, follow these steps:

- From the EC2 dashboard select: ``Launch Instance``
- Select the ``Community AMI's`` option in the left pane and search for ``Security-Onion-16.04`` in the search bar.
- Select the ``Security-Onion-16.04`` AMI with the most recent build date.
- Choose the appropriate instance type based on the desired hardware requirements and select ``Next: Configure Instance Details``.  For assistance on determining resource requirements please visit our Hardware Requirements section. 

    https://securityonion.readthedocs.io/en/latest/hardware.html

- From the subnet drop-down menu select the same subnet as the sniffing interface.
- Under the Network interfaces section configure the eth0 (management) interface.
- Under the Network interfaces section select: ``Add Device`` to attach the previously created sniffing interface to the instance.
- From the Network Interface drop-down menu for eth1 choose the sniffing interface you created for this instance.  Please note if you have multiple interfaces listed you can verify the correct interface by navigating to the Network Interfaces section in the EC2 Dashboard.
- Select: ``Next: Add Storage`` and configure the volume settings.
- Select: ``Next: Add Tags`` and add any additional tags for the instance.
- Select: ``Next: Configure Security Group`` and add the appropriate inbound rules.
- Select: ``Review and Launch``
- If prompted, select the appropriate SSH keypair that will be used to ssh into the Security Onion instance for administration 
- Please note that the default username for the Security-Onion-16.04 AMI is: ``onion``
- Once you have logged in, please do the following steps.

    Change the hostname (Optional):
    ::
        
      sudo vim /etc/hostname
    
    Update packages:
    ::
      
      sudo soup

    Run through both phases of setup:
    ::

      sudo sosetup


Traffic Mirroring
---------------------------------

Traffic mirroring allows you to copy the traffic to/from an instance and send it to the sniffing interface of a network security monitoring sensor or a group of interfaces using a network load balancer.  For more details about AWS Traffic Mirroring please see: https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html

Create Mirror Target
---------------------------------

A mirror target in AWS refers to the destination for the mirrored traffic.  This can be a single interface or a group of interfaces using a network load balancer.  To configure a mirror target, follow these steps:

- From the VPC dashboard select: ``Mirror Targets`` under the Traffic Mirroring section in the left window pane.
- Select: ``Create traffic mirror target``
- Under the Choose target section select the appropriate target type and choose the sniffing interface connected to the Security Onion instance.  For more details about traffic mirror targets please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-targets.html
- Select: ``Create``

Create Mirror Filter
---------------------------------

A mirror filter allows you to define the traffic that is copied to in the mirrored session and is useful for tuning out noisy or unwanted traffic.  To configure a mirror filter, follow these steps:

- From the VPC dashboard select: ``Mirror Filters`` under the Traffic Mirroring section in the left window pane.
- Select: ``Create traffic mirror filter``
- Add the appropriate inbound and outbound rules.  For mor details about traffic mirror filters please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filters.html
- Select: ``Create``

Create Mirror Session
-------------------------------

A traffic mirror session defines the source of the traffic to be mirrored based on the selected traffic mirror filters and sends that traffic to the desired traffic mirror target.  For more details about traffic mirror sessions please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html

- From the VPC dashboard select: ``Mirror Sessions`` under the Traffic Mirroring section in the left window pane.
- Select: ``Create traffic mirror session``
- Under the Mirror source section, choose the interface that you want to be mirrored.
- Under the Mirror target section, choose the interface or load balancer you want to send the mirrored traffic to.
- Assign a session number under the Additional settings section for the mirror session.
- In the filters section under Additional settings choose the mirror filter you want to apply to the mirrored traffic.
- Select: ``Create``

Verify Traffic Mirroring
------------------------------

To verify the mirror session is sending the correct data to the sniffing interface run the following command on the Security Onion instance:

::

    sudo tcpdump -nni <interface> 


You should see ``VXLAN`` tagged traffic being mirrored from the interface you selected as the Mirror Source.

To verify Zeek is properly decapsulating and parsing the VXLAN traffic you can verify logs are being generated in the ``/nsm/zeek/logs/current`` directory:

::

    ls -la /nsm/zeek/logs/curent/
     




