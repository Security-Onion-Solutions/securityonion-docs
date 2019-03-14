Passwords
=========

OS root account
---------------

Like other Ubuntu-based distributions, there is no root password. Your default user account has been given sudo permissions. Graphical utilities requesting administrative access should prompt for password; enter your user password. Command-line utilities that require administrative access can be prefixed with ``sudo``. For example, to add an OS user account:

::

    sudo adduser mynewuseraccount

Sguil
-----

Log into Sguil using the username/password you created in the Setup wizard.

You can add accounts as follows (please note that Sguil usernames must be alphanumeric):

::

    sudo so-user-add

You can change passwords using the Sguil client (``File`` --> ``Change Password``) or as follows:

::

    sudo so-user-passwd

You can disable accounts as follows:

::

    sudo so-user-disable

Squert
------

Squert authenticates against the Sguil user database, so you should be able to login to Squert using the same username/password you use to login to Sguil.

Kibana
------

When you access Kibana, you are prompted to login using Apache Single Sign On (SSO). This SSO authenticates against the Sguil user database, so you should be able to login to Kibana using the same username/password you use to login to Sguil.

MySQL
-----

The MySQL root password is randomized. MySQL only allows connections from localhost. If you need to look at the database manually, you can do so like this:

::

    sudo mysql --defaults-file=/etc/mysql/debian.cnf

