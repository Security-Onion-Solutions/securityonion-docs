Tuning
======

To get the best performance out of Security Onion, you'll want to tune it for your environment.  Start by creating Berkeley Packet Filters (BPFs) to ignore any traffic that you don't want your network sensors to process.  Then tune your rulesets using PulledPork's ``disablesid.conf`` and ``modifysid.conf``.  There may be entire categories of rules that you want to disable first and then look at the remaining enabled rules to see if there are individual rules that can be disabled.  Once your ruleset is a manageable size, then look at tuning your alerts via Sguil's autocat feature.  Once your rules and alerts are under control, then look at sostat to see if you have packet loss.  If so, then tune using PF_RING or AF-PACKET.  If you are on a large network, you may need to do additional tuning like pinning processes to CPU cores.  More information on each of these topics can be found in this section.

.. toctree::
   :maxdepth: 2
   
   bpf
   rules
   local-rules
   alerts
   pf-ring
   af-packet
   performance
   MySQLTuning
   Trimming-PCAPs
   DisablingProcesses
