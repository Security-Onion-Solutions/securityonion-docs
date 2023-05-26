.. _soc:

Security Onion Console (SOC)
============================

.. image:: images/diagrams/analyst.png
  :target: _images/diagrams/analyst.png

Once all configuration is complete, you can then connect to Security Onion Console (SOC) with your web browser. We recommend chromium-based browsers such as Google Chrome. Other browsers may work, but fully updated chromium-based browsers provide the best compatibility. 

Depending on the options you chose in the installer, connect to the IP address or hostname of your Security Onion installation. Then login using the email address and password that you specified in the installer. 

.. image:: images/login.png
  :target: _images/login.png

Once logged in, you'll notice the user menu in the upper right corner. This allows you to manage your user settings and access documentation and other resources.

.. image:: images/soc-overview.png
  :target: _images/soc-overview.png

On the left side of the page, you'll see links for analyst tools like :ref:`alerts`, :ref:`dashboards`, :ref:`hunt`, :ref:`cases`, :ref:`pcap`, :ref:`kibana`, :ref:`cyberchef`, :ref:`playbook`, and :ref:`attack-navigator`. While :ref:`alerts`, :ref:`dashboards`, :ref:`hunt`, :ref:`cases`, and :ref:`pcap` are built into SOC itself, the remaining tools are external and will spawn separate browser tabs.

If you'd like to customize SOC, please see the :ref:`soc-customization` section. If you'd like to learn more about SOC logs, please see the :ref:`soc-logs` section.

.. toctree::
   :maxdepth: 2

   alerts
   dashboards
   hunt
   cases
   pcap
   grid
   downloads
   administration
   kibana
   elastic-fleet
   osquery-manager
   influxdb
   cyberchef
   playbook
   attack-navigator
