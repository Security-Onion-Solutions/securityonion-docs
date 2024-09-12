.. _stig:

STIG  
====

STIG stands for Security Technical Implementation Guide. For more information about STIGs, please see https://public.cyber.mil/stigs/.

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonion.com/pro for more information about purchasing a Security Onion Pro license to enable this feature.

STIG During the ISO Install
---------------------------

The recommended way to use STIG with Security Onion is to install via our Security Onion ISO image. From the :ref:`installation` menu you'll select the ``Install Security Onion Pro`` option.

Installing using the Security Onion Pro menu options will create additional partitions on your system to meet the STIG requirements. The partitions created include:

==============       =========
 Partition            Storage
==============       =========
/home                  25GB
/tmp                   2GB
/var                   50GB
/var/log               5GB
/var/log/audit         2GB
/var/log/tmp           2GB
==============       =========

In addition to the required partitions, using the STIG menu option will also configure the system to use :ref:`fips` mode, and enable :ref:`luks` disk encryption. Both of these options can be used independently of the STIG menu option depending on your requirements.

Enabling STIG
-------------
.. warning::

    | Before enabling STIGs on your production Security Onion deployment, we recommend testing in a development environment. With different environments and configurations, there may be unexpected errors.

To enable STIGs you'll first need setup your Security Onion grid and apply your :ref:`Security Onion Pro <pro>` license. You can then navigate to :ref:`administration` --> Configuration --> stig --> enabled and set the value to ``true``.

.. note::

    | You will need to enable the :ref:`administration-advanced-settings` option to modify this setting.

OpenSCAP
--------
In order to apply STIGs on Security Onion we use a combination of our existing Saltstack configuration managment and OpenSCAP. Currently, OpenSCAP is using a draft version of STIGs for Oracle Linux 9.

OpenScap can be configured to run at different time intervals. By default, OpenSCAP will run a remediation every 12 hours meaning any changes made to the system that bring it out of compliance will be reverted back to the STIG compliant state. This setting can be lowered or increased by modifying the ``run_interval`` setting found under :ref:`administration` --> Configuration --> stig

With the STIG feature enabled, you can find OpenSCAP reports under ``/opt/so/log/stig``. Currently, the expected compliance score is 86%.

More information
----------------
For more information about OpenSCAP see: https://www.open-scap.org/
For more information about STIGs see: https://public.cyber.mil/stigs/
