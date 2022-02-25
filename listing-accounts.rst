.. _listing-accounts:

Listing Accounts
================

OS
--

Operating System (OS) user accounts are stored in ``/etc/passwd``.  You can get a list of all OS accounts using the following command:

::

  cut -d: -f1 /etc/passwd
  
If you want a list of user accounts (not service accounts), then you can filter ``/etc/passwd`` for accounts with a UID greater than 999 like this:

::

  cat /etc/passwd | awk -F: '$3 > 999 {print ;}' | cut -d: -f1 
  
SOC
---

To list all :ref:`soc` accounts, you can use the ``so-user`` command with the ``list`` option:

::

    sudo so-user-list

Alternatively, you can get a list of users in :ref:`soc` by clicking ``Administration`` and then ``Users``:

.. image:: images/users.png
  :target: _images/users.png

The Status column will show a different icon depending on the status of the account. In the screenshot above, the first account is disabled, the second account is enabled and has :ref:`mfa` enabled, and the third account is enabled but does not have :ref:`mfa` enabled. Hovering over the icon in the Status column will show you these details as well.
