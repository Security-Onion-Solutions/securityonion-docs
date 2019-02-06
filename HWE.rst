Introduction
============

HWE stands for Hardware Enablement and is Ubuntu's term for kernel and
graphics driver support. Depending on which HWE stack you're running,
you may need to upgrade it.

Security Onion 14.04 ISO images and HWE stacks
==============================================

If you installed your system using our older Security Onion 14.04 ISO
images (14.04.3.1, 14.04.4.4.1, or 14.04.4.2), then you're running an
interim HWE stack and you'll need to upgrade the HWE stack.

If you installed using our Security Onion 14.04.5.1 (or newer) ISO
image, then it already includes the 16.04 Xenial HWE stack and should
not require any HWE upgrades.

Install updates first
=====================

| Our first step is to install all updates using `soup <Upgrade>`__:
| ``sudo soup``

If soup prompts to reboot, please do so.

Check HWE Status
================

| Now that all updates have been installed, run ``soup`` again to see if
  your HWE stack is supported:
| ``sudo soup``

If it says at the very end ``All updates have been installed``, then no
further action is required and you can ignore the rest of this page. If
you got something other than that, then please continue reading!

Upgrade HWE
===========

| If ``soup`` says
  ``Please upgrade your Hardware Enablement Stack (HWE)``, then you'll
  need to upgrade your HWE stack using the "Ubuntu 14.04 LTS - Trusty
  Tahr" instructions here:
| https://wiki.ubuntu.com/Kernel/LTSEnablementStack

You should then reboot and run ``soup`` again to verify that it now says
``All updates have been installed``.

Example
=======

For example, if you installed your system using our older Security Onion
14.04 ISO images (14.04.3.1, 14.04.4.4.1, or 14.04.4.2), then you're
running an interim HWE stack and you'll need to upgrade the HWE stack as
follows.

#. Run soup to ensure that all updates have been installed:
   ``sudo soup``
#. If soup prompts to reboot, then do so.
#. Run soup again to check the status of your HWE stack:
   ``sudo soup``
#. If soup asks you to upgrade to a new HWE stack, then do the
   following. Please note this command only applies to desktop versions
   of Ubuntu 14.04 (like our Security Onion ISO image) and NOT server
   versions.
   ``sudo apt-get install --install-recommends linux-generic-lts-xenial xserver-xorg-core-lts-xenial xserver-xorg-lts-xenial xserver-xorg-video-all-lts-xenial xserver-xorg-input-all-lts-xenial libwayland-egl1-mesa-lts-xenial``
#. Reboot:
   ``sudo reboot``
#. Run soup again to check HWE status:
   ``sudo soup``
#. It should now say ``All updates have been installed``.

More information
================

For more information, please see:

https://blog.securityonion.net/2016/09/securityonion-sostat-20120722.html

https://lists.ubuntu.com/archives/ubuntu-security-announce/2016-July/003493.html

https://wiki.ubuntu.com/Kernel/LTSEnablementStack
