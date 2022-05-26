.. _so-elastic-auth:

so-elastic-auth
===============

We support Elastic authentication. This means that you will authenticate to :ref:`elasticsearch` and :ref:`kibana` using the same username and password that you use for :ref:`soc`. 

Please note that if Elastic auth is enabled and you add a new user directly in :ref:`kibana` via the Kibana Users page, then that new user will only have access to :ref:`kibana` and no other apps. If you want the user to have access to all apps, make sure you add the user as shown in the :ref:`adding-accounts` section.

New Installations
-----------------

New installations will automatically enable Elastic auth. If for some reason you want to disable Elastic auth, you can do so as shown in the Disabling section below.

Existing Installations
----------------------

If you have an older installation that you've upgraded to Security Onion 2.3.60 or later and would like to enable Elastic auth, you can do so as shown in the Enabling section below. After manually enabling Elastic auth, each user will need to reset their password inside of :ref:`soc` as shown in the :ref:`passwords` section and this will update their username and password in Elastic.

Usage
-----

::

   so-elastic-auth <true|false>

Enabling
--------

To enable Elastic auth, run ``so-elastic-auth`` with the ``true`` option:

::

   sudo so-elastic-auth true
   
Disabling
---------

To disable Elastic auth, run ``so-elastic-auth`` with the ``false`` option:

::

   sudo so-elastic-auth false

Service Accounts
----------------

Service accounts use randomly generated passwords that are 72 characters in length. If you need to reset these passwords, you can use the ``so-elastic-auth-password-reset`` utility.
