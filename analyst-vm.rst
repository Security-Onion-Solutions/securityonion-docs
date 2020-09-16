.. _analyst-vm:

Analyst VM
==========

Full-time analysts may want to create a dedicated Analyst VM. This allows you to investigate pcaps and other potentially malicious artifacts without fear of impacting your Security Onion deployment or your workstation.

Starting in Security Onion 2.2, the ``so-analyst`` script will install a full GNOME desktop environment including Chromium web browser, Wireshark, NetworkMiner, and other analyst tools. If you installed using our ISO image:

::

 sudo ~/SecurityOnion/setup/so-analyst
 
Otherwise, if you installed standard CentOS/Ubuntu and then cloned our github repo, then it's most likely:

::

 sudo ~/securityonion/setup/so-analyst

To connect from the Analyst VM to your manager node, you will need to run :ref:`so-allow` on the manager node and choose the ``analyst`` option to allow the traffic through the host-based :ref:`firewall`.
