Please read through this entire page before beginning!

DISCLAIMERS
===========

-  We offer no guarantees that this upgrade process will work perfectly.

WARNINGS
========

-  Before upgrading production sensors, you should fully test this
   upgrade process on test sensors in a test environment that closely
   matches your production environment.

PRE-UPGRADE NOTES
=================

-  If you are behind a proxy, make sure that you've `configured your
   proxy settings <Proxy>`__. In the commands below that use sudo, you
   may need to use ``sudo -i`` so that your proxy settings are applied
   to the sudo environment.

-  The upgrade process will take at **least** 1-2 hours (per
   server/sensor), depending on the speed of your server hardware and
   Internet connection. Please plan accordingly.

-  If you’re upgrading a distributed deployment, you’ll need to perform
   the steps below on the master server and all sensors, but make sure
   you **start with the master server first!**

-  After upgrading the master server, ensure all sensors are upgraded as
   soon as possible to minimize disruption and/or incompatibility
   issues. Mixed-release (12.04 + 14.04) environments are currently
   untested and unsupported.

PREPARATION
===========

-  Start with a fully configured Security Onion 12.04 installation.

-  If running in a VM, create a snapshot so that you can revert if
   necessary.

-  You may want to record a transcript of the full upgrade so you can
   refer back to it in case of any errors. For more information, please
   see
   https://www.debian.org/releases/stable/i386/release-notes/ch-upgrading.en.html#record-session.

-  | Ensure all 12.04 updates are installed:
   | ``sudo soup``

-  | If soup prompted to reboot, go ahead and do that. If it didn’t, go
   | ahead and reboot anyway:
   | ``sudo reboot``

-  | Review sostat output to make sure system is healthy before
     continuing:
   | ``sudo sostat``

-  **IMPORTANT!** Backup Bro config since it will be removed when Ubuntu
   removes the package:

   ::

       sudo sed -i 's|PREV="2.3.2"|PREV="pre-2.4"|g' /var/lib/dpkg/info/securityonion-bro.preinst
       sudo /var/lib/dpkg/info/securityonion-bro.preinst install

-  | Verify that Bro config was backed up to /opt/bro/etc\_pre-2.4/ (you
     should have files in this directory):
   | ``ls -alh /opt/bro/etc_pre-2.4/``

-  You may want to backup any other files that you've manually modified.

UPGRADE FROM UBUNTU 12.04 TO UBUNTU 14.04
=========================================

-  | Configure Ubuntu to look for the 14.04 upgrade:
   | ``sudo sed -i 's|Prompt=never|Prompt=lts|g' /etc/update-manager/release-upgrades``

-  | Kill xscreensaver (otherwise, do-release-upgrade in the next step
     will prompt you to do so):
   | ``sudo pkill xscreensaver``

-  | Initiate upgrade to Ubuntu 14.04:
   | ``sudo do-release-upgrade``

-  Follow the prompts. If you receive a prompt regarding xscreensaver,
   select OK. You may receive prompts regarding files that have changed
   like the following:

   +-----------------------------------------------------+----------+
   | file                                                | answer   |
   +=====================================================+==========+
   | /etc/sudoers                                        | ``Y``    |
   +-----------------------------------------------------+----------+
   | /etc/apache2/mods-available/ssl.conf                | ``Y``    |
   +-----------------------------------------------------+----------+
   | /etc/apache2/apache2.conf                           | ``Y``    |
   +-----------------------------------------------------+----------+
   | /etc/apache2/ports.conf                             | ``Y``    |
   +-----------------------------------------------------+----------+
   | /etc/syslog-ng/syslog-ng.conf                       | ``N``    |
   +-----------------------------------------------------+----------+
   | /etc/php5/apache2/php.ini                           | ``Y``    |
   +-----------------------------------------------------+----------+
   | /etc/xdg/xdg-xubuntu/menus/xfce-applications.menu   | ``Y``    |
   +-----------------------------------------------------+----------+

-  These are files that Security Onion modifies, and you may receive
   prompts for additional files that you have modified. The safest
   option for each of these is to choose to install the package
   maintainer’s version (``Y``, where applicable), with the exception of
   the prompt in regard to syslog-ng.conf. Choosing the installation of
   the package maintainer's version will back up the existing file in
   case you need to review it later for any custom modifications you had
   made.
-  **IMPORTANT!** If you receive a prompt regarding syslog-ng.conf,
   press ``N`` to keep your currently-installed version.

-  When prompted to restart, press ``Y`` to continue.

ADD BACK SECURITY ONION PACKAGES
================================

-  After rebooting, log back in.

-  If running in a VM, perform a snapshot.

-  | Open a terminal, and add back our stable PPA:
   | ``sudo apt-get install -y software-properties-common``
   | ``sudo add-apt-repository ppa:securityonion/stable``
   | ``sudo apt-get update``

-  Add back any missing Security Onion packages by installing the
   ``securityonion-iso`` metapackage. If you didn't install from our ISO
   and instead installed from your preferred flavor of Ubuntu and added
   our PPA and packages, then you may not necessarily need to install
   the ``securityonion-iso`` metapackage. In the command below, you can
   replace ``securityonion-iso`` with the same Security Onion
   metapackage(s) you originally installed (``securityonion-server``,
   ``securityonion-sensor``, ``securityonion-all``,
   ``securityonion-elsa``, etc).:

   ``sudo apt-get install securityonion-iso syslog-ng-core``\ 

-  **IMPORTANT!** If you receive a prompt regarding ``syslog-ng.conf``,
   press ``N`` to keep your currently-installed version.

-  | If you encounter an error in regard to ``mod_passenger.so``, try
     disabling the module as follows:
   | ``sudo a2dismod passenger``

-  | Update all packages that are currently installed:
   | ``sudo soup``

CLEAN UP
========

-  Review your Snort/Suricata/Bro/other configuration for any local
   customizations that you may need to re-apply.

-  | Clean up old UFW file:
   | ``sudo rm /etc/ufw/applications.d/apache2.2-common``

-  | Remove any unnecessary packages:
   | ``sudo apt-get autoremove``

-  | Reboot:
   | ``sudo reboot``

VERIFY
======

-  After rebooting, log back in.

-  Keep in mind that there is a 60 second delay after the system boots
   before it tries to start any Security Onion processes, so wait a
   minute or two before continuing.

-  | Verify services are running:
   | ``sudo service nsm status``

-  | If you had created your own ELSA query menu at
     /var/www/elsa/local.php and it wasn't automatically migrated to
     /var/www/so/elsa/local.php, then you can copy it:
   | ``sudo cp /var/www/elsa/local.php /var/www/so/elsa/local.php``
   | You may also need to adjust any links to match the new URL
     structure. Replace
     ``<a href="https://<?php echo $_SERVER['HTTP_HOST']; ?>:3154/?``
     with ``<a href="/elsa-query/?``

-  | Run sostat and look for anything out of the ordinary:
   | ``sudo sostat``

-  Check log files for anything out of the ordinary.
