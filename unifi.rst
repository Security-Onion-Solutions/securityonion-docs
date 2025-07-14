.. _unifi:

UniFi
=====

If you have UniFi firewalls on your network, you can send their logs to Security Onion. Typically, UniFi firewalls have two different kinds of logs. The first is standard :ref:`iptables` firewall logs. The second is system logs in :ref:`cef` format. To get all of these logs into :ref:`elasticsearch`, you'll need to add the Elastic integrations for :ref:`iptables` and :ref:`cef` and then configure the Security Onion firewall to allow the remote device to send both types of logs.

Add the CEF and iptables integrations
-------------------------------------

First, add the Elastic integration for ``CEF``.

.. note::

   For more information about the ``CEF`` integration, please see https://www.elastic.co/docs/reference/integrations/cef.

#. Go to :ref:`elastic-fleet`, click the ``Agent policies`` tab, and then click the desired policy (for example ``so-grid-nodes_general``).
#. Click the ``Add integration`` button.
#. Search for ``cef`` and then click on the ``CEF`` integration.
#. The Elastic Integration page will show an overview of the CEF Integration. Review all information on the page and then click the ``Add CEF`` button.
#. On the ``Add CEF integration`` screen, go to the ``UDP host to listen on`` field and change ``localhost`` to ``0.0.0.0``. Check the ``UDP port to listen on`` field and update if necessary. Click the ``Save and continue`` button and then click ``Save and deploy changes``.

Next, add the Elastic integration for ``iptables``.

.. note::

   For more information about the ``iptables`` integration, please see https://www.elastic.co/docs/reference/integrations/iptables.

#. Go to :ref:`elastic-fleet`, click the ``Agent policies`` tab, and then click the desired policy (for example ``so-grid-nodes_general``).
#. Click the ``Add integration`` button.
#. Search for ``iptables`` and then click on the ``iptables`` integration.
#. The Elastic Integration page will show an overview of the iptables Integration. Review all information on the page and then click the ``Add iptables`` button.
#. On the ``Add iptables integration`` screen, go to the ``UDP host to listen on`` field and change ``localhost`` to ``0.0.0.0``. Check the ``UDP port to listen on`` field and update if necessary. Click the ``Save and continue`` button and then click ``Save and deploy changes``.

Allow UniFi logs through firewall
---------------------------------

Next, allow the traffic from the UniFi device through the firewall to the Elastic integration ports.

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

Once all configuration is complete, you should be able to go to :ref:`dashboards` and select one of the ``Firewall - UniFi`` dashboards to see your UniFi logs. Please note that these dashboards assume that your firewall rules start with either ``Block`` or ``Allow`` in the description. Also note that you may need to manually enable logging on your firewall rules.
