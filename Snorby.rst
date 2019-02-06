-  | Snorby is now considered un-maintained and is no longer included in
     Security Onion as of Security Onion 14.04. If you are still using
     the old Security Onion 12.04 that includes Snorby, you should plan
     on upgrading to Security Onion 14.04 as soon as possible:
   | https://github.com/Security-Onion-Solutions/security-onion/wiki/Upgrading-from-12.04-to-14.04
   | https://github.com/Security-Onion-Solutions/security-onion/wiki/Installation

-  | Originally developed by Dustin Webber:
   | https://github.com/snorby/snorby

-  Web 2.0, Ajax, Ruby-on-Rails

-  Log into Snorby using the EMAIL ADDRESS and password you specified in
   Setup

-  Snorby has its own MySQL database (separate from the Sguil and ELSA
   databases)

-  The Snorby database only stores NIDS alerts from Snort or Suricata

-  | Pivot from a NIDS alert in Snorby to CapME to access full packet
     capture:
   | https://github.com/Security-Onion-Solutions/security-onion/wiki/CapMeAuthentication

-  Pivot from an IP address in Snorby to ELSA for related logs (Bro
   logs, OSSEC logs, syslog)

-  | If you need to wipe the Snorby database, please see:
   | https://github.com/Security-Onion-Solutions/security-onion/wiki/WipingSnorby

-  | How do I wipe the Snorby database?
   | `Wipe Snorby <WipingSnorby>`__

-  | Be aware that Snorby uses highcharts. Read the highcharts license
     to determine if you need to purchase a commercial license. If you
     feel that you would be required to purchase a commercial license
     but are unwilling/unable to, you can `disable/remove Snorby
     altogether <DisablingProcesses#disabling-snorby>`__ or de-activate
     HighCharts (the charts on the bottom half of the Snorby Dashboard
     will be blank, but nothing else in Snorby should be affected):
   | sudo mv /opt/snorby/public/javascripts/highcharts.js
     /opt/snorby/public/javascripts/highcharts.js.DISABLED
   | 

-  How do I change the timezone in Snorby?
-  click Settings in the upper right corner
-  click the drop-down box next to "Time zone"
-  select your time zone from the list
-  click the "Update Settings" button
-  | set the same timezone in CapMe's timezone.php:
   | http://blog.securityonion.net/2014/01/new-capme-package-allows-you-to.html

-  | How do I configure Snorby to send emails?
   | Snorby is now considered unmaintained and is being removed from
     Security Onion, but these steps are left here for legacy
     documentation purposes.

Modify Snorby's ``mail_config.rb`` file on the master server as needed
for your mail server:

::

    /opt/snorby/config/initializers/mail_config.rb

Then restart the Snorby delayed\_job process:

::

    sudo pkill -f delayed_job

    sudo su www-data -c "cd /opt/snorby; bundle exec rake snorby:update RAILS_ENV=production"

You can also modify ``/opt/snorby/config/snorby_config.yml`` and change
the ``domain`` setting in the Production section to be the FQDN or IP
address of your Snorby server. However, the resulting link in the email
will still be incorrect since it will be http instead of https and it
will be missing the proper port.
