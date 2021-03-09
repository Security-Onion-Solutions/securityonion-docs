.. _host:

Host Visibility
===============

When you logged into :ref:`soc`, you may have seen some host logs from :ref:`wazuh`. Security Onion can also consume many other kinds of host logs as well. You can send logs to Security Onion via :ref:`osquery`, :ref:`beats`, :ref:`wazuh`, or :ref:`syslog`. 

For Windows endpoints, you can optionally augment the standard Windows logging with :ref:`sysmon` and/or :ref:`autoruns`. Those additional logs can then be transported by whatever mechanism you chose above.

.. toctree::
   :maxdepth: 2

   osquery
   beats
   wazuh
   syslog
   sysmon
   autoruns
