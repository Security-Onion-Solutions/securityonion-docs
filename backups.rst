.. _backups:

Backups
=======

Security Onion 2 performs daily backups of some critical files so that you can recover your grid from a catastophic failure of the manager. Daily backups create a tar file located in /nsm/backups directory located on the manager. 

What is being backed up?
------------------------

/etc/pki  

All of the certs including the CA are backed up. Restoring this would allow you to communicate with your salt minions again.

/opt/so/saltstack/local

This includes all of minion sls files and all other sls customizations. 

Kibana Customizations
---------------------

SOC Users
---------

thehive
-------

