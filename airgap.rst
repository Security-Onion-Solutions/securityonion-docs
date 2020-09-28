.. _airgap:

Airgapped Networks
==================

Security Onion is commited to allowing users to run a full install on networks that do not have Internet access. Starting in 2.x RC3, users will see an option to specify that the install is airgapped. The installer will then make the appropriate modifications to make this work properly.

Key Differences
---------------

By selecting ``Airgap`` as an install option, a couple of things happen that are different than a normal install with Internet access. First, all CentOS repos are removed and replaced with a new repo that runs on the manager. During the install, all of the necessary RPMs are copied from the ISO to a new repo located in ``/nsm/repo/``. All devices in the grid will now use this repo for updates to packages. Another difference is the latest ET Open rules from Emerging Threats are copied to ``/nsm/repo/rules/`` so that the manager can access them. This allows users to use the standard SO process for managing SIDS etc. Finally, yara rules for :ref:`strelka` are copied to ``/nsm/repo/rules/strelka/`` so that :ref:`strelka` has the latest and greatest rules for static file analysis.

Updating
--------

.. note::

   If upgrading from RC3 there is an extra step that needs to take place to copy over the proper version of soup in order to complete the update. To accomplish this you need to run the following commands:
   - mkdir -p /tmp/sotemp
   If using a DVD with the image burned to it:
   - mount /dev/cdrom /tmp/sotemp
   If using an ISO file:
   - mount -t iso9660 -o loop /home/user/securityonion-2.3.0.iso /tmp/sotemp
   - cp /tmp/sotemp/SecurityOnion/salt/common/tools/sbin/soup /opt/so/saltstack/default/salt/common/tools/sbin/
   - salt-call state.apply common
   - soup
    
Soup will automatically detect that you are upgrading an airgap install and will ask for the location of the upgrade disk. This can be done by burning the disk and putting it in the DVD drive, burning a USB stick like any standard ISO, or simply just copying the ISO file to the airgapped manager. 
