Use Cases
=========

Security Onion is designed for many different use cases! Here are just a few examples.

Pcap Forensics
--------------

One of the easiest ways to get started with Security Onion is using it to forensically analyze one or more pcap files. Just install Security Onion and then run `so-import-pcap <so-import-pcap>`__ on one or more of the pcap files in ``/opt/samples/``.  For example, to import the ``2019`` pcaps in ``/opt/samples/mta/``:

::

  sudo so-import-pcap /opt/samples/mta/2019*

For more information, please see the `so-import-pcap <so-import-pcap>`__ section.

Evaluation
----------

``Evaluation Mode`` is ideal for classroom or small lab environments.  

For more information, please see the `Quick Evaluation <QuickISOImage>`__ section.

Production Server - Standalone
------------------------------

For more information, please see the `Production Deployment <ProductionDeployment>`__ section.

Production Server - Distributed Deployment
------------------------------------------

Install Security Onion on the manager box. Then install Security Onion on one or more nodes and join to the manager.

For more information, please see the `Production Deployment <ProductionDeployment>`__ section.

Sending Logs to Separate SIEM
-----------------------------

You can install Security Onion and then configure it to send logs to a separate SIEM.

For more information, please see the `Syslog Output <syslog-output>`__ section.
