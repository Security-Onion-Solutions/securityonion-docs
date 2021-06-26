.. _so-elastic-auth:

so-elastic-auth
===============

Starting in Security Onion 2.3.60, we will support Elastic authentication. This means that you will authenticate to :ref:`elasticsearch` and :ref:`kibana` using the same username and password that you use for :ref:`soc`. 

New Installations
-----------------

New installations of Security Onion 2.3.60 and later will automatically enable Elastic auth. If for some reason you want to disable Elastic auth, you can do so as shown in the Disabling section below.

Existing Installations
----------------------

If you have an older installation that you've upgraded to Security Onion 2.3.60 or later and would like to enable Elastic auth, you can do so as shown in the Enabling section below. After manually enabling Elastic auth, each :ref:`soc` user will need to reset their password inside of :ref:`soc` and this will update their username and password in Elastic.

Usage
-----

::

   so-elastic-auth <true|false>

Enabling
--------

To enable Elastic auth, run ``so-elastic-auth`` with the ``true`` option:

::

   so-elastic-auth true
   
Disabling
---------

To disable Elastic auth, run ``so-elastic-auth`` with the ``false`` option:

::

   so-elastic-auth false
