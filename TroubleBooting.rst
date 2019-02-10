Booting Issues
==============

-  Did you verify the downloaded ISO image as described on the
   `Installation <Installation>`__ page?
-  Does your machine support 64-bit? (If you're trying to run a 64-bit
   VM, then your 64-bit processor must support virtualization and
   virtualization must be enabled in the BIOS.) If not, then you'll need
   to obtain a 64-bit machine to use our 64-bit ISO image (recommended).
-  If you think your machine does support 64-bit, but you're still
   having problems with our 64-bit ISO image, try downloading the Ubuntu
   16.04 64-bit ISO image and seeing if it runs. If it doesn't, then you
   should verify your 64-bit compatibility.
-  If the ISO image boots, but it does not get past the splash screen,
   try pressing the "Esc" key to see the current status.
-  If the ISO image boots, but the Live Desktop doesn't appear properly,
   it may be a video card/driver issue. Try changing ``modeset``
   options:
   https://groups.google.com/d/topic/security-onion/FTEecyn4uJ4/discussion\ 
   https://groups.google.com/d/topic/security-onion/UKE5-dqybQ4/discussion\ 
   https://groups.google.com/d/topic/security-onion/51JZWXZfBho/discussion\ 
-  | If all else fails but standard Ubuntu 16.04 installs normally, then you can always install our packages and Docker images on top of your Ubuntu 16.04 installation as described on our wiki:
   | `InstallingOnUbuntu <InstallingOnUbuntu>`__\ 
   | `ProductionDeployment <ProductionDeployment>`__
