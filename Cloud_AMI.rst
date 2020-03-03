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
- Select 'Create Security Group'
- Provide as Security Group Name and Description
- Select the appropriate VPC for the Security Group 
- With the inbound tab selected, Select Add Rule. 
- Add the appropriate inbound rules to ensure all desired traffic destined for the sniffing interface is allowed.
- Select the Create button when finished.

Create Sniffing Interface
----------------

Prior to launching the Security Onion AMI you may want to create the interface that will be used to monitor your VPC.  This interface will be attached to the Security Onion AMI as a secondary interface.  

- From the EC2 Dashboard Select Network Intrefaces under the Network & Security section in the left window pane. 
- Select Create Network Interface
- Provide a description and choose the appropriate subnet you want to monitor. -- need to verify this statement
- Select the Security Group that you created for the Sniffing Interface
- Select Create


Create Security Onion EC2 instance in Amazon Web Services (AWS)
---------------------------------

- From the EC2 Dashboard select Launch Instance
- Select the Community AMI's option in the left pane and search for ``Security-Onion-16.04`` in the search bar.
- Select Security-Onion-16.04.x.x AMI
- Choose the appropriate instance type based on the hardware requirements and select ``Next: Configure Instance Details``.  For assistance on determining resource requirements please visit our Hardware Requirmentmest section. 

    https://securityonion.readthedocs.io/en/latest/hardware.html

- From the subnet drop-dow select the same subnet as the sniffing interface.
- Under the Network interfaces section configure eth0 (management interface).
- Under the Network interfases section select Add Device to attach the previously created sniffing interface to the instance.
- From the Network Interface Drop-down for eth1 choose the sniffing interface.  Please note if you have multiple interfaces listed you can verify the correct interface by navigating to the Network Interfaces section in the EC2 Dashboard.
- Select Next: Add Storage and configure the Volume settings
- Select Next: Add Tags and add any additional tags for the instance.
- Select Next: Configure Security Group and add the appropriate inboud rules
- Select Review and Launch
- If promtped to select the appropriate SSH keypair that will be used to ssh into the Security Onion instance for administation.  




