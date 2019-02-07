Managing Rules
==============

| Rulesets are chosen during setup and are specified in
  ``/etc/nsm/pulledpork/pulledpork.conf``.
| If you change the the configuration in ``pulledpork.conf``, then you
  will need to run ``rule-update`` (if in a server/sensor deployment,
  run ``rule-update`` on the master first, then the sensor, or wait for
  it to be replicated).

Options
-------

Security Onion offers the following choices for rulesets to be used by
Snort/Suricata:

-  **ET Open**

   -  optimized for Suricata, but available for Snort as well
   -  **free**

   | For more information, see:
   | https://rules.emergingthreats.net/open/

-  **ET Pro** (Proofpoint)

   -  optimized for Suricata, but available for Snort as well
   -  rules retrievable as released
   -  license fee per sensor

   For more information, see:
   https://www.proofpoint.com/us/threat-insight/et-pro-ruleset
-  **Snort Community**

   -  optimized for Snort
   -  community-contributed rules
   -  **free**

   | For more information, see:
   | https://www.snort.org/downloads/#rule-downloads
   | https://www.snort.org/faq/what-are-community-rules

-  **Snort Registered**

   -  optimized for Snort
   -  Snort SO (Shared Object) rules will only work with Snort
   -  same rules as Snort Subscriber ruleset, except rules only
      retrievable after 30 days past release
   -  **free**

   | For more information, see:
   | https://www.snort.org/downloads/#rule-downloads
   | https://snort.org/documents/registered-vs-subscriber

-  **Snort Subscriber** (Talos)

   -  optimized for Snort
   -  Snort SO (Shared Object) rules will only work with Snort
   -  rules retrievable as released
   -  license fee per sensor

   | For more information, see:
   | https://www.snort.org/downloads/#rule-downloads
   | https://snort.org/documents/registered-vs-subscriber
