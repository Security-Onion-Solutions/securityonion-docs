.. _Analyst-VM:

Analyst VM
==========

Full-time analysts may want to create a dedicated Analyst VM. This allows you to investigate pcaps without fear of impacting your production server/sensors.

To connect from the Analyst VM to your production management server, you will need to run `<so-allow>`_ on the management server and choose the ``analyst`` option to allow the traffic through the host-based `firewall <Firewall>`_.
