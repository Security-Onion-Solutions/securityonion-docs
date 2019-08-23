Disabling Accounts
==================

OS
--

If you need to disable an OS user account, you can expire the account using ``usermod --expiredate 1``.  For example, to disable the account for user ``tom``:

::

    sudo usermod --expiredate 1 tom

For more information, please see ``man passwd`` and ``man usermod``.

SSO
---

If you need to disable a SSO (Sguil/Squert/Kibana) account, you can use the ``so-user-disable`` command:

::

    sudo so-user-disable

If you later need to re-enable this SSO account, you can use the ``so-user-passwd`` command to reset the password which will automatically re-enable the account.

Elastic
-------

If you've enabled Elastic authentication, you can manage Elastic user accounts in Kibana under Management --> Users.
