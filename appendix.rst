.. _appendix:

Appendix
========

This appendix covers the process of upgrading from the old Security Onion 16.04 to the new Security Onion 2.

.. warning::

   Security Onion 2 is a MAJOR architectural change, so please note the following:

   - Security Onion 2 has higher hardware requirements, so you should check that your hardware meets those requirements. 
   - Once you've upgraded from Ubuntu 16.04 to Ubuntu 18.04, you will essentially do a new installation of Security Onion 2 on top of Ubuntu 18.04.  Very little data will be retained during the upgrade!
   - There will be no way to migrate application accounts from Security Onion 16.04 to Security Onion 2.
   - There will be no way to migrate sguild data from Security Onion 16.04 to Security Onion 2.
   - You may need to purge pcap to make free space for the upgrade process. Any pcap remaining after the upgrade can only be accessed via tcpdump.
   - We do not provide any guarantees that the upgrade process will work! If the upgrade fails, be prepared to perform a fresh installation of Security Onion 2.
 
For the reasons listed above, we recommend that most users procure new hardware and perform a fresh installation of Security Onion 2.

.. tip::

   If you're planning to purchase new hardware, please consider official Security Onion appliances from Security Onion Solutions (https://securityonionsolutions.com). Our custom appliances have already been designed for certain roles and traffic levels and have Security Onion pre-installed. Purchasing from Security Onion Solutions will save you time and effort **and** help to support development of Security Onion as a free and open source platform!

If you have reviewed all of the warnings above and still want to attempt an in-place upgrade, you should be able to do the following:

.. warning::

   Please ensure you have local access to the machine being upgraded (console/DRAC/IPMI).  Failure to do so could result in an unsuccessful upgrade, requiring a clean installation of Security Onion 2. 

Make sure that Security Onion 16.04 is fully up-to-date:
::

   sudo soup

Reboot:
::

   sudo reboot


Copy and paste the following:

::

   sudo rm /etc/apt/sources.list.d/securityonion-ubuntu-stable-xenial.list && \    
   sudo so-stop && \  
   sudo service syslog-ng stop && \
   sudo service mysql stop && \
   sudo service salt-minion stop && \
   sudo docker system prune -a -f && \
   sudo sed -i 's|PREV="pre-.*$|PREV="pre-upgrade-to-18.04"|g' /var/lib/dpkg/info/securityonion-bro.preinst && \
   sudo /var/lib/dpkg/info/securityonion-bro.preinst install && \ 
   sudo apt install update-manager-core -y && \
   sudo sed -i 's|Prompt=never|Prompt=lts|g' /etc/update-manager/release-upgrades && \
   sudo pkill xscreensaver && \
   sudo do-release-upgrade

You may be interactively prompted to provide an answer to the following questions or similar during the upgrade:

::

   Non-superusers capture PCAP -> No
   login.defs -> Install package maintainer's version
   grub -> Choose to keep local version
   sshd_config -> Choose to keep local version
   syslog-ng.conf -> Choose to keep local version
   
   
At the end of release upgrade process, you will be prompted to reboot. Do NOT reboot yet, as you will most likely need to re-install openssh-server:
::

   sudo apt install openssh-server   
   
Reboot:
::
   
   sudo reboot

After upgrading to Ubuntu 18.04 and rebooting, copy and paste the following:
::

   sudo service apache2 stop && \
   sudo systemctl disable apache2.service && \
   sudo service mysql stop && \
   sudo systemctl disable mysql.service && \
   sudo ntpdate -u time.nist.gov && \ 
   sudo apt autoremove -f -y && \ 
   for i in $(dpkg -l | grep securityonion | awk '{print $2}'); do sudo apt remove $i -y -f --purge; done && \
   sudo mv /etc/salt/ /etc/salt_pre_upgrade && \
   sudo mv /var/ossec /var/ossec_pre_upgrade && \ 
   sudo apt purge salt-* -y && \
   sudo apt install netplan.io -y && \
   sudo apt purge -y ifupdown && \
   sudo rm /etc/network/interfaces* && \
   sudo mv /nsm/zeek/spool/ /nsm/zeek/old_spool && \
   sudo mv /nsm/zeek/logs/stats/ /nsm/zeek/logs/old_stats && \
   sudo sed -i 's/^*/#/' /etc/cron.d/salt-update


On Distributed Manager - also do the following for Redis:
::

   sudo systemctl stop redis.service && \
   sudo systemctl disable redis.service && \
   sudo apt purge redis -y
   
Remove all left-over unneeded packages:
::

   sudo apt autoremove -y

Apply netplan for the management interface in ``/etc/netplan/netplan.yaml`` (create the file and ensure that the extension is ``.yaml``).

If using DHCP (NOT recommended):

::
   
   network:
     version: 2
     renderer: networkd
     ethernets:
       ens18:
         dhcp4: true


If using static IP:
::

   network:
     version: 2
     renderer: networkd
     ethernets:
       ens18:
         addresses:
           - 10.10.10.2/24
         gateway4: 10.10.10.1
         nameservers:
           search: [mydomain]
           addresses: [10.10.10.1, 1.1.1.1]


Other examples: https://netplan.io/examples/

Apply the netplan configuration (may disconnect after this command, so ensure local access is available):
::

   sudo netplan apply

Reboot:
::

   sudo reboot

Delete "Wired connection 1" for later use as bond interface:
::

   sudo nmcli con delete "Wired connection 1"

.. warning::

   Don't reboot yet!

Install Security Onion 2:

Skip to step 7, detailed here: 
   
https://docs.securityonion.net/en/2.3/installation.html#installation-on-ubuntu-or-centos
 
Post-Installation:

While the files will still reside disk, config files/settings will NOT be migrated to the appropriate format/locations for Security Onion 2.

Example configuration may include:

- IDS Rule Oinkcode/Thresholds/Disablements (``/etc/nsm/rules/threshold.conf``, ``/etc/nsm/pulledpork``)
- Custom Logstash config (``/etc/logstash/custom``)
- Custom Zeek scripts or BPFs (``/opt/zeek/share/zeek/policy``, ``/etc/nsm/rules/bpf.conf``)

