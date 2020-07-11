.. _passwords:

Passwords
=========

OS user account
---------------

When you first install Security Onion, you go through the standard OS installer and create a user account for yourself.  If you need to change your user password, you can use the ``passwd`` command:

::

    passwd
    
OS root account
---------------

Your default user account should have sudo permissions. Command-line utilities that require administrative access can be prefixed with ``sudo``. For example, the ``so-status`` command requires administrative access so you can run it with ``sudo`` as follows:

::

    sudo so-status

Security Onion Console
----------------------

Log into Security Onion Console using the username and password you created in the Setup wizard.

You can change your password in :ref:`soc` by clicking the user icon in the upper right corner and then clicking ``Settings``:

.. image:: https://user-images.githubusercontent.com/1659467/87231839-768ad500-c388-11ea-885d-6e0c638e63b1.png
