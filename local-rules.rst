.. _local-rules:

Adding Local Rules
==================

NIDS
----
You can add NIDS rules in ``/opt/so/saltstack/local/salt/idstools/local.rules`` on your manager. Within 15 minutes, :ref:`salt` should then copy those rules into ``/opt/so/rules/nids/local.rules``. The next run of ``idstools`` should then merge ``/opt/so/rules/nids/local.rules`` into ``/opt/so/rules/nids/all.rules`` which is what :ref:`suricata` reads from. 

If you don't want to wait for these automatic processes, you can run them manually from the manager (replacing ``$SENSORNAME_$ROLE`` as necessary):

  ::

    sudo salt-call state.highstate
    sudo so-rule-update
    sudo salt $SENSORNAME_$ROLE state.apply suricata

For example:
   
-  Let's add a simple rule to ``/opt/so/saltstack/local/salt/idstools/local.rules`` that's really just a copy of the traditional ``id check returned root`` rule:

   ::

       alert ip any any -> any any (msg:"GPL ATTACK_RESPONSE id check returned root 2"; content:"uid=0|28|root|29|"; classtype:bad-unknown; sid:7000000; rev:1;)
       
-  From the manager, tell :ref:`salt` to update:

   ::

       sudo salt-call state.highstate
       
-  Update rules:

   ::
   
       sudo so-rule-update
       
-  Restart Suricata (replacing ``$SENSORNAME_$ROLE`` as necessary):

   ::
   
       sudo salt $SENSORNAME_$ROLE state.apply suricata

-  If you built the rule correctly, then Suricata should be back up and running.

-  You can then run ``curl http://testmynids.org/uid/index.html`` on the node to generate traffic which should cause this rule to alert (and the original rule that it was copied from, if it is enabled).

YARA
----

Default YARA rules are provided from Florian Roth's `signature-base` Github repo at https://github.com/Neo23x0/signature-base.

Local Rules:
~~~~~~~~~~~

To add local YARA rules, create a directory in ``/opt/so/saltstack/local/salt/strelka/rules``, for example ``localrules``.  Inside of ``/opt/so/saltstack/local/salt/strelka/rules/localrules``, add your YARA rules.

After adding your rules, update the configuration by running ``so-strelka-restart``.

Remotely Managed Rules:
~~~~~~~~~~~~~~~~~~~~~~

To have so-yara-update pull YARA rules from a Github repo, copy ``/opt/so/saltstack/local/salt/strelka/rules/``, and modify ``repos.txt`` to include the repo URL (one per line).

Next, run ``so-yara-update`` to pull down the rules.  Finally, run ``so-strelka-restart`` to allow Strelka to pull in the new rules.
