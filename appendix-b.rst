.. _appendix-b:

Appendix B
==========

This appendix covers the process of upgrading a Security Onion 2.3 standalone installation from Ubuntu 18.04 to Ubuntu 20.04.

.. warning::

   - We do not provide any guarantees that the upgrade process will work! If the upgrade fails, be prepared to perform a fresh installation.
   - Please ensure that you have local access to the machine being upgraded via console, DRAC, IPMI, etc. Failure to do so could result in an unsuccessful upgrade, requiring a fresh installation.

If you have reviewed all of the warnings above and still want to attempt an in-place upgrade, you should be able to do the following.

First, make sure that all Ubuntu packages are fully up-to-date and then reboot:
::

   sudo apt update && sudo apt upgrade -y && sudo reboot

After rebooting, copy and paste the following multi-line command to initiate the upgrade process:
::

   sudo apt-mark unhold salt-* && \
   sudo apt-mark unhold docker* && \
   sudo sed -i 's|^deb \[arch=amd64\] https://download.docker.com|# deb [arch=amd64] https://download.docker.com|g' /etc/apt/sources.list && \
   sudo sed -i 's|^deb|# deb|' /etc/apt/sources.list.d/wazuh.list && \
   sudo sed -i 's|^deb|# deb|' /etc/apt/sources.list.d/saltstack.list && \
   sudo do-release-upgrade

When prompted about configuration options, accept the default option. When the upgrade is complete, it will prompt you to reboot. After rebooting, copy and paste the following multi-line command:
::

   sudo sed -i 's|# deb \[arch=amd64\] https://download.docker.com/linux/ubuntu bionic|deb [arch=amd64] https://download.docker.com/linux/ubuntu focal|g' /etc/apt/sources.list && \
   sudo sed -i 's|# deb|deb|' /etc/apt/sources.list.d/wazuh.list && \
   sudo sed -i 's|# deb|deb|' /etc/apt/sources.list.d/saltstack.list && \
   sudo sed -i 's|bionic|focal|' /etc/apt/sources.list.d/saltstack.list && \
   sudo sed -i 's|18|20|' /etc/apt/sources.list.d/saltstack.list && \
   sudo apt update && \
   sudo apt upgrade -y && \
   sudo apt install salt-common salt-master salt-minion -y && \
   sudo touch /etc/NetworkManager/conf.d/10-globally-managed-devices.conf && \
   sudo service network-manager restart && \
   sudo rm -rf /opt/so/state/influxdb* && \
   sudo salt-call state.highstate -linfo queue=True ; \
   sudo so-status

Review the output for any errors and make sure all services started properly.
