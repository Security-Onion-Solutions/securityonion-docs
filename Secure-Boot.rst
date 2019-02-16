Secure Boot
===========

Modern Linux kernels prevent the loading of unsigned third party modules (like `<PF_RING>`__) if UEFI Secure Boot is enabled. An example of this can be found here: https://groups.google.com/d/msg/security-onion/r64yl58KGJ4/uRedkKTBCAAJ

To avoid issues like this, modern versions of our Setup wizard now default to `<AF-PACKET>`__ instead of `<PF_RING>`__ for both `<Bro>`__ and `<Suricata>`__: https://blog.securityonion.net/2019/02/new-setup-and-nsm-packages-now.html

| However, if you choose `<Snort>`__ as your NIDS engine, it will fall back to `<PF_RING>`__ (at least until Snort 3.0 is released). If you have problems with `<Snort>`__ and `<PF_RING>`__, you can disable Secure Boot:
| https://wiki.ubuntu.com/UEFI/SecureBoot/DKMS\ 
| http://askubuntu.com/questions/762254/why-do-i-get-required-key-not-available-when-install-3rd-party-kernel-modules
