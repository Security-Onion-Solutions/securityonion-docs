Managing Rules
==============

NIDS rulesets are chosen during setup and are specified in ``/etc/nsm/pulledpork/pulledpork.conf``. If you change the configuration in ``/etc/nsm/pulledpork``, then you will need to update your rules as shown in the following section.

Updating Rules
--------------

To update your rules, run ``rule-update`` on your master server:

::

  sudo rule-update
  
If you have a distributed deployment with salt enabled and you run ``rule-update`` on your master server, then those new rules will automatically replicate from the master to your sensors within 15 minutes.  If you don't want to wait 15 minutes, you can force the sensors to update immediately by running the following command on your master server:

::

  sudo salt '*' state.highstate
  
If you have a distributed deployment with salt disabled and you run ``rule-update`` on your master server, then those new rules will replicate from the master to your sensors during the daily cron job.  If you don't want to wait for that daily cron job, you can force an immediate update on the sensor by logging into the sensor and running:

::

  sudo rule-update

Rulesets
--------

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
