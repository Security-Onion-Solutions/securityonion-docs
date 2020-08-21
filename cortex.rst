.. _cortex:

Cortex
======

From https://github.com/TheHive-Project/Cortex:

    Cortex tries to solve a common problem frequently encountered by SOCs, CSIRTs and security researchers in the course of threat intelligence, digital forensics and incident response: how to analyze observables they have collected, at scale, by querying a single tool instead of several?

    Cortex, an open source and free software, has been created by TheHive Project for this very purpose. Observables, such as IP and email addresses, URLs, domain names, files or hashes, can be analyzed one by one or in bulk mode using a Web interface. Analysts can also automate these operations thanks to the Cortex REST API.
  
Usage
-----

.. image:: https://user-images.githubusercontent.com/1659467/87231233-586ea600-c383-11ea-926e-911030c47796.png

In Security Onion, Cortex is set up with two default organizations:

 - ``cortex`` - This is a default organization that is created by Cortex for overall management.
 - ``SecurityOnion`` - This is an organization that we create to enable analyzers by default and provide integration with TheHive.

Users initially authenticate to Cortex via the username and password supplied during setup.  Once authenticated to the Cortex organization, users will possess `superadmin` privileges, capabable of managing all organizations, users, etc.

From here, users should create an additonal user for the `SecurityOnion` organization, or create their own ogranization/users if they wish to log into Cortex and manage analyzers and responders.

It is always recommended that you create your own organization, but the provided organizations should work for testing.

More Information
----------------

.. seealso::

    For more information about Cortex, please see https://github.com/TheHive-Project/Cortex.
