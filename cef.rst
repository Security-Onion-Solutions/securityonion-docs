.. _cef:

CEF
===

If you have devices on your network that can send logs in CEF format, you can send those logs to Security Onion. To get those CEF logs into :ref:`elasticsearch`, you'll need to add the Elastic integration for CEF and then configure the Security Onion firewall to allow the remote device to send its logs.

Add the CEF integration
-----------------------

First, add the Elastic integration for ``CEF``.

.. note::

   For more information about the ``CEF`` integration, please see https://www.elastic.co/docs/reference/integrations/cef.

#. Go to :ref:`elastic-fleet`, click the ``Agent policies`` tab, and then click the desired policy (for example ``so-grid-nodes_general``).
#. Click the ``Add integration`` button.
#. Search for ``cef`` and then click on the ``Common Event Format (CEF)`` integration.
#. The Elastic Integration page will show an overview of the CEF Integration. Review all information on the page and then click the ``Add Common Event Format (CEF)`` button.
#. On the ``Add Common Event Format (CEF) integration`` screen, disable the options labeled ``Collect CEF application logs (input: logfile)`` and ``Collect CEF application logs (input: tcp)``.  Make sure that ``Collect CEF application logs (input: udp)`` is enabled and then change the ``Syslog Host`` setting from ``localhost`` to ``0.0.0.0``. The ``Syslog Port`` should be set to ``9003`` by default. Click the ``Save and continue`` button and then click ``Save and deploy changes``.

Allow CEF logs through firewall
-------------------------------

Next, allow the traffic from the CEF host through the firewall to the CEF integration port. 

.. note::

   The following instructions assume that this is the first firewall change you have made and therefore refer to ``customhostgroup0`` and ``customportgroup0``. If those have already been used, you can select the next available hostgroup and portgroup.

#. Navigate to :ref:`administration` --> Configuration.
#. At the top of the page, click the ``Options`` menu and then enable the ``Show advanced settings`` option.
#. On the left side, go to ``firewall``, select ``hostgroups``, and click the ``customhostgroup0`` group. On the right side, enter the IP address of the CEF host and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``portgroups``, select the ``customportgroup0`` group, and then click ``udp``. On the right side, enter your desired listener port (9003 by default) and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``role``, and then select the node type that will receive the CEF logs. Then drill into ``chain`` --> ``INPUT`` --> ``hostgroups`` --> ``customhostgroup0`` --> ``portgroups``. On the right side, enter ``customportgroup0`` and click the checkmark to save.
#. If you would like to apply the rules immediately, click the ``SYNCHRONIZE GRID`` button under the ``Options`` menu at the top of the page.

CEF dashboard
-------------

Once all configuration is complete, you should be able to go to :ref:`dashboards` and select the ``CEF`` dashboard to see your iptables logs.

