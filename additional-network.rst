.. _additional-network:

Additional Network Visibility
=============================

In the :ref:`network` section, we looked at network visibility provided by Security Onion itself. In addition to this native visibility, you probably have other devices on your network that provide additional network visibility and you might want to send that data to Security Onion for storage and correlation with other data sources. One option would be :ref:`netflow` logs from firewalls, switches, or routers showing what traffic was observed by the network device. Another option would be firewall logs showing what traffic was allowed through the firewall and what traffic was denied. An example of that would be :ref:`pfsense` firewall logs. 

.. toctree::
   :maxdepth: 2

   netflow
   pfsense
