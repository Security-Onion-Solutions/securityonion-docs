.. _airgap:

Airgap
======

Security Onion is committed to allowing users to run a full install on networks that do not have Internet access. Our ISO image includes everything you need to run without Internet access. Make sure that you choose the airgap option during Setup. 

If your network has Internet access but has overly restrictive proxies, firewalls, or other network devices, then you may want to consider the airgap option as everything will install via the ISO image.

.. image:: images/06_setup_airgap.png
  :target: _images/06_setup_airgap.png

Airgap mode works as follows:

- During the install, all of the necessary RPM packages are copied from the ISO image to a new repo located in ``/nsm/repo/``. All devices in the grid will now use this repo for updates to packages.

- :ref:`nids` rules for :ref:`suricata` are copied to ``/nsm/rules/suricata``.

- :ref:`yara` rules for :ref:`strelka` are copied to ``/nsm/rules/yara``.

- :ref:`sigma` rules for :ref:`elastalert` are copied to ``/nsm/repo/rules/sigma``.

- When updating the system, :ref:`soup` will ask for the location of the latest ISO media and will then update using that media rather than pulling from the Internet.

Rule Updates
------------

Our ISO image includes the Emerging Threats (ET) ruleset. When :ref:`soup` updates an airgap system via ISO, it automatically installs the latest ET rules as well. If you would like to switch to a different ruleset like Emerging Threats Pro (ETPRO), then you can manually copy the ETPRO rules to ``/nsm/rules/suricata/emerging-all.rules`` using a command like:

::

  cat /path/to/ETPRO_rules/*.rules > /nsm/rules/suricata/emerging-all.rules
