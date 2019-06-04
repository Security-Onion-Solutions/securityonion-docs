Use Cases
=========

Security Onion is designed for many different use cases! Here are just a few examples.

Pcap Forensics
--------------

One of the easiest ways to get started with Security Onion is using it to forensically analyze one or more pcap files. Just install Security Onion and then run `so-import-pcap <so-import-pcap>`__ on one or more of the pcap files in ``/opt/samples/``.  For example, to import the ``2019`` pcaps in ``/opt/samples/mta/``:

::

  sudo so-import-pcap /opt/samples/mta/2019*

Classroom
---------

``Evaluation Mode`` is ideal for classroom or small lab environments.

Install Security Onion. Run Setup and configure network interfaces. Reboot, run Setup again, and then choose ``Evaluation Mode``.

For more information, please see the `Quick Evaluation <QuickISOImage>`__ section.

Production Server - Standalone
------------------------------

Install Security Onion. Run Setup and configure network interfaces.  Reboot, run Setup again, choose ``Production Mode``, choose ``New Deployment``, and enable network sensor services.

For more information, please see the `Production Deployment <ProductionDeployment>`__ section.

Production Server - Distributed Deployment
------------------------------------------

Install Security Onion on the master server box. Run Setup and configure network interfaces. Reboot, run Setup again, choose ``Production Mode``, and then choose ``New Deployment``.
 
Install Security Onion on one or more nodes and then on each one: run Setup, configure network interfaces, reboot, run Setup again, choose ``Production Mode``, and then choose ``Existing Deployment`` to join to master.

For more information, please see the `Production Deployment <ProductionDeployment>`__ section.

Analyst VM
----------

If you've built a Production Server as described above, you may want to connect to it using an `Analyst VM <Analyst-VM>`_.  Install Security Onion in a VM on your local desktop or laptop. You do NOT need to run Setup in the Analyst VM since this VM won't be running any services, only applications such as `<Sguil>`_, `Wireshark <wireshark>`_, `NetworkMiner <networkminer>`_, and a web browser.

For more information, please see the `<Analyst-VM>`__ section.

Sending Logs to Separate SIEM
-----------------------------

You can install Security Onion and then configure it to send logs to a separate SIEM.

For more information, please see the `Syslog Output <syslog-output>`__ section.
