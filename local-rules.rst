.. _local-rules:

Adding Local Rules
==================

You can add rules in ``/opt/so/saltstack/local/salt/idstools/local.rules`` on your manager. Within 15 minutes, :ref:`salt` should then copy those rules into ``/opt/so/rules/nids/local.rules``. The next run of ``idstools`` should then merge ``/opt/so/rules/nids/local.rules`` into ``/opt/so/rules/nids/all.rules`` which is what :ref:`suricata` reads from. If you don't want to wait for these automatic processes, you can run them manually from the manager:

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
       
-  Restart Suricata:

   ::
   
       sudo salt $SENSORNAME_$ROLE state.apply suricata

-  If you built the rule correctly, then Suricata should be back up and running.

-  You can then run ``curl http://testmynids.org/uid/index.html`` on the node to generate traffic which should cause this rule to alert (and the original rule that it was copied from, if it is enabled).
