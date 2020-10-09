.. _listing-accounts:

Listing Accounts
================

OS
--

Operating System (OS) user accounts are stored in ``/etc/passwd``.  You can get a list of all OS accounts using the following command:

::

  cut -d: -f1 /etc/passwd
  
If you want a list of user accounts (not service accounts), then you can filter ``/etc/passwd`` for accounts with a UID greater than 1000 like this:

::

  cat /etc/passwd | awk -F: '$3 > 1000 {print ;}' | cut -d: -f1 
  
SOC
---

To list all :ref:`soc` accounts, you can use the ``so-user`` command with the ``list`` option:

::

    sudo so-user list

Alternatively, you can get a list of users in :ref:`soc` by clicking ``Administration`` and then ``Users``:

.. image:: https://user-images.githubusercontent.com/1659467/95574989-ea766100-09fb-11eb-8900-6fc7c48ee59e.png
  :target: https://user-images.githubusercontent.com/1659467/95574989-ea766100-09fb-11eb-8900-6fc7c48ee59e.png

TheHive
-------
To see all :ref:`hive` accounts, log into :ref:`hive` and then click ``Admin`` and ``Users`` to access the User management screen.
