.. _email:

Email Configuration
===================

Some applications rely on having a mail server in the OS itself and other applications (like :ref:`wazuh`) have their own mail configuration and so they don't rely on a mail server in the OS itself.

Operating System
----------------

You can install and configure your favorite mail server. Depending on your needs, this could be something simple like ``nullmailer`` or something more complex like ``exim4``.

Elastalert
----------

Follow the steps on the `Elastalert <ElastAlert#email---internal>`__ page.

Wazuh
-----

If you want :ref:`wazuh` to send email, you can modify ``/opt/so/conf/wazuh/ossec.conf`` as follows:

::

   <global>
   <email_notification>yes</email_notification>
   <email_to>YourUsername@YourDomain.com</email_to> 
   <smtp_server>YourMailRelay.YourDomain.com</smtp_server>
   <email_from>ossec@YourDomain.com</email_from> 
   <email_maxperhour>100</email_maxperhour>
   </global>

Then restart :ref:`wazuh`:

::

   sudo so-wazuh-restart

You can specify the severity of an event for which :ref:`wazuh` will send email alerts by specifying an appropriate value for ``email_alert_level`` in ``/opt/so/conf/wazuh/ossec.conf``. If you notice ``email_alert_level`` is not being respected for a certain rule, it may be that the option is overridden by ``<options>alert_by_email</options>`` being set for a rule. You can modify this behavior in ``/opt/so/conf/wazuh/rules/local_rules.xml``.

You can also find an explanation of the alert levels at https://www.ossec.net/docs/manual/rules-decoders/rule-levels.html.
