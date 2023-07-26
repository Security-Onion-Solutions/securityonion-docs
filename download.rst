.. _download:

Download
========

Before downloading, we highly recommend that you review the :ref:`release-notes` section so that you are aware of all recent changes!

We recommend that you download our Security Onion ISO image but see the :ref:`os` page for other options.

.. tip::

  For most use cases, we recommend using our Security Onion ISO image as it's the quickest and easiest method.
  
.. warning::

   **ALWAYS verify the checksum of ANY downloaded ISO image!** Regardless of whether you're downloading our Security Onion ISO image or any other ISO image, you should ALWAYS verify the downloaded ISO image to ensure it hasn't been tampered with or corrupted during download. If it fails to verify, try downloading again. If it still fails to verify, try downloading from another computer or another network.

-  If downloading our Security Onion ISO image for version 2.4.3 or later, you can find the download link and verification instructions at https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/DOWNLOAD_AND_VERIFY_ISO.md.
-  If downloading any other ISO image, please verify that ISO image using whatever instructions they provide.

.. warning::

   If you download our ISO image and then scan it with antivirus software, it is possible that one or more of the files included in the ISO image may generate false positives. If you look at the antivirus scan details, it will most likely tell you that it alerted on a file in ``SecurityOnion\agrules\``. This is part of :ref:`strelka` and it is being incorrectly flagged as a backdoor when it is really just a Yara ruleset that looks for backdoors. In some cases, the alert may be for a sample EXE that is included in :ref:`strelka` but again a false positive.
   
.. note::

  If you're going to create a bootable USB from one of the ISO images above, there are many ways to do that.  One popular choice that seems to work well for many folks is Balena Etcher which can be downloaded at https://www.balena.io/etcher/.
