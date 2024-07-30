.. _fips:

FIPS  
====

FIPS stands for Federal Information Processing Standards and you can read more about it at https://en.wikipedia.org/wiki/Federal_Information_Processing_Standards.

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonion.com/pro for more information about purchasing a Security Onion Pro license to enable this feature.

Enabling FIPS During the ISO Install   
------------------------------------

The recommended way to use FIPS with Security Onion is to install via our Security Onion ISO image. At the ISO boot menu, you'll need to modify the boot command. This can be done using the ``e`` key in UEFI boot mode or the ``Tab`` key in BIOS boot mode before it automatically boots. Then append ``fips=1`` (and possibly other options like :ref:`luks` and :ref:`stig`) to the boot parameters and continue the boot process.
