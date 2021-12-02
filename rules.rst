.. _rules:

Managing Rules
==============

Updating Rules
--------------

To update your rules, run ``so-rule-update`` on your manager node:

::

  sudo so-rule-update
  
If you have a distributed deployment and you update the rules on your manager node, then those rules will automatically replicate from the manager node to your sensors within 15 minutes.  If you don't want to wait 15 minutes, you can force the sensors to update immediately by running the following command on your manager node:

::

  sudo salt \* state.highstate

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

To enable the ET Pro ruleset in an already installed grid, modify the ``/opt/so/saltstack/local/pillar/minions/<manager.sls>`` file as follows:

::

  idstools:
    config:
      ruleset: 'ETPRO'
      oinkcode: 'MYOINKCODE'

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
-  license fee per sensor (users are responsible for purchasing enough licenses for their entire deployment)

To enable the Talos Subscriber ruleset in an already installed grid, modify the ``/opt/so/saltstack/local/pillar/minions/<manager.sls>`` file as follows: 

::

  idstools:
    config:
      ruleset: 'TALOS'
      oinkcode: 'MYOINKCODE'

| For more information, see:
| https://www.snort.org/downloads/#rule-downloads
| https://snort.org/documents/registered-vs-subscriber

Other
------------------------

- not officially managed/supported by Security Onion
- license fee may or may not apply

To add other remotely-accessible rulesets, add an entry under ``urls`` for the ruleset URL in ``/opt/so/saltstack/local/pillar/minions/<manager.sls>``:

::

  idstools:
    config:
      ...primary ruelset...
      ...primary ruleset oinkcode...
      urls:
        - https://ruleseturlhere

