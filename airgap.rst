.. _airgap:

Airgap
======

Security Onion is committed to allowing users to run a full install on networks that do not have Internet access. Setup will ask if you want to configure the installation for airgap and will then make the appropriate modifications to make this work properly. Please note that the airgap option is intended to be consistent across your deployment, so if you are on an airgap network you should choose the airgap option when installing the manager and all nodes.

Key Differences
---------------

By selecting ``Airgap`` as an install option, a couple of things happen that are different than a normal install with Internet access. First, all CentOS repos are removed and replaced with a new repo that runs on the manager. During the install, all of the necessary RPMs are copied from the ISO to a new repo located in ``/nsm/repo/``. All devices in the grid will now use this repo for updates to packages. Another difference is the latest ET Open rules from Emerging Threats are copied to ``/nsm/repo/rules/`` so that the manager can access them. This allows users to use the standard SO process for managing SIDS etc. Finally, yara rules for :ref:`strelka` are copied to ``/nsm/repo/rules/strelka/`` so that :ref:`strelka` has the latest and greatest rules for static file analysis.
