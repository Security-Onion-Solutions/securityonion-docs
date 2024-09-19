.. _additional-network:

Additional Network Visibility
=============================

In the :ref:`network` section, we looked at network visibility provided by Security Onion itself. The ideal situation would be to have Security Onion network sensors covering each and every one of your network segments. If you're able to achieve that ideal situation, then you may not need any additional network visibility. However, there may be times when you simply can't cover certain network segments with Security Onion network sensors and that's when these additional options can be beneficial. Keep in mind, though, that the data that they provide is nowhere near as comprehensive as a full Security Onion network sensor. One option would be :ref:`netflow` logs from firewalls, switches, or routers showing what traffic was observed by the network device. Another option would be firewall logs showing what traffic was allowed through the firewall and what traffic was denied. An example of that would be :ref:`pfsense` or :ref:`opnsense` firewall logs. You can find other firewall integrations in the :ref:`third-party-integrations` section.

.. toctree::
   :maxdepth: 2

   netflow
   pfsense
   opnsense
