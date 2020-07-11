.. _trouble-booting:

Booting Issues
==============

If you have trouble booting an ISO image, here are some troubleshooting steps:

-  Did you verify the downloaded ISO image using hashes or GPG key?
-  Does your machine support 64-bit? If you're trying to run a 64-bit VM, then your 64-bit processor must support virtualization and virtualization must be enabled in the BIOS.
-  If you think your machine does support 64-bit, but you're still having problems with our 64-bit ISO image, try downloading the standard Ubuntu 18.04 64-bit ISO image or CentOS 7 64-bit ISO image and seeing if they run. If they don't, then you should verify your 64-bit compatibility.
-  | If all else fails but standard CentOS 7 64-bit or Ubuntu 18.04 64-bit installs normally, then you can always install our components on top of them as described on the following pages:
   | :ref:`quick-eval-non-iso`\ 
   | :ref:`production-deployment`
