FIPS  
====

Federal Information Processing Standards  

Enable FIPS During the ISO Install   
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The recommended way to use FIPS with Security Onion is to install via ISO. To enable FIPS with the ISO installer users neeed to modify the string of the boot command. This can be done using the "e" key in UEFI boot mode or the "tab" key in BIOS boot mode. Under the boot parameters simply append fips=1 to the string.  
