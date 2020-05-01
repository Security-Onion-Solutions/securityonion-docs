Upgrading from 14.04 to 16.04
=============================

Please read through this entire page before beginning!

.. warning::

   -  We offer no guarantees that this upgrade process will work perfectly.
   
   -  Before upgrading production sensors, you should fully test this upgrade process on test sensors in a test environment that closely matches your production environment.
   
   -  Argus, Pads, Prads, and ELSA are no longer supported -- these software packages will be removed upon upgrade and will not be supported in future releases.
   
   -  If you were previously running ELSA, please ensure your system has been converted to `Elastic <ELSA-to-Elastic>`__ before upgrading.

Pre-upgrade Notes
-----------------

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

-  If you're upgrading a master server and you have a large ip2c table,
   you may want to truncate it and populate fresh data before initiating
   the 16.04 upgrade:

   ::

       sudo mysql --defaults-file=/etc/mysql/debian.cnf -Dsecurityonion_db -e 'truncate table ip2c;'    
       sudo so-squert-ip2c

-  After upgrading the master server, ensure all sensors are upgraded as
   soon as possible to minimize disruption and/or incompatibility
   issues. Mixed-release (14.04 + 16.04) environments are currently
   untested and unsupported.

Preparation
-----------

-  Start with a fully configured Security Onion 14.04 (Elastic Stack)
   installation.

-  If running in a VM, create a snapshot so that you can revert if
   necessary.

-  You may want to record a transcript of the full upgrade so you can
   refer back to it in case of any errors. For more information, please
   see
   https://www.debian.org/releases/stable/i386/release-notes/ch-upgrading.en.html#record-session.

-  NON-MASTER MACHINES ONLY - If the master server has already been
   upgraded, on each forward node, heavy node, or storage node, do the
   following:

   ::

       sudo rm /etc/apt/sources.list.d/securityonion-ubuntu-stable-xenial.list  
       sudo service salt-minion stop

-  | Ensure all 14.04 updates are installed:
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

       sudo sed -i 's|PREV="pre-.*$|PREV="pre-upgrade-to-16.04"|g' /var/lib/dpkg/info/securityonion-bro.preinst
       sudo /var/lib/dpkg/info/securityonion-bro.preinst install

-  | Verify that Bro config was backed up to
     /opt/bro/etc\_pre-upgrade-to-16.04/ (you should have files in this
     directory):
   | ``ls -alh /opt/bro/etc_pre-upgrade-to-16.04/``

-  You may want to backup any other files that you've manually modified.

Upgrade from Ubuntu 14.04 to Ubuntu 16.04
-----------------------------------------

-  | Configure Ubuntu to look for the 16.04 upgrade:
   | ``sudo sed -i 's|Prompt=never|Prompt=lts|g' /etc/update-manager/release-upgrades``

-  | Kill xscreensaver (otherwise, do-release-upgrade in the next step
     will prompt you to do so):
   | ``sudo pkill xscreensaver``

-  | Initiate upgrade to Ubuntu 16.04:
   | ``sudo do-release-upgrade``

-  | If you receive a message like ``No new release found.``, then
     you'll need to ensure you can reach the Ubuntu changelogs site:
   | ``curl http://changelogs.ubuntu.com/meta-release-lts``

   If you can't reach the site, try checking for connectivity, or your
   firewall to see if it is being blocked.

-  If you receive a prompt to restart services during the upgrade,
   choose ``Yes``.

-  If you receive a prompt to allow non-superusers to capture packets
   (Wireshark), choose ``No``.

-  If you receive a prompt in regard to grub configuration, choose
   ``keep local GRUB configuration``.

-  Follow the prompts. If you receive a prompt regarding xscreensaver,
   select OK. You may receive prompts regarding files that have changed
   like the following:

   +----------------------------------------------------+----------+
   | file                                               | answer   |
   +====================================================+==========+
   | /etc/sudoers                                       | ``Y``    |
   +----------------------------------------------------+----------+
   | /etc/default/grub                                  | ``N``    |
   +----------------------------------------------------+----------+
   | /etc/apt/apt.conf.d/01autoremove                   | ``N``    |
   +----------------------------------------------------+----------+
   | /etc/apt/apt.conf.d/99update-notifier              | ``N``    |
   +----------------------------------------------------+----------+
   | /etc/apache2/mods-available/ssl.conf               | ``Y``    |
   +----------------------------------------------------+----------+
   | /etc/apache2/apache2.conf                          | ``Y``    |
   +----------------------------------------------------+----------+
   | /etc/apache2/ports.conf                            | ``Y``    |
   +----------------------------------------------------+----------+
   | /etc/syslog-ng/syslog-ng.conf                      | ``N``    |
   +----------------------------------------------------+----------+
   | /etc/php5/apache2/php.ini                          | ``Y``    |
   +----------------------------------------------------+----------+
   | /etc/xdg/menus/gnome-flashback-applications.menu   | ``N``    |
   +----------------------------------------------------+----------+
   | /etc/redis/redis.conf                              | ``N``    |
   +----------------------------------------------------+----------+
   | /etc/pulse/default.pa                              | ``N``    |
   +----------------------------------------------------+----------+

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

