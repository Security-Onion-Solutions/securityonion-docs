Connecting to Sguild
====================

This article will show how to connect to the Sguil server to view security alerts in real-time.

Connecting to Sguild from an Analyst Machine
--------------------------------------------

To directly connect to a Sguild server one must possess a working Sguil client. Sguil may not be easy or available for install on certain operating systems. Because of this we recommend installing Security Onion in a virtual machine on your workstation and use that to connect to sguild on your production Security Onion instance.

- To connect from the Analyst VM to your production master server, you will need to run ``so-allow`` on the master server and choose the ``analyst`` option to allow the traffic through the host-based `<firewall>`_.

- Install Security Onion in a Virtual Machine and configure the network adapter to use NAT mode by going to your VM's settings.

- Now double-click the Sguil desktop icon to launch the Sguil client.

- Fill in the IP address or DNS name of the Security Onion server and apply your credentials.

- Then select the sensors to monitor and finally click ``Start Sguil``.

Connect to Sguild Locally (not recommended)
-------------------------------------------

- Double-click the Sguil icon on the desktop of your Security Onion server.

- Set the Sguil Host to localhost, enter your credentials, and then click OK.

- After, choose which sensors you would like to monitor for this sguil session and then click Start Sguil.

Connect Remotely via SSH w/ X11 Forwarding
------------------------------------------

This method requires SSH and an X11 server installed on the machine from which you will be connecting from.

If you're using OSX install the XQuartz package, Windows try ciXwin, Linux and BSD family use Xorg.

Connect to the Security Onion server via SSH while passing the X11 forwarding option ( ``-X`` ).

::

    ssh -X user@nsm

Once logged in as the normal user open the sguil client application. The display will be sent to your machine using the X11 protocol over SSH.

::

    sguil.tk

Since we're only forwarding the application window, we're connected locally i.e. as if we were sitting at the server's console. Because of this we can use ``localhost`` as the Sguild Host.

Once logged in we will be able to select which sensors we would like to monitor.

Finally, select Start Sguil. Now you can view the alerts in real-time, perform advanced SQL queries, and pivot into a number of applications like Wireshark, Kibana, and NetworkMiner.
