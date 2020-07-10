.. _soc:

Security Onion Console (SOC)
============================

Once you have run ``so-allow`` and allowed your IP address, you can then connect to Security Onion Console (SOC) and access several different analyst tools that can be used for slicing and dicing data coming from your network and endpoints.

Most of our analyst tools are browser-based. We recommend chromium or chromium-based browsers such as Google Chrome. Other browsers may work, but chromium-based browsers provide the best compatibility.

There are a variety of tools here and they all complement each other very well. For example, here's one potential workflow:

 - open :ref:`hive` and review NIDS alerts from :ref:`suricata`
 - find an interesting alert and pivot from there to :ref:`kibana` or :ref:`hunt` for more information about the connection or the IP addresses involved from :ref:`zeek` and perhaps :ref:`sysmon` logs
 - return to :ref:`hive` and document any indicators of compromise (IOCs) found thus far
 - go to :ref:`fleet` and perform a wider search for those IOCs across all :ref:`osquery` endpoints
 - use :ref:`cyberchef` to further analyze and decode additional host artifacts
 - develop a play in :ref:`playbook` that will automatically alert on IOCs moving forward
 - finally, return to :ref:`hive` and document the entire investigation and close the case

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
