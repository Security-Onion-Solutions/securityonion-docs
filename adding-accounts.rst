Adding Accounts
===============

OS
--

If you need to add a new OS user account, you can use the ``adduser`` command.  For example, to add a new account called ``tom``:

::

    sudo adduser tom

For more information, please see ``man adduser``.

Application
-----------

If you need to add a new SSO (Sguil/Squert/Kibana) account, you can use the ``so-user-add`` command (please note that SSO usernames must be alphanumeric):

::

    sudo so-user-add

If you've enabled Elastic authentication, you can manage user accounts in Kibana under Management -> Users.
