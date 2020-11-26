.. _local-rules:

Adding Local Rules
==================

You can add rules in ``/opt/so/saltstack/local/salt/idstools/local.rules`` on your manager. Within 15 minutes, :ref:`salt` should then merge them into ``/opt/so/rules/nids/all.rules`` and restart processes as necessary. You can force this to happen immediately:

- From the manager:

  ::

    salt $SENSORNAME_$ROLE state.apply suricata

or

- From the node:

  ::

    salt-call state.apply suricata

For example:
   
-  Let's add a simple rule that's really just a copy of the traditional ``id check returned root`` rule:

   ::

       alert ip any any -> any any (msg:"GPL ATTACK_RESPONSE id check returned root 2"; content:"uid=0|28|root|29|"; classtype:bad-unknown; sid:7000000; rev:1;)
       
-  From the manager, tell :ref:`salt` to update:

   ::

       sudo salt $SENSORNAME_$ROLE state.highstate

-  If you built the rule correctly, then Suricata should be back up and running.

-  You can then run ``curl http://testmynids.org/uid/index.html`` on the node to generate traffic which should cause this rule to alert (and the original rule that it was copied from, if it is enabled).
