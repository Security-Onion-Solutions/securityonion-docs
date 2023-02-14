.. _trouble-booting:

Booting Issues
==============

If you have trouble booting an ISO image, here are some troubleshooting steps:

-  Verify the downloaded ISO image using hashes or GPG key.
-  Verify that your machine is x86-64 architecture (standard Intel or AMD 64-bit).
-  If you're trying to run a 64-bit virtual machine, verify that your 64-bit processor supports virtualization and that virtualization is enabled in the BIOS.
-  If you’re trying to create a bootable USB from an ISO image, try using Balena Etcher which can be downloaded at https://www.balena.io/etcher/.
-  Certain display adapters may require the ``nomodeset`` option passed to the kernel (see https://unix.stackexchange.com/questions/353896/linux-install-goes-to-blank-screen).
-  If you're still having problems with our 64-bit ISO image, try downloading the standard 64-bit ISO image for CentOS 7 or Ubuntu 20.04. If they don't run, then you should double-check your 64-bit compatibility.

.. tip::

  If all else fails but standard 64-bit CentOS 7 or Ubuntu 20.04 installs normally, then you can always install our components on top of them as described on the :ref:`installation` page.
