.. _snort:

Snort
=====

Snort is a Network Intrusion Detection System (`<NIDS>`_). It sniffs network traffic and generates IDS alerts.

Previous versions of Security Onion compiled Snort using PF_RING for flow-based load balancing. However, Security Onion 2.0 no longer includes PF_RING and thus no longer includes Snort. Once Snort 3.0 has been released including full support for AF_PACKET flow-based load balancing, we can consider adding Snort 3.0. 

More Information
----------------

For more information about Snort, please see https://snort.org.
