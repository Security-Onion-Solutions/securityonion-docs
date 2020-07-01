Disabling Processes
===================

If you've already run Setup and want to disable a certain sensor service, you can simply stop the running service and then change the corresponding config value from ``yes`` to ``no`` to prevent it from restarting the next time the NSM scripts are run.

For example, suppose you access Zeek's HTTP logs via Kibana, so you want to disable ``http_agent`` to prevent those HTTP logs from being duplicated into the ``Sguil`` database. You would first stop the running ``http_agent`` service:

::

    sudo nsm_sensor_ps-stop --only-http-agent

You would then edit ``/etc/nsm/$HOSTNAME-$INTERFACE/sensor.conf`` and change:

::

    HTTP_AGENT_ENABLED="yes"

to:

::

    HTTP_AGENT_ENABLED="no"

to prevent ``http_agent`` from restarting the next time the NSM scripts are run. A quick way to do this for all ``/etc/nsm/*/sensor.conf`` files on one box is to use the ``sed`` command as follows:

::

    sudo sed -i 's|HTTP_AGENT_ENABLED="yes"|HTTP_AGENT_ENABLED="no"|g' /etc/nsm/*/sensor.conf

Wazuh
-----

Occasionally, folks ask about disabling Wazuh.  Please keep in mind that in addition to providing endpoint visibility from Wazuh agents, the Wazuh server also monitors and protects the Security Onion box itself. For example, suppose that you have an active adversary who is trying to compromise your Security Onion box. Wazuh may see those attempts and engage ``Active Response`` to block the attacker's IP address in the host-based firewall.

If you understand all of this and still want to disable Wazuh, you can do so as follows:

::

    # Stop the running Wazuh processes 
    sudo so-ossec-stop

    # Disable Wazuh
    sudo update-rc.d -f ossec-hids-server disable

