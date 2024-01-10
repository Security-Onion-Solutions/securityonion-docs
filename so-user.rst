.. _so-user:

so-user
=======

:ref:`soc` user management should normally be done via :ref:`administration` as shown in the :ref:`accounts` section. However, if for some reason you can't log into SOC, you can use ``so-user`` from the command line to manage SOC user accounts.

``so-user`` has many different operations. You can see them all by running ``so-user`` with no options:

::

        sudo so-user

Listing SOC Users
-----------------

To see a list of all SOC users, use the ``list`` operation:

::

        sudo so-user list

Changing SOC User Password
--------------------------

If you've forgotten your password, you can reset it using the ``password`` operation:

::

        sudo so-user password --email onionuser@example.com

Once you've reset your password, you should be able to log into SOC and go back to managing user accounts via :ref:`administration` as shown in the :ref:`accounts` section.
