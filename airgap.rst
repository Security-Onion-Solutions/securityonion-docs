.. _airgap:

Airgap
======

Security Onion is committed to allowing users to run a full install on networks that do not have Internet access. You will need to use our Security Onion ISO image as it includes everything you need to run without Internet access. Setup will ask if you want to configure the installation for airgap and will then make the appropriate modifications to make this work properly. 

Here's how airgap mode works:

- During the install, all of the necessary RPM packages are copied from the ISO image to a new repo located in ``/nsm/repo/``. All devices in the grid will now use this repo for updates to packages.

- Rules are copied to ``/nsm/repo/rules/``. This includes NIDS rules, Yara rules for :ref:`strelka`, and Sigma rules for :ref:`playbook`.

- When updating the system, :ref:`soup` will ask for the location of the latest ISO media and will then update using that media rather than pulling from the Internet.

Rule Updates
------------

The Security Onion ISO image includes the Emerging Threats (ET) ruleset. When :ref:`soup` updates an airgap system via ISO, it automatically installs the latest ET rules as well. If you would like to switch to a different ruleset like Emerging Threats Pro (ETPRO), then you can manually copy the ETPRO rules to ``/nsm/repo/rules/emerging-all.rules`` using a command like:

::

  cat /path/to/ETPRO_rules/*.rules > /nsm/repo/rules/emerging-all.rules
