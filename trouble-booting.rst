.. _trouble-booting:

Booting Issues
==============

If you have trouble booting an ISO image, here are some troubleshooting steps:

-  Verify the downloaded ISO image using hashes or GPG key.
-  Verify that your machine is x86-64 architecture (standard Intel or AMD 64-bit).
-  If you're trying to run a 64-bit VM, verify that your 64-bit processor supports virtualization and that virtualization is enabled in the BIOS.
-  If you think your machine does support 64-bit, but you're still having problems with our 64-bit ISO image, try downloading the standard Ubuntu 18.04 64-bit ISO image or CentOS 7 64-bit ISO image and seeing if they run. If they don't, then you should double-check your 64-bit compatibility.
-  | If all else fails but standard CentOS 7 64-bit or Ubuntu 18.04 64-bit installs normally, then you can always install our components on top of them as described on the :ref:`installation` page.
