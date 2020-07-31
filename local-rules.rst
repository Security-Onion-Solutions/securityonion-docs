.. _local-rules:

Adding Local Rules
==================

-  You can add rules in the ``/opt/so/saltstack/local/salt/idstools/localrules/`` directory on your manager. If you have existing rules files, you can copy them to this directory. Otherwise, just create a new file in this directory.
   
-  Let's add a simple rule that's really just a copy of the traditional ``id check returned root`` rule:

   ::

       alert ip any any -> any any (msg:"GPL ATTACK_RESPONSE id check returned root 2"; content:"uid=0|28|root|29|"; classtype:bad-unknown; sid:7000000; rev:1;)
       
-  Run ``salt-call state.highstate`` to merge ``/opt/so/saltstack/local/salt/idstools/localrules/`` into ``/opt/so/rules/nids/local.rules`` and restart processes as necessary:

   ::

       sudo salt-call state.highstate

-  If you built the rule correctly, then Suricata should be back up and running.

- You can then run ``curl testmyids.com`` to generate traffic which should cause this rule to alert (and the original rule that it was copied from, if it is enabled).
