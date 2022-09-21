.. _rules:

Managing Rules
==============

Updating Rules
--------------

Assuming you have Internet access, Security Onion will automatically update your NIDS rules on a daily basis. If you need to manually update your rules, you can run the following on your manager node:

::

  sudo so-rule-update
  
If you have a distributed deployment and you update the rules on your manager node, then those rules will automatically replicate from the manager node to your sensors within 15 minutes.  If you don't want to wait 15 minutes, you can force the sensors to update immediately by running the following command on your manager node:

::

  sudo salt \* state.highstate

Configuration
-------------

You can modify your rule configuration by going to :ref:`administration` --> Configuration --> idstools.

Rulesets
--------

Security Onion offers the following choices for rulesets to be used by :ref:`suricata`.

ET Open
-------

-  optimized for :ref:`suricata`, but available for Snort as well
-  **free**

| For more information, see:
| https://rules.emergingthreats.net/open/

ET Pro (Proofpoint)
-------------------

-  optimized for :ref:`suricata`, but available for Snort as well
-  rules retrievable as released
-  license fee per sensor (users are responsible for purchasing enough licenses for their entire deployment)

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
-  Snort SO (Shared Object) rules only work with Snort not :ref:`suricata`
-  same rules as Snort Subscriber ruleset, except rules only retrievable after 30 days past release
-  **free**

Since Shared Object rules won't work with :ref:`suricata`, you may want to disable them using a regex like ``'re:soid [0-9]+'`` as described in the :ref:`managing-alerts` section.
  
| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://snort.org/documents/registered-vs-subscriber

Snort Subscriber (Talos)
------------------------

-  optimized for Snort
-  Snort SO (Shared Object) rules only work with Snort not :ref:`suricata`
-  rules retrievable as released
-  license fee per sensor (users are responsible for purchasing enough licenses for their entire deployment)

Since Shared Object rules won't work with :ref:`suricata`, you may want to disable them using a regex like ``'re:soid [0-9]+'`` as described in the :ref:`managing-alerts` section.

| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://snort.org/documents/registered-vs-subscriber

Other
-----

- not officially managed/supported by Security Onion
- license fee may or may not apply
