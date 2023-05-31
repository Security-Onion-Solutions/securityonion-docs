.. _download:

Download
========

Before downloading, we highly recommend that you review the :ref:`release-notes` section so that you are aware of all recent changes!

You can either download our Security Onion ISO image (based on Rocky Linux 9) **or** download a standard x86-64 Rocky Linux 9 Minimal or Ubuntu 20.04 ISO image and then add our Security Onion components. **Please keep in mind that Ubuntu 20.04 is not supported for manager nodes and will be phased out altogether in the future.**

.. tip::

  For most use cases, we recommend using our Security Onion ISO image as it's the quickest and easiest method.
  
.. warning::

   **ALWAYS verify the checksum of ANY downloaded ISO image!** Regardless of whether you're downloading our Security Onion ISO image or a standard Rocky Linux or Ubuntu ISO image, you should ALWAYS verify the downloaded ISO image to ensure it hasn't been tampered with or corrupted during download.

-  If downloading our Security Onion ISO image, you can find the download link and verification instructions here:
   https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/VERIFY_ISO.md
-  If downloading an Ubuntu or Rocky Linux ISO image, please verify that ISO image using whatever instructions they provide.

.. warning::

   If you download our ISO image and then scan it with antivirus software, it is possible that one or more of the files included in the ISO image may generate false positives. If you look at the antivirus scan details, it will most likely tell you that it alerted on a file in ``SecurityOnion\agrules\``. This is part of :ref:`strelka` and it is being incorrectly flagged as a backdoor when it is really just a Yara ruleset that looks for backdoors. In some cases, the alert may be for a sample EXE that is included in :ref:`strelka` but again a false positive.
   
.. note::

  If you're going to create a bootable USB from one of the ISO images above, there are many ways to do that.  One popular choice that seems to work well for many folks is Balena Etcher which can be downloaded at https://www.balena.io/etcher/.
