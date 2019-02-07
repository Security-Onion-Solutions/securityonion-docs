Best Practices
==============

Security Onion comes with the option to implement what is considered a
set of "best practices" during setup. For many users, this is a quick
and easy way to ensure you are configuring your deployment to disable
any services that you may not need, and that would otherwise duplicate
work and data. The **Best Practices** option not only disables these
unnecessary services, but (assuming the appropriate packages are
installed) enables
`Salt <https://github.com/Security-Onion-Solutions/security-onion/wiki/Salt>`__
by default, to allow for ease of sensor management.

**The below sections assume that you already have these services
installed, and provide advice on how to disable them in your
deployment.**

| Disable any unnecessary services. First, Snorby should be disabled
  since it is now considered unmaintained:
| https://github.com/Security-Onion-Solutions/security-onion/wiki/DisablingProcesses#disabling-snorby

In addition, most folks will want to disable the following services:

-  prads (prads creates session data and asset data, already provided by
   Bro)
-  pads\_agent (not needed if prads is disabled)
-  sancp\_agent (not needed if prads is disabled)
-  argus (argus creates session data, which is already provided by Bro)
-  http\_agent (duplicates Bro http.log into Sguil database, which may
   cause performance issues)

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

For more information, please see `Disabling
Processes <DisablingProcesses#disabling-a-process>`__.
