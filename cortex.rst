.. _cortex:

Cortex
======

.. warning::

        Starting in Security Onion 2.3.100, we are transitioning from :ref:`hive` to :ref:`cases` and this will impact Cortex as well. Existing installations with TheHive/Cortex enabled will still be able to use TheHive/Cortex for a very short time. However, new installations will not be able to enable TheHive/Cortex. We will stop including TheHive/Cortex container images starting in Security Onion 2.3.120, currently scheduled for release in March 2022. From that point forward, users running the current version of Security Onion will no longer be able to natively run TheHive/Cortex on the platform and our support for TheHive/Cortex on Security Onion will end. Users wishing to continue using TheHive/Cortex on Security Onion should plan to migrate to an external instance of TheHive/Cortex.

From https://github.com/TheHive-Project/Cortex:

    Cortex tries to solve a common problem frequently encountered by SOCs, CSIRTs and security researchers in the course of threat intelligence, digital forensics and incident response: how to analyze observables they have collected, at scale, by querying a single tool instead of several?

    Cortex, an open source and free software, has been created by TheHive Project for this very purpose. Observables, such as IP and email addresses, URLs, domain names, files or hashes, can be analyzed one by one or in bulk mode using a Web interface. Analysts can also automate these operations thanks to the Cortex REST API.
  
Usage
-----

.. image:: https://user-images.githubusercontent.com/1659467/87231233-586ea600-c383-11ea-926e-911030c47796.png

Log into the Cortex web interface at ``/cortex`` (at the IP address or hostname of your Security Onion installation) using the same credentials that you use to log into :ref:`hive`.

In Security Onion, Cortex is set up with two default organizations:

 - ``cortex`` - This is a default organization that is created by Cortex for overall management.
 - ``SecurityOnion`` - This is an organization that we create to enable analyzers by default and provide integration with :ref:`hive`.

Users initially authenticate to Cortex via the username and password supplied during setup.  Once authenticated to the Cortex organization, users will possess `superadmin` privileges, capabable of managing all organizations, users, etc.

From here, users should create an additional user for the `SecurityOnion` organization, or create their own organization/users if they wish to log into Cortex and manage analyzers and responders.

It is always recommended that you create your own organization, but the provided organizations should work for testing.

More Information
----------------

.. seealso::

    For more information about Cortex, please see https://github.com/TheHive-Project/Cortex.
