OS root account
===============

Like other Ubuntu-based distributions, there is no root password. Your
default user account has been given sudo permissions. Graphical
utilities requesting administrative access should prompt for password;
enter your user password. Command-line utilities that require
administrative access can be prefixed with ``sudo``. For example, to add
an OS user account:

::

    sudo adduser mynewuseraccount

Sguil
=====

Log into Sguil using the username/password you created in the Setup
wizard.

You can add accounts as follows (please note that Sguil usernames must
be alphanumeric):

::

    sudo nsm_server_user-add

You can change passwords using the Sguil client (File --> Change
Password) or as follows:

::

    sudo nsm_server_user-passwd

You can disable accounts as follows:

::

    sudo nsm_server_user-disable

Squert
======

Squert authenticates against the Sguil user database, so you should be
able to login to Squert using the same username/password you use to
login to Sguil.

ELSA
====

ELSA authenticates against the Sguil user database, so you should be
able to login to ELSA using the same username/password you use to login
to Sguil.

Kibana
======

When you access Kibana, you are prompted to login using Apache Single
Sign On (SSO). This SSO authenticates against the Sguil user database,
so you should be able to login to Kibana using the same
username/password you use to login to Sguil.

MySQL
=====

The MySQL root password is null to allow the NSMnow administration
scripts to add/delete sensors properly. MySQL only allows connections
from localhost. If you need to look at the database manually, you can do
so like this:

::

    sudo mysql --defaults-file=/etc/mysql/debian.cnf

Xplico
======

| Xplico's default credentials are listed here:
| http://wiki.xplico.org/doku.php?id=interface

| Please note that Xplico is no longer included in Security Onion by
  default and will reach EOL soon:
| https://securityonion.net/wiki/xplico

Snorby
======

| **Please note**: Snorby has been removed in the new Security Onion
  14.04, but this note is left here for legacy documentation purposes.
| Snorby does not authenticate against the Sguil user database. Log into
  Snorby using the EMAIL ADDRESS and password you specified in Setup.

Reset Snorby Password
=====================

To reset your Snorby password, first open the Rails console:

::

    cd /opt/snorby/
    sudo RAILS_ENV=production bundle exec rails c

In the Rails console, reset your Snorby password as follows:

::

    u = User.find_by_email("foo@bar.com")
    u.password="NewUnencryptedPassword123"
    u.password_confirmation="NewUnencryptedPassword123"
    u.save
    quit
