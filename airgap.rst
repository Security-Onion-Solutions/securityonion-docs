.. _airgap:

Airgap
======

Security Onion is committed to allowing users to run a full install on networks that do not have Internet access. You will need to use our Security Onion ISO image as it includes everything you need to run without Internet access. Setup will ask if you want to configure the installation for airgap and will then make the appropriate modifications to make this work properly. Please note that the airgap option is intended to be consistent across your deployment, so if you are on an airgap network you should choose the airgap option when installing the manager and all nodes (recent versions enforce this automatically).

Key Differences
---------------

There are a few differences between an airgap install and a normal install with Internet access:

- All CentOS repos are removed and replaced with a new repo that runs on the manager.

- During the install, all of the necessary RPMs are copied from the ISO to a new repo located in ``/nsm/repo/``. 

- All devices in the grid will now use this repo for updates to packages.

- The latest Emerging Threats (ET) Open rules are copied to ``/nsm/repo/rules/`` so that the manager can access them and users can use the standard Security Onion process for managing NIDS rules. 

- Yara rules are copied to ``/nsm/repo/rules/strelka/`` for :ref:`strelka` file analysis.

- When updating the system, :ref:`soup` will ask for the location of the latest ISO media and will then update using that media rather than pulling from the Internet.

Rule Updates
------------

The Security Onion ISO image includes the Emerging Threats (ET) ruleset. When :ref:`soup` updates an airgap system via ISO, it automatically installs the latest ET rules as well. If you would like to switch to a different ruleset like Emerging Threats Pro (ETPRO), then you can manually copy the ETPRO rules to ``/nsm/repo/rules/emerging-all.rules`` using a command like:

::

  cat /path/to/ETPRO_rules/*.rules > /nsm/repo/rules/emerging-all.rules
