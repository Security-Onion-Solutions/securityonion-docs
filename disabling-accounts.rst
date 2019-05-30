Disabling Accounts
==================

OS
--

If you need to disable an OS user account, you can expire the account using ``usermod --expiredate 1``.  For example, to disable the account for user ``tom``:

::

    sudo usermod --expiredate 1 tom

For more information, please see ``man passwd``.

SSO
---

If you need to disable a SSO (Sguil/Squert/Kibana) account, you can use the ``so-user-disable`` command:

::

    sudo so-user-disable
