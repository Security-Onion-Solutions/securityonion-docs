.. _soc:

Security Onion Console (SOC)
============================

Once you have run ``so-allow`` and allowed your IP address, you can then connect to Security Onion Console (SOC) with your web browser. We recommend chromium or chromium-based browsers such as Google Chrome. Other browsers may work, but chromium-based browsers provide the best compatibility.

SOC gives you access to a variety of tools and they all complement each other very well. For example, here's one potential workflow:

 - Open :ref:`hive` and review NIDS alerts from :ref:`suricata`.
 - Once you've found a NIDS alert that you want to investigate, you might want to expand your search and look for additional logs relating to the source and destination IP addresses, so pivot to :ref:`kibana` or :ref:`hunt` for more information from :ref:`zeek` or perhaps :ref:`sysmon` logs.
 - Return to :ref:`hive` and document any indicators of compromise (IOCs) found thus far.
 - Go to :ref:`fleet` and perform a wider search for those IOCs across all :ref:`osquery` endpoints.
 - Use :ref:`cyberchef` to further analyze and decode additional host artifacts.
 - Develop a play in :ref:`playbook` that will automatically alert on IOCs moving forward.
 - Finally, return to :ref:`hive` and document the entire investigation and close the case.
 
.. toctree::
   :maxdepth: 2

   hunt
   kibana
   grafana
   cyberchef
   playbook
   fleet
   hive
   attack-navigator
