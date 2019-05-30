Listing Accounts
================

OS
--

OS user accounts are stored in ``/etc/passwd``.  You can get a list of all OS accounts using the following command:

::

  cut -d: -f1 /etc/passwd
  
SSO
---

To list all SSO (Sguil/Squert/Kibana) accounts, you can use the ``so-user-list`` command:

::

    sudo so-user-list
