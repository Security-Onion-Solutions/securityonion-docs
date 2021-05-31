.. _backups:

Backups
=======

Security Onion 2 performs daily backups of some critical files so that you can recover your grid from a catastophic failure of the manager. Daily backups create a tar file located in the ``/nsm/backup/`` directory located on the manager. 

What is being backed up?
------------------------

- ``/etc/pki/``

  All of the certs including the CA are backed up. Restoring this would allow you to communicate with your salt minions again.

- ``/opt/so/saltstack/local/``

  This includes all minion sls files and customizations. 

Kibana Customizations
---------------------

Kibana customizations are located in the ``.kibana`` indices. Periodic snapshots of this data will preserve them in case of failure. You can also utilize true elastic clustering to add replicas to ensure quick recovery.

Elastic Data
------------

Users can enable snapshots with :ref:`curator` to snapshot data to an external storage device such as a NAS. True Elastic clustering will allow you to have redundancy in case of a single node failure if you enable replicas. However, please keep in mind that enabling replicas doubles your storage needs.
