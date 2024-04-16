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

.. image:: images/config-item-idstools.png
  :target: _images/config-item-idstools.png

Rulesets
--------

Security Onion offers the following choices for rulesets to be used by :ref:`suricata`.

ET Open
-------

-  optimized for :ref:`suricata`
-  **free**

| For more information, see:
| https://rules.emergingthreats.net/open/

ET Pro (Proofpoint)
-------------------

-  optimized for :ref:`suricata`
-  rules retrievable as released
-  license fee per sensor (you are responsible for purchasing enough licenses for your entire deployment)

| For more information, see:
| https://www.proofpoint.com/us/threat-insight/et-pro-ruleset  

Snort Community
---------------

-  NOT optimized for :ref:`suricata`
-  community-contributed rules
-  **free**

| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://www.snort.org/faq/what-are-community-rules

Snort Registered
----------------

-  NOT optimized for :ref:`suricata`
-  Snort SO (Shared Object) rules do NOT work with :ref:`suricata`
-  same rules as Snort Subscriber ruleset, except rules only retrievable after 30 days past release
-  **free**

Since Shared Object rules won't work with :ref:`suricata`, you may want to disable them using a regex like ``'re:soid [0-9]+'`` as described in the :ref:`managing-alerts` section.
  
| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://snort.org/documents/registered-vs-subscriber

Snort Subscriber (Talos)
------------------------

-  NOT optimized for :ref:`suricata`
-  Snort SO (Shared Object) rules do NOT work with :ref:`suricata`
-  rules retrievable as released
-  license fee per sensor (you are responsible for purchasing enough licenses for your entire deployment)

Since Shared Object rules won't work with :ref:`suricata`, you may want to disable them using a regex like ``'re:soid [0-9]+'`` as described in the :ref:`managing-alerts` section.

| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://snort.org/documents/registered-vs-subscriber

Git Repository
------------------------

You can add your custom url rules download by going to :ref:`administration` --> Configuration --> idstools --> config --> urls


| Add your custom git RAW url in ``'["URL"]'``. (URL should be written as Python list ex: ["https://raw.github.com/test/nids.rules"])
| With the next so-idstools-restart  rules will be added into all.rules [/opt/so/rules/nids/suri/all.rules]

Other
-----

- not officially managed/supported by Security Onion
- license fee may or may not apply
