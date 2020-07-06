.. _analyst-vm:

Analyst VM
==========

Full-time analysts may want to create a dedicated Analyst VM. This allows you to investigate pcaps without fear of impacting your production server/sensors.

To connect from the Analyst VM to your production management server, you will need to run :ref:`so-allow` on the management server and choose the ``analyst`` option to allow the traffic through the host-based :ref:`firewall`.
