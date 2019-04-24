Managing Rules
==============

Rulesets are chosen during setup and are specified in ``/etc/nsm/pulledpork/pulledpork.conf``. If you change the configuration in ``pulledpork.conf``, then you will need to run ``rule-update`` on your master server.  If you're running a distributed deployment with separate sensors and you have salt enabled, then those new rules will automatically replicate from the master to your sensors within 15 minutes or you can force an immediate update with ``sudo salt "*" state.highstate``.  If you're running a distributed deployment with salt disabled, then new rules will replicate from the master to the sensors during the daily cron job or you can force an immediate update on the sensor with ``sudo rule-update``.

Security Onion offers the following choices for rulesets to be used by Snort/Suricata.

ET Open
-------

-  optimized for Suricata, but available for Snort as well
-  **free**

| For more information, see:
| https://rules.emergingthreats.net/open/

ET Pro (Proofpoint)
-------------------

-  optimized for Suricata, but available for Snort as well
-  rules retrievable as released
-  license fee per sensor

| For more information, see:
| https://www.proofpoint.com/us/threat-insight/et-pro-ruleset
   
Snort Community
---------------

-  optimized for Snort
-  community-contributed rules
-  **free**

| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://www.snort.org/faq/what-are-community-rules

Snort Registered
----------------

-  optimized for Snort
-  Snort SO (Shared Object) rules will only work with Snort
-  same rules as Snort Subscriber ruleset, except rules only retrievable after 30 days past release
-  **free**

| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://snort.org/documents/registered-vs-subscriber

Snort Subscriber (Talos)
------------------------

-  optimized for Snort
-  Snort SO (Shared Object) rules will only work with Snort
-  rules retrievable as released
-  license fee per sensor

| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://snort.org/documents/registered-vs-subscriber
