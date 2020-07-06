.. _nids:

NIDS
====

NIDS stands for Network Intrusion Detection System. It is a means of monitoring network traffic, looking for specific activity, and generating alerts.

Usage
-----

Security Onion 2.0 runs `<Suricata>`__ as its Network Intrusion Detection System (NIDS). 

Performance
-----------

`<Suricata>`__ leverages `<AF-PACKET>`_ for higher performance.

Analysis
--------

You can analyze NIDS alerts from Suricata via:

-  `Kibana <Kibana>`__
-  Hunt
-  TheHive

NIPS
----

Security Onion is designed to be passive and so Suricata runs in NIDS mode rather than NIPS (inline) mode.  Running in NIPS mode would require manual configuration and we do not recommend or support it.

More Information
----------------

- For more information about Suricata, please see the `<Suricata>`__ section.
