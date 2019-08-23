Passwords
=========

OS user account
---------------

When you first install Security Onion, you go through the standard Ubuntu installer and create a user account for yourself.  If you need to change your user password, you can use the ``passwd`` command:

::

    passwd
    
OS root account
---------------

Like other Ubuntu-based distributions, there is no root password. Your default user account has been given sudo permissions. Graphical utilities requesting administrative access should prompt for password; enter your user password. Command-line utilities that require administrative access can be prefixed with ``sudo``. For example, the ``so-status`` command requires administrative access so you can run it with ``sudo`` as follows:

::

    sudo so-status

Sguil
-----

Log into Sguil using the username and password you created in the Setup wizard.

You can change passwords using the Sguil client (``File`` --> ``Change Password``) or as follows:

::

    sudo so-user-passwd

Squert
------

When you access Squert, you are prompted to login using Apache Single Sign On (SSO). This SSO authenticates against the Sguil user database, so you should be able to login to Squert using the same username and password you use to login to Sguil.

Kibana
------

When you access Kibana, you are prompted to login using Apache Single Sign On (SSO). This SSO authenticates against the Sguil user database, so you should be able to login to Kibana using the same username and password you use to login to Sguil.

If you've enabled Elastic authentication, you can manage user accounts in Kibana under Management -> Users.

MySQL
-----

The MySQL root password is randomized. MySQL only allows connections from localhost. If you need to look at the database manually, you can do so like this:

::

    sudo mysql --defaults-file=/etc/mysql/debian.cnf

