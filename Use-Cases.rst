Use Cases
=========

Security Onion is designed for many different use cases! When you run Setup, it will ask you if you want ``Evaluation Mode`` or ``Production Mode``.  Each of these modes presents different options that may be applicable to different use cases.  Here are just a few examples.

Classroom
---------

``Evaluation Mode`` is ideal for classroom or lab environments.

Install Security Onion. Run Setup and configure network interfaces. Reboot, run Setup again, and then choose ``Evaluation Mode``.

| For more information, please see:
| `<QuickISOImage>`__

Pcap Forensics
--------------

Need to review a pcap with original timestamps preserved? Install Security Onion in ``Evaluation Mode`` as described above and then run `so-import-pcap <so-import-pcap>`__.

Production Server - Standalone
------------------------------

Install Security Onion. Run Setup and configure network interfaces.  Reboot, run Setup again, choose ``Production Mode``, choose ``New Deployment``, and enable network sensor services.

| For more information, please see:
| `<ProductionDeployment>`__

Production Server - Distributed Deployment
------------------------------------------

| Install Security Onion on the master server box. Run Setup and configure network interfaces. Reboot, run Setup again, choose ``Production Mode``, and then choose ``New Deployment``.
| 
| Install Security Onion on one or more nodes and then on each one: run Setup, configure network interfaces, reboot, run Setup again, choose ``Production Mode``, and then choose ``Existing Deployment`` to join to master.

| For more information, please see:
| `<ProductionDeployment>`__

Analyst VM
----------

If you've built a Production Server as described above, you may want to connect to it using an `Analyst VM<Analyst-VM>`_.  Install Security Onion in a VM on your local desktop or laptop. You do NOT need to run Setup in the Analyst VM since this VM won't be running any services, only applications such as `<Sguil>`_, `<Wireshark>`_, `<NetworkMiner>`_, and a web browser.

To connect from the Analyst VM to your production master server, you will need to run `<so-allow>`_ on the master server and choose the ``analyst`` option to allow the traffic through the host-based `<firewall>`_.

Once you've allowed the traffic using `<so-allow>`_, you can launch the `<Sguil>`_ client and connect to sguild on your production master server and/or launch the web browser and connect to `<Squert>`_ or `<Kibana>`_ on your Production Master Server.

| For more information, please see:
| `<Analyst-VM>`__

Sending Logs to Separate SIEM
-----------------------------

You can install Security Onion and then configure it to send logs to a separate SIEM.

| For more information, please see:
| `Sending logs to SIEM <ThirdPartyIntegration>`__
