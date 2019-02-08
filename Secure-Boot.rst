Secure Boot
===========

| Modern kernels prevent the loading of unsigned third party modules
  (like PF\_RING) if UEFI Secure Boot is enabled.
| An example of this can be found here:
| https://groups.google.com/d/msg/security-onion/r64yl58KGJ4/uRedkKTBCAAJ

| If you have problems with Snort/Suricata/Bro/PF\_RING and have UEFI
  Secure Boot enabled, you can disable Secure Boot:
| https://wiki.ubuntu.com/UEFI/SecureBoot/DKMS\ 
| http://askubuntu.com/questions/762254/why-do-i-get-required-key-not-available-when-install-3rd-party-kernel-modules

In the future, we will transition from `<PF_RING>`__ to `<AF-PACKET>`__ and this
will no longer be an issue.
