Account Management
==================

OS root account
---------------

Like other Ubuntu-based distributions, there is no root password. Your default user account has been given sudo permissions. Graphical utilities requesting administrative access should prompt for password; enter your user password. Command-line utilities that require administrative access can be prefixed with ``sudo``. For example, to add an OS user account:

::

    sudo adduser mynewuseraccount

For more details, use the OS command `man adduser`.


Security Onion Account Management
---------------------------------

Accounts used for the management and access of SO functionality through the different applications and web interfaces are managed through the command line interface with the following commands:

1. so-user-add
2. so-user-disable
3. so-user-list
4. so-user-passwd


so-user-add
-----------

You can add accounts as follows:

::

    sudo so-user-add

You will then be prompted for a user name and password.  su-user-add will automatically create an account for Sguil/Squert/Kibana.

so-user-disable
---------------

This command will disable an account, therefore preventing it from authenticating against Sguil/Squert/Kibana.

::

    sudo so-user-disable


**NOTE:**  Once disabled, there is no way to re-enable an account at this time.

so-user-list
------------

This command will display a list of active accounts which are able to authenticate against Sguil/Squert/Kibana.  Accounts that have been disabled will not be listed.

::

    sudo so-user-list


so-user-passwd
--------------

This command will allow you to change the password of accounts that were created with the so-user-add command.

::

    sudo so-user-add



Sguil
-----

Log into Sguil using the username and password you created in the Setup wizard.  As well, you can create create additional accounts by using the so-user-add command.

You can change passwords using the Sguil client (``File`` --> ``Change Password``) or as follows:

Squert
------

Squert authenticates against the Sguil user database, so you should be able to login to Squert using the same username and password you use to login to Sguil.

Kibana
------

When you access Kibana, you are prompted to login using Apache Single Sign On (SSO). This SSO authenticates against the Sguil user database, so you should be able to login to Kibana using the same username and password you use to login to Sguil.

MySQL
-----

The MySQL root password is randomized. MySQL only allows connections from localhost. If you need to look at the database manually, you can do so like this:

::

    sudo mysql --defaults-file=/etc/mysql/debian.cnf

