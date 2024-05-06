.. _luks:

LUKS  
====

LUKS disk encryption is a feature that requires the use of the Security Onion Pro license. 

Enable LUKS During the ISO Install   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended way to use LUKS with Security Onion is to install via ISO. To set the ISO installer to present LUKS options users neeed to modify the string of the boot command. This can be done using the "e" key in BIOS boot mode or the "tab" key in UEFI boot mode. Under the boot parameters simply append luks=1 to the string.  

LUKS Install without a TPM
~~~~~~~~~~~~~~~~~~~~~~~~~~

During the initial install of the ISO, the user will be prompted to enter a password to use to encrypt the LUKS partitions. If multiple drives are detected then the user has the option of just encrypting /nsm. Please note that this password will be required at each reboot. 

LUKS Install Options with a TPM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If a TPM module is installed in the system you will have the option of storing the key in the TPM to unlock the drives automatically at boot. This process uses clevis in order to manage this process.   
