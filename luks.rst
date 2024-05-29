.. _luks:

LUKS  
====

LUKS stands for Linux Unified Key Setup and you can read more about it at https://en.wikipedia.org/wiki/Linux_Unified_Key_Setup.

LUKS disk encryption is a feature that requires the use of the Security Onion Pro license. 

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonionsolutions.com for more information about purchasing a Security Onion Pro license to enable this feature.

Enabling LUKS During the ISO Install   
------------------------------------

The recommended way to use LUKS with Security Onion is to install via our Security Onion ISO image. At the ISO boot menu, you'll need to modify the boot command. This can be done using the ``e`` key in UEFI boot mode or the ``Tab`` key in BIOS boot mode before it automatically boots. Then append ``luks=1`` (and possibly other options like :ref:`fips` and :ref:`stig`) to the boot parameters and continue the boot process.

LUKS Install without a TPM
--------------------------

During the initial install of the ISO, the user will be prompted to enter a password to use to encrypt the LUKS partitions. If multiple drives are detected then the user has the option of just encrypting /nsm. Please note that this password will be required at each boot. 

LUKS Install Options with a TPM
-------------------------------

If a TPM module is installed in the system you will have the option of storing the key in the TPM to unlock the drives automatically at boot. This process uses clevis in order to manage this process.   
