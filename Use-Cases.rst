Use Cases
=========

Security Onion is designed for many different use cases! Here are just a
few examples.

Classroom
---------

Evaluation Mode is ideal for classroom or lab environments.

Install Security Onion. Run Setup and configure network interfaces.
Reboot, run Setup, and then choose Evaluation Mode.

| For more information, please see:
| https://github.com/Security-Onion-Solutions/security-onion/wiki/QuickISOImage

Pcap Forensics
--------------

Need to review a pcap with original timestamps preserved? Install
Security Onion in Evaluation Mode as described above and then run
`so-import-pcap <so-import-pcap>`__.

Production Server - Standalone
------------------------------

Install Security Onion. Run Setup and configure network interfaces.
Reboot, run Setup, choose Production Mode, choose New Deployment, and
enable network sensor services.

| For more information, please see:
| https://github.com/Security-Onion-Solutions/security-onion/wiki/ProductionDeployment

Production Server - Distributed Deployment
------------------------------------------

| Install Security Onion on the master server box. Run Setup and
  configure network interfaces. Reboot, run Setup, choose Production
  Mode, and then choose New Deployment.
| 
| Install Security Onion on one or more nodes and then on each one: run
  Setup, configure network interfaces, reboot, run Setup choose
  Production Mode, and then choose Existing Deployment to join to
  master.

| For more information, please see:
| https://github.com/Security-Onion-Solutions/security-onion/wiki/ProductionDeployment

Analyst VM
----------

Install Security Onion in a VM on your local desktop or laptop. Do NOT
run Setup. Launch the Sguil client and connect to sguild on your
Production Master Server. Launch the web browser and connect to Squert
or Kibana on your Production Master Server.

| For more information, please see:
| https://github.com/Security-Onion-Solutions/security-onion/wiki/ConnectingtoSguil#directly-connecting-to-sguild-remotely

Sensor sending logs to SIEM
---------------------------

Install Security Onion on a sensor box and then configure it to send
logs to your SIEM.

| For more information, please see:
| `Sending logs to SIEM <ThirdPartyIntegration>`__
