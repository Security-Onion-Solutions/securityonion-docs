.. _tuning:

Tuning
======

To get the best performance out of Security Onion, you'll want to tune it for your environment.  Start by creating Berkeley Packet Filters (BPFs) to ignore any traffic that you don't want your network sensors to process.  Then tune your IDS rulesets. There may be entire categories of rules that you want to disable first and then look at the remaining enabled rules to see if there are individual rules that can be disabled.   Once your rules and alerts are under control, then check to see if you have packet loss.  If so, then tune the number of AF-PACKET workers for sniffing processes.  If you are on a large network, you may need to do additional tuning like pinning processes to CPU cores.  More information on each of these topics can be found in this section.

.. toctree::
   :maxdepth: 2
   
   bpf
   rules
   local-rules
   alerts
   af-packet
   performance
