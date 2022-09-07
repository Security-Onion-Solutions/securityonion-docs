.. _so-elastic-auth:

so-elastic-auth
===============

Security Onion supports Elastic authentication. This means that you will authenticate to :ref:`elasticsearch` and :ref:`kibana` using the same username and password that you use for :ref:`soc`. 

Please note that if you add a new user directly in :ref:`kibana` via the Kibana Users page, then that new user will only have access to :ref:`kibana` and no other apps. If you want the user to have access to all apps, make sure you add the user as shown in the :ref:`adding-accounts` section.

Service Accounts
----------------

Service accounts use randomly generated passwords that are 72 characters in length. If you need to reset these passwords, you can use the ``so-elastic-auth-password-reset`` utility.
