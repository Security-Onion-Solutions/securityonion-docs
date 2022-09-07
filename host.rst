.. _host:

Host Visibility
===============

Security Onion can consume many kinds of host logs. You can send logs to Security Onion via your choice of either :ref:`beats` or :ref:`syslog`:

- Choose :ref:`beats` for dedicated log transport. Examples would be high volume domain controllers or Windows Event Collectors.
- Choose :ref:`syslog` if you can't install an agent but the device supports sending standard syslog. Examples include firewalls, switches, routers, and other network devices.

For Windows endpoints, you can optionally augment the standard Windows logging with :ref:`sysmon` and/or :ref:`autoruns`. Those additional logs can then be transported by whatever mechanism you chose above.

.. toctree::
   :maxdepth: 2

   osquery
   beats
   syslog
   sysmon
   autoruns
