.. _cortex:

Cortex
======

From https://github.com/TheHive-Project/Cortex:

    Cortex tries to solve a common problem frequently encountered by SOCs, CSIRTs and security researchers in the course of threat intelligence, digital forensics and incident response: how to analyze observables they have collected, at scale, by querying a single tool instead of several?

    Cortex, an open source and free software, has been created by TheHive Project for this very purpose. Observables, such as IP and email addresses, URLs, domain names, files or hashes, can be analyzed one by one or in bulk mode using a Web interface. Analysts can also automate these operations thanks to the Cortex REST API.
  
Credentials
-----------

| Username: cortexeadmin  
| Password: cortexchangeme  

.. image:: https://user-images.githubusercontent.com/1659467/87231233-586ea600-c383-11ea-926e-911030c47796.png

After logging in, change the password for the superadmin account (``cortexadmin``), and configure a password for the ``soadmin`` account (``SecurityOnion`` organization).

After specifying a password for the ``soadmin`` user, log in to Cortex with the same account. You should then be able to configure additional analyzers or details, as needed.

Note that the ``soadmin`` user already has a random API key generated upon initial setup, and that is used for integration with TheHive and SOCtopus. If you change this value, you must also change the value in ``/opt/so/saltstack/local/pillar/static.sls`` and re-run any applicable Salt states.

Usage
-----

In Security Onion, Cortex is set up with two default organizations:

 - ``cortex`` - This is a default organization that is created by Cortex for overall management.
 - ``SecurityOnion`` - This is an organization that we create to enable analyzers by default and provide integration with TheHive.

It is always recommended that you create your own organization, but the provided organizations should work for testing.

More Information
----------------

For more information about Cortex, please see https://github.com/TheHive-Project/Cortex.
