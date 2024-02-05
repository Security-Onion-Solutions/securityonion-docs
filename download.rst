.. _download:

Download
========

Before downloading, we highly recommend that you review the :ref:`release-notes` section so that you are aware of all recent changes!

.. warning::

   **ALWAYS verify the checksum of the ISO image before booting!** This ensures that the ISO image hasn't been tampered with or corrupted during download. If it fails to verify, try downloading again. If it still fails to verify, try downloading from another computer or another network.

Download and verify our ISO image as shown at https://github.com/Security-Onion-Solutions/securityonion/blob/2.4/main/DOWNLOAD_AND_VERIFY_ISO.md.

.. warning::

   If you download our ISO image and then scan it with antivirus software, it is possible that one or more of the files included in the ISO image may generate false positives. If you look at the antivirus scan details, it will most likely tell you that it alerted on a file in ``SecurityOnion\agrules\``. This is part of :ref:`strelka` and it is being incorrectly flagged as a backdoor when it is really just a Yara ruleset that looks for backdoors. In some cases, the alert may be for a sample EXE that is included in :ref:`strelka` but again a false positive.
   
.. note::

  If you're going to create a bootable USB from the ISO image, there are many ways to do that.  One popular choice that seems to work well for many folks is Balena Etcher which can be downloaded at https://www.balena.io/etcher/.