-  If you receive an error message in regard to mysql-server, please
   disregard and continue with the upgrade.

-  When prompted to restart, press ``Y`` to continue.

Add back Security Onion packages
--------------------------------

-  After rebooting, log back in.

-  If running in a VM, perform a snapshot.

-  Open a terminal, remove the old PPA, and add our stable PPA:

   ::

        sudo rm /etc/apt/sources.list.d/*    
        sudo add-apt-repository -y ppa:securityonion/stable    
        sudo apt-get update 

-  Add back any missing Security Onion packages by installing the
   ``securityonion-iso`` metapackage. If you didn't install from our ISO
   and instead installed from your preferred flavor of Ubuntu and added
   our PPA and packages, then you may not necessarily need to install
   the ``securityonion-iso`` metapackage. In the command below, you can
   replace ``securityonion-iso`` with the same Security Onion
   metapackage(s) you originally installed (``securityonion-server``,
   ``securityonion-sensor``, ``securityonion-all``, etc).:

   ``sudo apt-get install securityonion-iso syslog-ng-core``\ 

-  **IMPORTANT!** If you receive a prompt regarding ``syslog-ng.conf``,
   press ``N`` to keep your currently-installed version.

-  | If you encounter an error in regard to ``mod_passenger.so``, try
     disabling the module as follows:
   | ``sudo a2dismod passenger``

-  | Copy backed up Bro config back to ``/opt/bro/etc``:
   | ``sudo cp /opt/bro/etc_pre-upgrade-to-16.04/* /opt/bro/etc``

-  | Copy OSSEC config back in place:
   | ``sudo cp /var/ossec/etc/ossec.conf-2.8 /var/ossec/etc/ossec.conf``
   | ``sudo /var/ossec/bin/ossec-control enable client-syslog``

-  | Stop salt-minion and salt-master before running soup:
   | ``sudo service salt-minion stop``
   | ``sudo service salt-master stop``

-  | Update all packages that are currently installed:
   | ``sudo soup -y``

-  | Soup should prompt for a reboot. After reboot, run the following to
     enable ``securityonion.service``:
   | ``sudo systemctl enable securityonion.service``

-  NON-MASTER MACHINES ONLY:

   | run the following to disable MySQL:
   | ``sudo systemctl disable mysql``

   | run the following to disable salt-master:
   | ``sudo systemctl disable salt-master``

   | run the following to disable Redis:
   | ``sudo systemctl disable redis``

-  | Reboot again:
   | ``sudo reboot``

-  | MASTER ONLY - If sguild does not start after reboot, try running
     ``sguil-db-purge``:
   | ``sudo sguil-db-purge``

Clean Up
--------

-  Review your Snort/Suricata/Bro/other configuration for any local
   customizations that you may need to re-apply.

-  | Clean up old UFW file:
   | ``sudo rm /etc/ufw/applications.d/apache2.2-common``

-  | Remove old Security Onion init file:
   | ``sudo rm /etc/init/securityonion.conf``

-  | Remove any unnecessary packages:
   | ``sudo apt-get autoremove``

-  | Reboot:
   | ``sudo reboot``

Verify
------

-  After rebooting, log back in.

-  Verify that ``/etc/update-manager/release-upgrades`` has
   ``Prompt=never`` to avoid prompts to upgrade to 18.04 (not supported
   right now).

-  Keep in mind, Logstash may take a few minutes to initialize, so you
   may want to wait a few minutes before continuing.

-  | Verify services are running:
   | ``sudo so-status``

-  | Run sostat and look for anything out of the ordinary:
   | ``sudo sostat``

-  Check log files for anything out of the ordinary.

MySQL root password
-------------------

-  We will need to set a randomized root password for MySQL. We can do
   so by doing the following:

   .. rubric:: Reset debian.cnf:
      :name: reset-debian.cnf

   | ``sudo rm /etc/mysql/debian.cnf``
   | ``sudo dpkg-reconfigure --frontend noninteractive mysql-server-5.7``

If root password is blank, set random password:

::

     if echo "quit" | sudo mysql -uroot 2>/dev/null; then
          PASSWORD=$(LC_ALL=C </dev/urandom tr -dc '[:alnum:]' | head -c 32)
          sudo mysql --defaults-file=/etc/mysql/debian.cnf -e "ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 
         '$PASSWORD';"
     fi

Optional
--------

-  | Switch to pure GNOME desktop:
   | ``sudo so-desktop-gnome``

-  If you disabled the GUI previously, you'll need to re-apply similar
   configuration to boot into text mode:

   ::

       sudo systemctl enable multi-user.target --force    
       sudo systemctl set-default multi-user.target    
       sudo reboot
