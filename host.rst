.. _host:

Host Visibility
===============

When you logged into :ref:`soc`, you may have seen some host logs from :ref:`wazuh`. Security Onion can also consume many other kinds of host logs as well. You can send logs to Security Onion via your choice of either :ref:`osquery`, :ref:`beats`, :ref:`wazuh`, or :ref:`syslog`:

- Choose :ref:`osquery` if you want some live response actions and maybe light log transport. A good example here is a roaming laptop where log volume is low and you might want to send its logs to a dedicated :ref:`fleet` node in the DMZ.
- Choose :ref:`wazuh` if you want HIDS functionality and log transport.
- Choose :ref:`beats` for dedicated log transport. Examples would be high volume domain controllers or Windows Event Collectors.
- Choose :ref:`syslog` if you can't install an agent but the device supports sending standard syslog. Examples include firewalls, switches, routers, and other network devices.

For Windows endpoints, you can optionally augment the standard Windows logging with :ref:`sysmon` and/or :ref:`autoruns`. Those additional logs can then be transported by whatever mechanism you chose above.

.. toctree::
   :maxdepth: 2

   osquery
   beats
   wazuh
   syslog
   sysmon
   autoruns
