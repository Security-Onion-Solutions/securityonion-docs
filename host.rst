.. _host:

Host Visibility
===============

Security Onion can consume many kinds of host logs. You can send logs to Security Onion via your choice of either :ref:`elastic-agent` or :ref:`syslog`:

- Choose :ref:`elastic-agent` for comprehensive telemetry. The :ref:`elastic-agent` contains multiple Beats so this can provide more information than a standalone :ref:`beats` installation.
- Choose :ref:`syslog` if you can't install an agent but the device supports sending standard syslog. Examples include firewalls, switches, routers, and other network devices.

For Windows endpoints, you can optionally augment the standard Windows logging with :ref:`sysmon` and/or :ref:`autoruns`. Those additional logs can then be transported by whatever mechanism you chose above.

.. toctree::
   :maxdepth: 2

   elastic-agent
   beats
   syslog
   sysmon
   autoruns
