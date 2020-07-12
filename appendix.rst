.. _appendix:

Appendix
========

This appendix covers the process of upgrading from the old Security Onion 16.04 to the new Security Onion 2.0.

.. warning::

   Security Onion 2.0 is a MAJOR architectural change, so please note the following:

   - Security Onion 2.0 has higher hardware requirements, so you should check that your hardware meets those requirements. 
   - Once you've upgraded from Ubuntu 16.04 to Ubuntu 18.04, you will essentially do a new installation of Security Onion 2.0 on top of Ubuntu 18.04.  Very little data will be retained during the upgrade!
   - There will be no way to migrate application accounts from 16.04 to 2.0.
   - There will be no way to migrate sguild data from 16.04 to 2.0.
   - You may need to purge pcap to make free space for the upgrade process. Any pcap remaining after the upgrade can only be accessed via tcpdump.
   - We do not provide any guarantees that the upgrade process will work! If the upgrade fails, be prepared to perform a fresh installation of Security Onion 2.0.
 
For the reasons listed above, we recommend that most users procure new hardware and perform a fresh installation of Security Onion 2.0.

.. tip::

   If you're planning to purchase new hardware, please consider official Security Onion appliances from Security Onion Solutions (https://securityonionsolutions.com). Our custom appliances have already been designed for certain roles and traffic levels and have Security Onion pre-installed. Purchasing from Security Onion Solutions will save you time and effort **and** help to support development of Security Onion as a free and open source platform!

If you have reviewed all of the warnings above and still want to attempt an in-place upgrade, you should be able to do the following:

 - perform an in-place upgrade from Ubuntu 16.04 to Ubuntu 18.04 using standard Ubuntu procedures
 - once you have completed the Ubuntu 18.04 upgrade, follow the Ubuntu 18.04 instructions in the Installation Guide
