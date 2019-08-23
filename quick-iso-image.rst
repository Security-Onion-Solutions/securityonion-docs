Quick Evaluation using Security Onion ISO image
===============================================

If you just want to quickly evaluate Security Onion using our ISO image:

#. Review the `Hardware Requirements <Hardware>`__ and `Release Notes <Release-Notes>`__ pages.
#. `Download and verify our Security Onion ISO image <https://github.com/Security-Onion-Solutions/security-onion/blob/master/Verify_ISO.md>`__.
#. Boot the ISO image and choose the default boot menu option.
#. Once the live desktop appears, double-click the ``Install SecurityOnion`` icon.
#. Follow the prompts in the installer. If prompted with an ``encrypt home folder`` or ``encrypt partition`` option, **DO NOT** enable this feature. If asked about automatic updates, **DO NOT** enable automatic updates.
#. Once the installer completes, rebooot into your new installation and login using the username and password you specified during installation.
#. Double-click the Setup icon to run normal Setup.  Alternatively, you can run minimal Setup by opening a terminal (Ctrl-Alt-t) and then typing ``sosetup-minimal`` and pressing Enter. The Setup wizard will walk you through configuring ``/etc/network/interfaces`` and will then reboot.
#. After rebooting, log back in and start Setup the same way you did previously (either double-clicking the icon or running ``sosetup-minimal``). It will detect that you have already configured ``/etc/network/interfaces`` and will walk you through the rest of the configuration. When prompted for ``Evaluation Mode`` or ``Production Mode``, choose ``Evaluation Mode``.
#. Once you've completed the Setup wizard, use the Desktop icons to login to `<Sguil>`_, `<Squert>`_, or `<Kibana>`_.
#. Finally, review the `Post Installation <PostInstallation>`__ page.
