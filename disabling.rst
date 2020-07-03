Disabling Processes
===================

If you've already run Setup and want to disable a certain sensor service, you can simply stop the running service and then change the corresponding config value from ``yes`` to ``no`` to prevent it from restarting the next time the NSM scripts are run.

Wazuh
-----

Occasionally, folks ask about disabling Wazuh.  Please keep in mind that in addition to providing endpoint visibility from Wazuh agents, the Wazuh server also monitors and protects the Security Onion box itself. For example, suppose that you have an active adversary who is trying to compromise your Security Onion box. Wazuh may see those attempts and engage ``Active Response`` to block the attacker's IP address in the host-based firewall.

If you understand all of this and still want to disable Wazuh, you can do so as follows:

::

    # Stop the running Wazuh processes 
    sudo so-ossec-stop

    # Disable Wazuh
    sudo update-rc.d -f ossec-hids-server disable

