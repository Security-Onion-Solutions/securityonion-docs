ISO Release Notes
=================

-  | As always, make sure you verify the downloaded ISO image:
   | https://github.com/Security-Onion-Solutions/security-onion/blob/master/Verify_ISO.md   
-  When the ISO boots, choose the default boot menu option.

-  Once the live desktop appears, double-click the ``Install SecurityOnion`` icon.

-  On the "Installation type" screen, you may want to select the ``Use LVM`` option, as this will automatically create a ``/boot`` partition at the beginning of the drive and will give you more flexibility later. Check to see if the installer allocates a large amount of space to ``/home``. If this is the case, you may want to shrink ``/home`` to give more space to ``/``.

-  If prompted with an encrypt home folder or encrypt partition option, DO NOT enable this feature.

-  If asked about automatic updates, DO NOT enable automatic updates.

-  The Keyboard Layout screen may be larger than your screen resolution and so the Continue button may be off the screen to the right as shown at https://launchpadlibrarian.net/207213663/Screenshot_wilyi386deskmanual_2015-05-22_13%3A05%3A41.png.  You can simply slide the window over until you see the Continue button. For more information, please see https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/1458039.

-  Once the installer completes, it should prompt to remove installation media and press ENTER. If instead it appears to hang, simply press the ENTER key to reboot. If that doesn't work, you may forcibly restart the machine.

-  Once you've logged into your newly installed Security Onion, you'll notice that there is only a Setup icon on the desktop. Other icons will be created when you complete both phases of Setup. So you'll run Setup, configure your network interfaces, reboot, run Setup again to configure services, and then you'll see desktop icons for user interfaces.

-  Setup now defaults to enabling the Elastic Stack. We recommend a BARE MINIMUM of 4 CPU cores and 8GB RAM.

-  When choosing Evaluation Mode, the following services are enabled by default: `<Snort>`_, `<Bro>`_, `<netsniff-ng>`_, pcap_agent, snort_agent, barnyard2.

-  When choosing Production Mode, you then have the option of Best Practices or Custom. Best Practices asks a smaller number of questions and chooses the services that most folks want (`<Snort>`_ or `<Suricata>`_, `<Bro>`_, `<netsniff-ng>`_, pcap_agent, snort_agent, barnyard2, `<salt>`_). Custom gives you more control over your system but requires more in-depth knowledge about services and their functions.

-  Once you've completed both phases of Setup, you should see new icons on your Desktop.

-  For more information, please refer to the full `Installation <Installation>`__ guide and other documentation.
