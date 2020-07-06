.. _Adding-Accounts:

Adding Accounts
===============

OS
--

If you need to add a new OS user account, you can use the ``adduser`` command.  For example, to add a new account called ``tom``:

::

    sudo adduser tom

For more information, please see ``man adduser``.

SSO
---

If you need to add a new Security Onion Console (SOC) account, you can use the ``so-user-add`` command (please note that SSO usernames must be alphanumeric):

::

    sudo so-user-add

Elastic
-------

If you've enabled Elastic authentication, you can manage Elastic user accounts in Kibana under Management --> Users.
