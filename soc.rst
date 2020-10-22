.. _soc:

Security Onion Console (SOC)
============================

Once you've run :ref:`so-allow` and allowed your IP address, you can then connect to Security Onion Console (SOC) with your web browser. We recommend chromium or chromium-based browsers such as Google Chrome. Other browsers may work, but chromium-based browsers provide the best compatibility. 

Depending on the options you chose in the installer, connect to the IP address or hostname of your Security Onion installation. Then login using the email address and password that you specified in the installer. 

.. image:: https://user-images.githubusercontent.com/1659467/92961918-17a41380-f43e-11ea-8e41-668c16b80cbf.png
  :target: https://user-images.githubusercontent.com/1659467/92961918-17a41380-f43e-11ea-8e41-668c16b80cbf.png

Once logged in, you'll see links on the left side for analyst tools like :ref:`alerts`, :ref:`hunt`, :ref:`pcap`, :ref:`kibana`, :ref:`cyberchef`, :ref:`playbook`, :ref:`hive`, and :ref:`attack-navigator`. While :ref:`alerts`, :ref:`hunt`, and :ref:`pcap` are native to SOC itself, the remaining tools are external and will spawn separate browser tabs.

.. image:: images/analyst.png
  :target: _images/analyst.png

.. tip::

   SOC gives you access to a variety of tools and they all complement each other very well. For example, here's one potential workflow:

     - Check :ref:`grafana` to make sure your system is healthy.
     - Go to the :ref:`alerts` page and review unacknowledged alerts.
     - Once you've found an alert that you want to investigate, you might want to expand your search and look for additional logs relating to the source and destination IP addresses, so pivot to :ref:`hunt` for more information. If any of those additional logs look interesting, you might then want to pivot to :ref:`pcap` to look at the full packet capture for that stream.
     - Send alert to :ref:`hive` and document any indicators of compromise (IOCs) found in the previous step.
     - Go to :ref:`fleet` and perform a wider search for those IOCs across all :ref:`osquery` endpoints.
     - Use :ref:`cyberchef` to further analyze and decode additional host artifacts.
     - Develop a play in :ref:`playbook` that will automatically alert on IOCs moving forward and update your coverage in :ref:`attack-navigator`.
     - Finally, return to :ref:`hive` and document the entire investigation and close the case.
 
.. toctree::
   :maxdepth: 2

   alerts
   hunt
   pcap
   kibana
   grafana
   cyberchef
   playbook
   fleet
   hive
   attack-navigator
