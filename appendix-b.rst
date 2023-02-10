.. _appendix-b:

Appendix B: Ubuntu 18.04
========================

This appendix covers the process of upgrading a Security Onion 2.3 deployment from Ubuntu 18.04 to Ubuntu 20.04.

.. warning::

   - We do not provide any guarantees that the upgrade process will work! If the upgrade fails, be prepared to perform a fresh installation.
   - Please ensure that you have local access to the machine being upgraded via console, DRAC, IPMI, etc. Failure to do so could result in an unsuccessful upgrade, requiring a fresh installation.
   - Plan on at least one hour per node to complete the upgrade process.
   - If you have a distributed deployment with nodes configured to pull updates from the manager, you may need to comment out the proxy config in ``/etc/apt/apt.conf.d/00Proxy`` and make sure they can reach the Internet directly.

If you have reviewed all of the warnings above and still want to attempt an in-place upgrade, you should be able to follow the steps below.

.. note::

   If you have a distributed deployment, you will need to perform the steps on the manager first and then on each of the remaining nodes.

First, verify that the system is currently on Ubuntu 18.04:
::

   grep VERSION_ID /etc/os-release

Next, make sure that all Ubuntu packages are fully up-to-date and then reboot: 
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

When prompted about configuration options, accept the default option. When the upgrade is complete, it will prompt you to reboot.

After rebooting, copy and paste the following multi-line command:
::

   sudo sed -i 's|# deb \[arch=amd64\] https://download.docker.com/linux/ubuntu bionic|deb [arch=amd64] https://download.docker.com/linux/ubuntu focal|g' /etc/apt/sources.list && \
   sudo sed -i 's|# deb|deb|' /etc/apt/sources.list.d/wazuh.list && \
   sudo sed -i 's|# deb|deb|' /etc/apt/sources.list.d/saltstack.list && \
   sudo sed -i 's|bionic|focal|' /etc/apt/sources.list.d/saltstack.list && \
   sudo sed -i 's|18|20|' /etc/apt/sources.list.d/saltstack.list && \
   sudo apt update && \
   sudo apt upgrade -y && \
   sudo apt install salt-common salt-master salt-minion -y

If this node has any sniffing interfaces, then you may need to update NetworkManager:
::

   sudo touch /etc/NetworkManager/conf.d/10-globally-managed-devices.conf && \
   sudo service network-manager restart

If this node is a manager, then you may need to remove some influxdb files:
::

   sudo rm -rf /opt/so/state/influxdb*

Run all salt states and review the output for any errors:
::

   sudo salt-call state.highstate -linfo queue=True

Finally, make sure all services started properly:
::

   sudo so-status
