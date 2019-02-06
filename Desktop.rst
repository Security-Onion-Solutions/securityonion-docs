Disabling
=========

| If you are running a production deployment and don't need the desktop
  environment, you can disable the GUI altogether and boot in text mode:
| http://askubuntu.com/questions/16371/how-do-i-disable-x-at-boot-time-so-that-the-system-boots-in-text-mode

Support
=======

If you need to keep running the desktop environment and you're running
XFCE, LXDE, or another desktop environment that is on the 3-year support
cycle, you will most likely want to switch to a fully supported desktop
environment until we're ready to move off of Ubuntu 14.04. We've
prepared a package to make it easy to switch to Gnome Flashback (a
lightweight environment similar to XFCE or LXDE).

Installing Gnome Flashback
==========================

Install the new ``securityonion-desktop-gnome`` package:

::

    sudo apt update && sudo apt install securityonion-desktop-gnome

Converting to Gnome Flashback
=============================

After installing the ``securityonion-desktop-gnome`` package, you can
now run the ``so-desktop-gnome`` script:

::

    sudo so-desktop-gnome

The script will notify you that it is about to remove all XFCE packages
and install Gnome Flashback. Press Enter to continue. When the script is
finished, review all output for any error messages and then press Enter
to reboot.

Resolution
==========

Once you've rebooted and logged into the new Gnome Flashback session,
you may want to change your display resolution:

-  Click ``Applications`` → ``System Tools`` → ``Preferences`` →
   ``Displays``
-  Click the ``Resolution`` drop-down box and set your desired
   resolution
-  If you don't see the ``Apply`` button, press ``Alt-F7`` and then use
   your arrow keys to move the window until ``Apply`` is visible, then
   press Enter
-  Click the ``Apply`` button
