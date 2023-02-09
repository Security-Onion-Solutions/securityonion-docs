.. _appendix-b:

Appendix B
==========

This appendix covers the process of upgrading from Ubuntu 16.04 to Ubuntu 18.04.

.. warning::

   - We do not provide any guarantees that the upgrade process will work! If the upgrade fails, be prepared to perform a fresh installation.
   - Please ensure that you have local access to the machine being upgraded via console, DRAC, IPMI, etc.  Failure to do so could result in an unsuccessful upgrade, requiring a fresh installation.

If you have reviewed all of the warnings above and still want to attempt an in-place upgrade, you should be able to do the following.

First, make sure that all Ubuntu packages are fully up-to-date:
::

   sudo apt update && sudo apt upgrade -y

Reboot:
::

   sudo reboot

Once the system has booted, copy and paste the following into a terminal to prepare for the upgrade process:
::

   sudo sed -i 's|deb \[arch=amd64\] https://download.docker.com|#deb [arch=amd64] https://download.docker.com|g' /etc/apt/sources.list && \
   sudo sed -i 's/^/#/' /etc/apt/sources.list.d/wazuh.list && \
   sudo sed -i 's/^/#/' /etc/apt/sources.list.d/saltstack.list && \
   sudo apt-mark unhold docker* && \
   sudo apt-mark unhold salt-*
   
Initiate the upgrade from Ubuntu 18.04 to Ubuntu 20.04:
::
   
   sudo do-release-upgrade

If prompted, accept all the defaults. When the upgrade is complete, reboot:
::

   sudo reboot

After rebooting, copy and paste the following:
::

   sudo sed -i 's|#deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic|deb [arch=amd64] https://download.docker.com/linux/ubuntu focal|g' /etc/apt/sources.list && \
   sudo sed -i 's/#//' /etc/apt/sources.list.d/wazuh.list && \
   sudo sed -i 's/#//' /etc/apt/sources.list.d/saltstack.list && sed -i 's/bionic/focal/' /etc/apt/sources.list.d/saltstack.list && sed -i 's/18/20/' /etc/apt/sources.list.d/saltstack.list && \
   sudo apt update && apt upgrade -y && \
   sudo apt install salt-common salt-master salt-minion -y && \
   sudo touch /etc/NetworkManager/conf.d/10-globally-managed-devices.conf && \
   sudo service network-manager restart && \
   sudo rm -rf /opt/so/state/influxdb* && \
   sudo so-checkin

