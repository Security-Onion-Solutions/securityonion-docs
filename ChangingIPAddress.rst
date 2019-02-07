Changing IP Addresses
=====================

If you need to update the IP address of your server/sensor to move it to
a different area of your network, you need to do a few things:

-  update the actual IP address of the management interface
-  update NSM config files to reflect the new IP address

Update the actual IP address of the management interface
--------------------------------------------------------

To update the actual IP address of the management interface, you have
two options:

-  manually update ``/etc/network/interfaces``\ 
   OR
-  re-run the ``FIRST`` phase of Setup (select "Yes, configure
   /etc/network/interfaces)

Update NSM config files to reflect the new IP address
-----------------------------------------------------

To update NSM config files to reflect the new IP address, you have two
options:

-  re-run the ``SECOND`` phase of Setup on all server/sensors
   ``(wiping all data and config)``
   OR
-  manually update the IP address as shown below

Files to update when changing the IP address
--------------------------------------------

Changing Server IP
~~~~~~~~~~~~~~~~~~

-  /etc/nsm/HOSTNAME-INTERFACE/http\_agent.conf:

   ::

       set SERVER_HOST [SERVER-IP]

-  /etc/nsm/HOSTNAME-INTERFACE/pads\_agent.conf:

   ::

       set SERVER_HOST [SERVER-IP]

-  /etc/nsm/HOSTNAME-INTERFACE/pcap\_agent.conf:

   ::

       set SERVER_HOST [SERVER-IP]

-  /etc/nsm/HOSTNAME-INTERFACE/sancp\_agent.conf:

   ::

       set SERVER_HOST [SERVER-IP]

-  /etc/nsm/HOSTNAME-INTERFACE/sensor.conf:

   ::

       SENSOR_SERVER_HOST="[SERVER-IP]"

-  /etc/nsm/HOSTNAME-INTERFACE/snort\_agent-N.conf:

   ::

       set SERVER_HOST [SERVER-IP]

-  /etc/nsm/ossec/ossec\_agent.conf:

   ::

       set SERVER_HOST [SERVER-IP]

-  /root/.ssh/securityonion\_ssh.conf

   ::

       SERVERNAME=[SERVER-IP]

-  /etc/elsa\_web.conf

   ::

       "pcap_url": "https://[SERVER-IP]/capme"

-  /etc/salt/minion.d/onionsalt.conf

   ::

       master: [SERVER-IP]

Automating the change of the server IP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You may be able to use sed to update all files at once using something
like this:

::

    sudo service nsm stop
    sudo sed -i 's|OLD.SERVER.IP.ADDR|NEW.SERVER.IP.ADDR|g' /etc/nsm/*/*agent* /etc/nsm/*/sensor.conf /root/.ssh/securityonion_ssh.conf /etc/salt/minion.d/onionsalt.conf /etc/elsa_web.conf
    sudo service nsm start
