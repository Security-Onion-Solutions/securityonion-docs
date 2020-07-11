.. _adding-accounts:

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

If you need to add a new Security Onion Console (SOC) account, you can use the ``so-user-add`` command and specify the user's email address. For example, to add a new account for ``tom@example.com``:

::

    sudo so-user-add tom@example.com
