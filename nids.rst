NIDS
====

NIDS stands for Network Intrusion Detection System. It is a means of monitoring network traffic, looking for specific activity, and generating alerts.

Usage
-----

Security Onion can run either `<Snort>`__ or `<Suricata>`__ as its Network Intrusion Detection System (NIDS). When you run Setup and choose Evaluation Mode, it will automatically default to Snort. If you choose Production Mode, you will be asked to choose whether you want to run `<Snort>`__ or `<Suricata>`__.

Performance
-----------

In Security Onion, we compile both `<Snort>`__ and `<Suricata>`__ to support `<PF-RING>`__ for higher performance.  Suricata also supports `<AF-PACKET>`_ as an alternative.  Modern versions of Setup default to running `<Suricata>`_ in `<AF-PACKET>`_ mode.

Analysis
--------

You can analyze NIDS alerts from Snort/Suricata via:

-  `Squert <Squert>`__
-  `Kibana <Kibana>`__
-  `Sguil <Sguil>`__

Switching from Snort to Suricata
--------------------------------

Please note that, if you’re running the Snort Talos ruleset, Snort Shared Object rules will not load in Suricata. Most folks who choose the Suricata engine choose to run the Emerging Threats ruleset.

::

   sudo so-sensor-stop
   sudo sed -i 's|ENGINE=snort|ENGINE=suricata|g' /etc/nsm/securityonion.conf
   sudo rule-update
   sudo so-sensor-start

Switching from Suricata to Snort
--------------------------------

::

   sudo so-sensor-stop
   sudo sed -i 's|ENGINE=suricata|ENGINE=snort|g' /etc/nsm/securityonion.conf
   sudo rule-update
   sudo so-sensor-start

Switching from Snort to Suricata in a salted distributed environment
--------------------------------------------------------------------
From the Master Server, run:
::

   sudo so-sensor-stop
   sudo sed -i 's|ENGINE=snort|ENGINE=suricata|g' /etc/nsm/securityonion.conf
   sudo rule-update
   sudo so-sensor-start
   #The remaining commands assume all sensor hostnames contain "securityonionsensor"
   sudo salt '*securityonionsensor*' cmd.run 'so-sensor-stop'
   sudo salt '*securityonionsensor*' cmd.run 'sed -i "s|ENGINE=snort|ENGINE=suricata|g" /etc/nsm/securityonion.conf'
   sudo salt '*securityonionsensor*' state.highstate
   sudo salt '*securityonionsensor*' cmd.run 'so-sensor-start'   

NIPS
----

Security Onion is designed to be passive and so Snort and Suricata run in NIDS mode rather than NIPS (inline) mode.  Running in NIPS mode would require manual configuration and we do not recommend or support it.

More Information
----------------

- For more information about Snort, please see the `<Snort>`__ section.

- For more information about Suricata, please see the `<Suricata>`__ section.
