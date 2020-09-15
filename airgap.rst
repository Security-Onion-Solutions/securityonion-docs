.. _airgap:

Airgapped Networks
==================

Secuirty Onion is commited to allowing users to run a full install on networks that do not have Internet access. Starting in RC3, users will see an option to specify that the install is airgapped. The install will then make the appropriate midifications to the install to make this work properly. 


Key Differences
---------------

By selecting "Airgap" as an install option a couple of things happen that are different than a normal install with Internet access. First you will see that all the CentOS repos are removed and replaced with a new repo that runs on the manager. During the install all of the RPMs needed for an install are copied from the ISO to a new repo located in /nsm/repo. All devices in the grid will now use this repo for updates to packages. Another difference is the latest ET Open rules from emerging threats are copied to /nsm/repo/rules so that the manager can access them. This allows users to use the standard SO process for managing SIDS etc. Finally Strelka yara rules are copied to /nsm/repo/rules/strelka so that strelka has the latest and greatest yara rules for static file analysis.  


Updating
--------

Starting with GA, airgap installs will use soup to update the environment. Soup will be able to automatically detect that it is an airgap install. It will require the user to mount the newest install ISO on the Manager so that soup has access to the files located there. It will copy over all of the latest docker containers, latest OS RPMs, and the latest Security Onion code then perform the upgrade. This will reduce the complexity from pervious versions and help promote frequent updates for airgap installs.


