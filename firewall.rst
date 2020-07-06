Firewall
========

Setup defaults to only allowing port 22 (ssh)
---------------------------------------------

When you run Setup, it defaults to locking down the local firewall to only allowing port 22 (ssh).  If you need to allow connections on other ports, you can run the `<so-allow>`_ utility.

Sensors automatically add their own firewall rules to the management server
---------------------------------------------------------------------------

When you run Setup on a sensor-only installation, it will ssh to the management server and add new firewall rules to the management server to allow the sensor to connect on the following ports:

-  22/tcp (ssh)
-  4505/tcp (salt)
-  4506/tcp (salt)
