Security Onion VPC Traffic Mirroring Configuration
============

Overview
-----------------------------------------

This guide does cover network connectivity to a Security Onion node. This can be achieved through
configuring an external IP for the node’s management interface, or through the use of a VPN connection
via OpenVPN, PfSense etc.

For an example, please see:

https://medium.com/@svfusion/setup-site-to-site-vpn-to-aws-with-pfsense-1cac16623bd6

This guide also does not cover how to set up a VPC in AWS.

For an example, please see:

https://docs.aws.amazon.com/directoryservice/latest/admin- guide/gsg_create_vpc.html


Create a Security Group for Sniffing Interface 
-----------------

Security Groups act like a firewall for your Amazon EC2 instances controlling both inbound and outbound traffic. We will need to create a Secuity Group specifically for the interface we will be using to sniff the traffic.  This Security Group will need to be as open as possible to ensure all traffic destined to the sniffing interface will be allowed through.

- From the EC2 Dashboard Select Security Groups under the Network & Security sections in the left window pane.
- Select ``Create Security Group``
- Provide as Security Group Name and Description
- Select the appropriate VPC for the Security Group 
- With the inbound tab selected, Select Add Rule. 
- Add the appropriate inbound rules to ensure all desired traffic destined for the sniffing interface is allowed.
- Select ``Create``

Create Sniffing Interface
----------------

Prior to launching the Security Onion AMI you may want to create the interface that will be used to monitor your VPC.  This interface will be attached to the Security Onion AMI as a secondary interface.  

- From the EC2 Dashboard select ``Network Intrefaces`` under the Network & Security section in the left window pane. 
- Select ``Create Network Interface``
- Provide a description and choose the appropriate subnet you want to monitor. -- need to verify this statement
- Select the security Group that you created for the sniffing interface
- Select ``Create``


Create Security Onion EC2 instance in Amazon Web Services (AWS)
---------------------------------

- From the EC2 Dashboard select Launch Instance
- Select the ``Community AMI's`` option in the left pane and search for ``Security-Onion-16.04`` in the search bar.
- Select ``Security-Onion-16.04.x.x`` AMI
- Choose the appropriate instance type based on the hardware requirements and select ``Next: Configure Instance Details``.  For assistance on determining resource requirements please visit our Hardware Requirmentmest section. 

    https://securityonion.readthedocs.io/en/latest/hardware.html

- From the subnet drop-dow select the same subnet as the sniffing interface.
- Under the Network interfaces section configure eth0 (management interface).
- Under the Network interfases section select ``Add Device`` to attach the previously created sniffing interface to the instance.
- From the Network Interface Drop-down for eth1 choose the sniffing interface.  Please note if you have multiple interfaces listed you can verify the correct interface by navigating to the Network Interfaces section in the EC2 Dashboard.
- Select ``Next: Add Storage`` and configure the Volume settings
- Select ``Next: Add Tags`` and add any additional tags for the instance.
- Select ``Next: Configure Security Group`` and add the appropriate inboud rules
- Select ``Review and Launch``
- If promtped to select the appropriate SSH keypair that will be used to ssh into the Security Onion instance for administation. 
- Please note that the default username for the Security-Onion-16.04 AMI is ``onion``
- Once you have logged in, run the following commands:

::

    sudo soup
    sudo sosetup


Traffic Mirroring
---------------------------------

Traffic Mirroring allows you to copy the traffic from an interface on an instance and send it to a single interface or a group of interfaces using a network load balancer.  For more details about AWS Traffic Mirroring please see: https://docs.aws.amazon.com/vpc/latest/mirroring/what-is-traffic-mirroring.html

Create Mirror Target
---------------------------------

A mirror target in AWS refers to the destinaion for the mirrored traffic.  This can be a single interface or a group of interfaces using a network load balancer.  To set up a Mirror target follow these steps.

- From the VPC Dashboard select ``Mirror Targets`` under the Traffic Mirroring section in the left window pane
- Select ``Create traffic mirror target``
- Under the Choose target section choose the appropriate target type and choose the sniffing interface connected to the Security Onion instance.  For more details about traffic mirror targest please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-targets.html
- Select ``Create``

Create Mirror Filter
---------------------------------

A mirror filters allow you to define the traffic that is copied to in the mirrored session and is useful for tuning out noisey or unwanted traffic.  To set up a Mirror Filter follow these steps.

- From the VPC Dashboard select ``Mirror Filters`` under the Traffic Mirroring section in the left window pane
- Select ``Create traffic mirror filter``
- Add the appropriate inbound and outbound rules.  For mor details about traffic mirror filters please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-filters.html
- Select ``Create``

Create Mirror Session
-------------------------------

A traffic mirror session defines the source of the traffic to be mirrored, based on traffic mirror filters, to the desired traffic mirror target.  For more details about traffic mirror sessions please see: https://docs.aws.amazon.com/vpc/latest/mirroring/traffic-mirroring-session.html

- From the VPS Dashboard select ``Mirror Sessions`` under the Traffic Mirroring section in the left window pane
- Select ``Create traffic mirror session``
- Under the Mirror source section choose interface that you want to be mirrored
- Under the Mirror target section choose the interface or load balancer you want to send the mirrored traffic to
- Assign a Session number under the Additional settings section for the mirror session
- In the filters section under Additional settings choose the mirror filer you want to apply to the mirrored traffic
- Select ``Create``






