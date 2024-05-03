.. _luks:

LUKS  
====

LUKS disk encryption is a feature that requires the use of the Security Onion Pro license. 

Enable LUKS During the ISO Install   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended way to use LUKS with Security Onion is to install via ISO. To set the ISO installer to present LUKS options users neeed to modify the string of the boot command. This can be done using the "e" key in BIOS boot mode or the "tab" key in UEFI boot mode. Under the boot parameters simply append luks=1 to the string.  

LUKS Install Options
