.. _email:

Email Configuration
===================

Some applications rely on having a mail server in the OS itself and other applications (like Wazuh) have their own mail configuration and so they don't rely on a mail server in the OS itself.

Operating System
----------------

Install and configure your favorite mail server. Depending on your needs, this could be something simple like ``nullmailer``  (recommended) or something more complex like ``exim4``.

Here are some ``nullmailer`` instructions provided by Michael Iverson:

::

   sudo apt-get install nullmailer

   # edit /etc/mailname to hold your "from" domain name. (If you were google, you'd use "gmail.com".)

   # edit /etc/nullmailer/adminaddr to contain the address you want mail to root to be routed to.

   # edit /etc/nullmailer/remotes to contain the mail server to forward email to. 

Alternatively, here are some instructions for the more complex ``exim4``:

::

   sudo apt-get -y install mailutils
   sudo dpkg-reconfigure exim4-config

Once you've configured your mail server and verified that it can send email properly, you might want to create a daily cronjob to execute ``/usr/sbin/sostat`` and email you the output:

::

   # /etc/cron.d/sostat
   crontab entry to run sostat and email its output
   ------------------------------------------------
   SHELL=/bin/sh
   PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
   EMAIL=YourUsername@YourDomain.com\ 
   01 12 * * * root HOSTNAME=$(hostname); /usr/sbin/sostat 2>&1 | mail -s "$HOSTNAME stats" $EMAIL

If you don't already have the ``mail`` utility, you can try installing:

::

   sudo apt-get install mailutils

Wazuh
-----

Modify ``/opt/so/wazuh/etc/ossec.conf`` as follows:

::

   <global>
   <email_notification>yes</email_notification>
   <email_to>YourUsername@YourDomain.com</email_to> 
   <smtp_server>YourMailRelay.YourDomain.com</smtp_server>
   <email_from>ossec@YourDomain.com</email_from> 
   <email_maxperhour>100</email_maxperhour>
   </global>

Then restart Wazuh:

::

   sudo so-wazuh-restart

You can specify the severity of an event for which Wazuh will send email alerts by specifying an appropriate value for ``email_alert_level`` in ``/opt/so/wazuh/etc/ossec.conf``. If you notice ``email_alert_level`` is not being respected for a certain rule, it may be that the option is overridden by ``<options>alert_by_email</options>`` being set for a rule. You can modify this behavior in ``/opt/so/wazuh/etc/rules/local_rules.xml``.

You can also find an explanation of the alert levels at http://ossec-docs.readthedocs.io/en/latest/manual/rules-decoders/rule-levels.html.

Zeek
----

Edit ``/opt/so/conf/zeek/zeekctl.cfg`` and set the following:

::

   MailTo = YourUsername@YourDomain.com
   sendmail = /usr/sbin/sendmail

Then update and restart Zeek:

::

   sudo so-zeek-restart

You should then start receiving hourly connection summary emails. If you don't want the connection summary emails, you can add the following to ``zeekctl.cfg`` and update and restart Zeek as shown above:

::

   tracesummary=

You may want to receive emails for Zeek notices. To do that, add the following to ``/opt/so/conf/zeek/local.zeek`` and then update/restart Zeek as shown above:

::

   hook Notice::policy(n: Notice::Info)
   {
   add n$actions[Notice::ACTION\_ALARM];
   }

Also see http://mailman.icsi.berkeley.edu/pipermail/bro/2013-December/006418.html.

Elastalert
----------

Follow the steps on the `Elastalert <ElastAlert#email---internal>`__ page.

Lack of network traffic
-----------------------

If you configured Zeek as shown above, they should automatically email you if your network sensors stop seeing traffic.  
