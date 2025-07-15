.. _iptables:

iptables
========

If you have Linux iptables firewalls on your network, you can send those logs to Security Onion. To get those iptables logs into :ref:`elasticsearch`, you'll need to add the Elastic integration for iptables and then configure the Security Onion firewall to allow the remote firewall to send its logs.

Add the iptables integration
----------------------------

First, add the Elastic integration for ``iptables``.

.. note::

   For more information about the ``iptables`` integration, please see https://www.elastic.co/docs/reference/integrations/iptables.

#. Go to :ref:`elastic-fleet`, click the ``Agent policies`` tab, and then click the desired policy (for example ``so-grid-nodes_general``).
#. Click the ``Add integration`` button.
#. Search for ``iptables`` and then click on the ``iptables`` integration.
#. The Elastic Integration page will show an overview of the iptables Integration. Review all information on the page and then click the ``Add iptables`` button.
#. On the ``Add iptables integration`` screen, disable the options labeled ``Collect iptables application logs (input: logfile)`` and ``Collect iptables application logs (input: journald)``. Make sure that ``Collect iptables application logs (input: udp)`` is enabled and then change the ``Syslog host`` setting from ``localhost`` to ``0.0.0.0``. The ``Syslog Port`` should be set to ``9001`` by default. Click the ``Save and continue`` button and then click ``Save and deploy changes``.

Allow iptables logs through firewall
------------------------------------

Next, allow the traffic from the iptables host through the firewall to the iptables integration port. 

.. note::

   The following instructions assume that this is the first firewall change you have made and therefore refer to ``customhostgroup0`` and ``customportgroup0``. If those have already been used, you can select the next available hostgroup and portgroup.

#. Navigate to :ref:`administration` --> Configuration.
#. At the top of the page, click the ``Options`` menu and then enable the ``Show advanced settings`` option.
#. On the left side, go to ``firewall``, select ``hostgroups``, and click the ``customhostgroup0`` group. On the right side, enter the IP address of the iptables host and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``portgroups``, select the ``customportgroup0`` group, and then click ``udp``. On the right side, enter your desired listener port (9001 by default) and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``role``, and then select the node type that will receive the iptables logs. Then drill into ``chain`` --> ``INPUT`` --> ``hostgroups`` --> ``customhostgroup0`` --> ``portgroups``. On the right side, enter ``customportgroup0`` and click the checkmark to save.
#. If you would like to apply the rules immediately, click the ``SYNCHRONIZE GRID`` button under the ``Options`` menu at the top of the page.

iptables dashboard
------------------

Once all configuration is complete, you should be able to go to :ref:`dashboards` and select the ``Firewall - iptables`` dashboard to see your iptables logs.

