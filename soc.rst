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
