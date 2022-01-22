.. _soc:

Security Onion Console (SOC)
============================

.. image:: images/analyst.png
  :target: _images/analyst.png

Once you've run :ref:`so-allow` and allowed your IP address, you can then connect to Security Onion Console (SOC) with your web browser. We recommend chromium or chromium-based browsers such as Google Chrome. Other browsers may work, but fully updated chromium-based browsers provide the best compatibility. 

Depending on the options you chose in the installer, connect to the IP address or hostname of your Security Onion installation. Then login using the email address and password that you specified in the installer. 

.. image:: images/login.png
  :target: _images/login.png

Once logged in, you'll notice the user menu in the upper right corner.

.. image:: images/soc-user-menu.png
  :target: _images/soc-user-menu.png

On the left side of the page, you'll see links for analyst tools like :ref:`alerts`, :ref:`hunt`, :ref:`cases`, :ref:`pcap`, :ref:`kibana`, :ref:`cyberchef`, :ref:`playbook`, and :ref:`attack-navigator`. While :ref:`alerts`, :ref:`hunt`, :ref:`cases`, and :ref:`pcap` are native to SOC itself, the remaining tools are external and will spawn separate browser tabs.

.. image:: images/soc-tools.png
  :target: _images/soc-tools.png

.. tip::

   SOC gives you access to a variety of tools and they all complement each other very well. For example, here's one potential workflow:

     - Check :ref:`grid` and :ref:`grafana` to make sure your deployment is healthy.
     - Go to the :ref:`alerts` page and review any unacknowledged alerts.
     - Once you've found an alert that you want to investigate, you might want to pivot to :ref:`hunt` to expand your search and look for additional logs relating to the source and destination IP addresses.
     - If any of those alerts or logs look interesting, you might want to pivot to :ref:`pcap` to review the full packet capture for the entire stream.
     - You might want to send that full packet capture to :ref:`cyberchef` for further analysis and decoding.
     - Escalate alerts and logs to :ref:`cases` and document any observables.
     - Go to :ref:`fleet` and perform a wider search for those observables across all :ref:`osquery` endpoints.
     - Develop a play in :ref:`playbook` that will automatically alert on observables moving forward and update your coverage in :ref:`attack-navigator`.
     - Finally, return to :ref:`cases` and document the entire investigation and close the case.
 
.. toctree::
   :maxdepth: 2

   alerts
   hunt
   cases
   pcap
   grid
   downloads
   administration
   kibana
   grafana
   cyberchef
   playbook
   fleet
   hive
   attack-navigator
