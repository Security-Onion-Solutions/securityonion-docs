.. _airgap:

Airgap
======

Security Onion is commited to allowing users to run a full install on networks that do not have Internet access. Setup will ask if you want to configure the installation for airgap and will then make the appropriate modifications to make this work properly.

Key Differences
---------------

By selecting ``Airgap`` as an install option, a couple of things happen that are different than a normal install with Internet access. First, all CentOS repos are removed and replaced with a new repo that runs on the manager. During the install, all of the necessary RPMs are copied from the ISO to a new repo located in ``/nsm/repo/``. All devices in the grid will now use this repo for updates to packages. Another difference is the latest ET Open rules from Emerging Threats are copied to ``/nsm/repo/rules/`` so that the manager can access them. This allows users to use the standard SO process for managing SIDS etc. Finally, yara rules for :ref:`strelka` are copied to ``/nsm/repo/rules/strelka/`` so that :ref:`strelka` has the latest and greatest rules for static file analysis.

Security Onion Version Updates
------------------------------

When you run :ref:`soup` on an airgap install, it will ask for the location of the upgrade disk. You can do one of the following:

- burn the latest ISO image to a DVD and insert it in the DVD drive

- flash the ISO image to a USB drive and insert that USB drive

- simply copy the ISO file itself to the airgapped manager

Starting in Security Onion 2.3.80, you can also specify the path on the command line using the ``-f`` option:

::

	soup -y -f /home/user/securityonion.iso

Security Onion Hotfixes
-----------------------

Hotfix upgrades follow the same process as described in the "Updates" section above.

Updating from RC3
-----------------

.. note::

   If upgrading from RC3 there is an extra step that needs to take place to copy over the proper version of soup in order to complete the update. To accomplish this you need to run the following commands.
  
- Create a temp directory:

   ::

      mkdir -p /tmp/sotemp
   
- If using a DVD with the image burned to it:

   ::

      sudo mount /dev/cdrom /tmp/sotemp
   
   Otherwise, if using an ISO file:

   ::

      sudo mount -t iso9660 -o loop /home/user/securityonion-2.3.0.iso /tmp/sotemp
   
- Copy the new version of :ref:`soup`:

   ::

      sudo cp /tmp/sotemp/SecurityOnion/salt/common/tools/sbin/soup /opt/so/saltstack/default/salt/common/tools/sbin/
   
- Update :ref:`salt`:

   ::

      sudo salt-call state.apply common
   
- Unmount the temp directory:

   ::

      sudo umount /tmp/sotemp
   
- Run the new version of :ref:`soup`

   ::

      sudo soup
