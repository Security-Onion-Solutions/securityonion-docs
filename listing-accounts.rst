Listing Accounts
================

OS
--

OS user accounts are stored in ``/etc/passwd``.  You can get a list of all OS accounts using the following command:

::

  cut -d: -f1 /etc/passwd
  
::

Furthermore, you can get a list of all OS accounts that had a UID > 1000 (not a service account) using the following command:

::

  cat /etc/passwd | awk -F: '$3 > 1000 {print ;}' | cut -d: -f1 
  
SSO
---

To list all SSO (Sguil/Squert/Kibana) accounts, you can use the ``so-user-list`` command:

::

    sudo so-user-list

Elastic
-------

If you've enabled Elastic authentication, you can manage Elastic user accounts in Kibana under Management --> Users.
