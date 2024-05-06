STIG  
====

Security Technical Implementation Guide

Enable STIG During the ISO Install   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended way to use STIG with Security Onion is to install via ISO. To enable STIG with the ISO installer users neeed to modify the string of the boot command. This can be done using the "e" key in UEFI boot mode or the "tab" key in BIOS boot mode. Under the boot parameters simply append stig=1 to the string.  

