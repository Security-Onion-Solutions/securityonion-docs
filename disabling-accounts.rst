.. _disabling-accounts:

Disabling Accounts
==================

OS
--

If you need to disable an OS user account, you can expire the account using ``usermod --expiredate 1``.  For example, to disable the account for user ``tom``:

::

    sudo usermod --expiredate 1 tom

For more information, please see ``man passwd`` and ``man usermod``.

SOC & TheHive & Fleet - CLI
---------------------------

If you need to disable an account in :ref:`soc`, :ref:`hive`, and :ref:`fleet`, you can use the ``so-user-diasable`` command and specify the user's email address. For example, to disable the account for ``tom@example.com``:

::

    sudo so-user-disable tom@example.com

After disabling a user account, the :ref:`soc` :ref:`administration` page will show the disabled user account with a lock icon in the Status column:

.. image:: images/users.png
  :target: _images/users.png

TheHive - UI
------------

Log into :ref:`hive` and then click ``Admin`` and ``Users`` to access the User management screen. Then click the ``Lock`` button for the user account you want to disable.
