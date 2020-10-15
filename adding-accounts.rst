.. _adding-accounts:

Adding Accounts
===============

OS
--

If you need to add a new OS user account, you can use the ``adduser`` command.  For example, to add a new account called ``tom``:

::

    sudo adduser tom

For more information, please see ``man adduser``.

SOC & TheHive & Fleet - CLI
---------------------------

If you need to add a new account to :ref:`soc`, :ref:`hive`, and :ref:`fleet` you can use the ``so-user-add`` command and specify the user's email address. For example, to add a new account for ``tom@example.com``:

::

    sudo so-user-add tom@example.com

TheHive - UI
------------

If you need to add a new :ref:`hive` account, log into :ref:`hive` with your existing account and then click ``Admin`` and ``Users`` to access the ``User management`` screen. Then click the ``Add user`` button and follow the prompts. Once the user has been created, you can then set their password.
