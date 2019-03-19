Best Practices
==============

Security Onion comes with the option to implement what is considered a set of ``Best Practices`` during Setup. For many users, this is a quick and easy way to ensure you are configuring your deployment to disable any services that you may not need, and that would otherwise duplicate work and data. The ``Best Practices`` option not only disables these unnecessary services, but (assuming the appropriate packages are installed) enables `Salt <Salt>`__ by default, to allow for ease of sensor management.

**The below sections assume that you already have these services installed, and provide advice on how to disable them in your deployment.**

Most folks will want to disable the following services:

-  prads (prads creates session data and asset data, already provided by Bro)
-  pads_agent (not needed if prads is disabled)
-  sancp_agent (not needed if prads is disabled)
-  argus (argus creates session data, which is already provided by Bro)
-  http_agent (duplicates Bro http.log into Sguil database, which may cause performance issues)

To do so, stop the required service/s:

::

    sudo nsm_sensor_ps-stop --only-prads
    sudo nsm_sensor_ps-stop --only-pads-agent
    sudo nsm_sensor_ps-stop --only-sancp-agent
    sudo nsm_sensor_ps-stop --only-argus
    sudo nsm_sensor_ps-stop --only-http-agent

And then disable them so they don't start on reboot:

::

    sudo sed -i 's|PRADS_ENABLED="yes"|PRADS_ENABLED="no"|g' /etc/nsm/*/sensor.conf
    sudo sed -i 's|PADS_AGENT_ENABLED="yes"|PADS_AGENT_ENABLED="no"|g' /etc/nsm/*/sensor.conf
    sudo sed -i 's|SANCP_AGENT_ENABLED="yes"|SANCP_AGENT_ENABLED="no"|g' /etc/nsm/*/sensor.conf
    sudo sed -i 's|ARGUS_ENABLED="yes"|ARGUS_ENABLED="no"|g' /etc/nsm/*/sensor.conf
    sudo sed -i 's|HTTP_AGENT_ENABLED="yes"|HTTP_AGENT_ENABLED="no"|g' /etc/nsm/*/sensor.conf

For more information, please see the `Disabling Processes <DisablingProcesses#disabling-a-process>`__ section.
