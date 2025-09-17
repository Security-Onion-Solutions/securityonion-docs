.. _unifi:

UniFi
=====

If you have UniFi firewalls on your network, you can send their logs to Security Onion. Typically, UniFi firewalls can send two different kinds of logs. The first is iptables firewall logs and the second is system logs in CEF format. To get all of these logs into :ref:`elasticsearch`, you'll need to add the Elastic integrations for iptables and CEF, configure the UniFi device to send those logs, and then configure the Security Onion firewall to allow those logs.

Add the iptables and CEF integrations
-------------------------------------

First, add the Elastic integrations for iptables and CEF.

.. note::

        For more information about the iptables integration, see:
        https://www.elastic.co/docs/reference/integrations/iptables
        
        For more information about the CEF integration, see:
        https://www.elastic.co/docs/reference/integrations/cef

#. Go to :ref:`elastic-fleet`, click the ``Agent policies`` tab, and then click the desired policy (for example ``so-grid-nodes_general``).
#. Click the ``Add integration`` button.
#. Search for ``iptables`` and then click on the ``iptables`` integration.
#. The Elastic Integration page will show an overview of the iptables Integration. Review all information on the page and then click the ``Add iptables`` button.
#. On the ``Add iptables integration`` screen, disable the options labeled ``Collect iptables application logs (input: logfile)`` and ``Collect iptables application logs (input: journald)``. Make sure that ``Collect iptables application logs (input: udp)`` is enabled and then change the ``Syslog host`` setting from ``localhost`` to ``0.0.0.0``. The ``Syslog Port`` should be set to ``9001`` by default. Click the ``Save and continue`` button and then click ``Save and deploy changes``.
#. Back at the desired policy screen, click the ``Add integration`` button.
#. Search for ``cef`` and then click on the ``Common Event Format (CEF)`` integration.
#. The Elastic Integration page will show an overview of the CEF Integration. Review all information on the page and then click the ``Add Common Event Format (CEF)`` button.
#. On the ``Add Common Event Format (CEF) integration`` screen, disable the options labeled ``Collect CEF application logs (input: logfile)`` and ``Collect CEF application logs (input: tcp)``.  Make sure that ``Collect CEF application logs (input: udp)`` is enabled and then change the ``Syslog Host`` setting from ``localhost`` to ``0.0.0.0``. The ``Syslog Port`` should be set to ``9003`` by default. Click the ``Save and continue`` button and then click ``Save and deploy changes``.

Configure UniFi
---------------

Next, configure UniFi to send both types of logs to Security Onion.

.. note::

        UniFi configuration may be different depending on what specific UniFi device you have and what software it is running. These instructions are based on a Cloud Gateway Fiber device running control plane version 4.2.12 and Network application version 9.3.43.

To configure UniFi to send iptables firewall logs to the Elastic integration for iptables:

#. In the UniFi web interface, navigate to Settings --> CyberSecure --> Traffic Logging.
#. Next to ``Activity Logging (Syslog)``, choose the ``SIEM Server`` option.
#. Set the ``Server Address`` to the IP address of the Security Onion node to send the logs to.
#. Set the ``Port`` to 9001.
#. Click the ``Apply Changes`` button.

To configure UniFi to send system logs to the Elastic integration for CEF:

#. In the UniFi web interface, navigate to Settings --> Control Plane --> Integrations.
#. Next to ``Activity Logging (Syslog)``, choose the ``SIEM Server`` option.
#. Set the ``Server Address`` to the IP address of the Security Onion node to send the logs to.
#. Set the ``Port`` to 9003.
#. Click the ``Apply Changes`` button.

While in UniFI, check your UniFi firewall rules and update if necessary:

#. In the UniFi web interface, navigate to Settings --> Policy Engine.
#. For any firewall rule that you want to see in Security Onion, make sure that ``Syslog Logging`` is enabled and the description starts with either ``Block`` or ``Allow``.

Allow UniFi logs through Security Onion firewall
------------------------------------------------

Finally, allow the traffic from the UniFi device through the Security Onion firewall to the Elastic integration ports.

.. note::

   The following instructions assume that this is the first firewall change you have made and therefore refer to ``customhostgroup0`` and ``customportgroup0``. If those have already been used, you can select the next available hostgroup and portgroup.

#. Navigate to :ref:`administration` --> Configuration.
#. At the top of the page, click the ``Options`` menu and then enable the ``Show advanced settings`` option.
#. On the left side, go to ``firewall``, select ``hostgroups``, and click the ``customhostgroup0`` group. On the right side, enter the IP address of the UniFi host and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``portgroups``, select the ``customportgroup0`` group, and then click ``udp``. On the right side, enter ``9001`` and ``9003`` and then click the checkmark to save.
#. On the left side, go to ``firewall``, select ``role``, and then select the node type that will receive the UniFi logs. Then drill into ``chain`` --> ``INPUT`` --> ``hostgroups`` --> ``customhostgroup0`` --> ``portgroups``. On the right side, enter ``customportgroup0`` and click the checkmark to save.
#. If you would like to apply the rules immediately, click the ``SYNCHRONIZE GRID`` button under the ``Options`` menu at the top of the page.

UniFi dashboards
----------------

Once all configuration is complete, you should be able to go to :ref:`dashboards` and select one of the ``Firewall - UniFi`` dashboards to see your UniFi logs.
