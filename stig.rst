.. _stig:

STIG  
====

STIG stands for Security Technical Implementation Guide. For more information about STIGs, please see https://public.cyber.mil/stigs/.

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonionsolutions.com for more information about purchasing a Security Onion Pro license to enable this feature.

Enabling STIG During the ISO Install   
------------------------------------

The recommended way to use STIG with Security Onion is to install via our Security Onion ISO image. At the ISO boot menu, you'll need to modify the boot command. This can be done using the ``e`` key in UEFI boot mode or the ``Tab`` key in BIOS boot mode before it automatically boots. Then append ``stig=1`` (and possibly other options like :ref:`fips` and :ref:`luks`) to the boot parameters and continue the boot process.
