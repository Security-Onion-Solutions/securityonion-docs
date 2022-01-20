.. _download:

Download
========

Before downloading, we highly recommend that you review the :ref:`release-notes` section so that you are aware of all recent changes!

You can either download our Security Onion ISO image (based on CentOS 7) **or** download a standard 64-bit CentOS 7, Ubuntu 18.04, or Ubuntu 20.04 ISO image and then add our Security Onion components. **Please keep in mind that we only support CentOS 7, Ubuntu 18.04, and Ubuntu 20.04**.

.. tip::

  For most use cases, we recommend using our Security Onion ISO image as it's the quickest and easiest method.
  
.. warning::

   **ALWAYS verify the checksum of ANY downloaded ISO image!** Regardless of whether you're downloading our Security Onion ISO image or a standard CentOS or Ubuntu ISO image, you should ALWAYS verify the downloaded ISO image to ensure it hasn't been tampered with or corrupted during download.

-  If downloading our Security Onion 2.3 ISO image, you can find the download link and verification instructions here:
   https://github.com/Security-Onion-Solutions/securityonion/blob/master/VERIFY_ISO.md
-  If downloading an Ubuntu or CentOS ISO image, please verify that ISO image using whatever instructions they provide.

.. warning::

   If you download our ISO image and then scan it with antivirus, it is possible that one or more of the files included in the ISO image may generate false positives. For example, Windows Defender may flag ``SecurityOnion\agrules\strelka\yara\thor-webshells.yar`` (part of :ref:`strelka`) as a backdoor when it is really just a Yara ruleset that looks for backdoors. As another example, McAfee may detect ``default_exe.exe`` (another part of :ref:`strelka`) as ``Artemis!EE468A4B1F55``.
   
.. seealso::

  If you're going to create a bootable USB from one of the ISO images above, there are many ways to do that.  One popular choice that seems to work well for many folks is Balena Etcher which can be downloaded at https://www.balena.io/etcher/.
