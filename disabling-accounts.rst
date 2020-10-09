.. _disabling-accounts:

Disabling Accounts
==================

OS
--

If you need to disable an OS user account, you can expire the account using ``usermod --expiredate 1``.  For example, to disable the account for user ``tom``:

::

    sudo usermod --expiredate 1 tom

For more information, please see ``man passwd`` and ``man usermod``.

SOC
---

If you need to disable a :ref:`soc` account, you can use the ``so-user`` command with the ``delete`` option and the user's email address. For example, to disable the account for ``tom@example.com``:

::

    sudo so-user delete tom@example.com

TheHive
-------
Log into :ref:`hive` and then click ``Admin`` and ``Users`` to access the User management screen. Then click the ``Lock`` button for the user account you want to disable.
