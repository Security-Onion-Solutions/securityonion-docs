.. _netflow:

NetFlow
=======

You may have devices on your network such as firewalls, routers, and switches that are capable of exporting NetFlow records. If you would like to collect these NetFlow records, add the Elastic Agent integration for ``NetFlow Records`` and then allow the Netflow traffic through the firewall.

First, add the ``NetFlow Records`` integration (https://docs.elastic.co/en/integrations/netflow):

#. Go to :ref:`elastic-fleet`, click the ``Agent policies`` tab, and then click the desired policy (for example ``so-grid-nodes_general``).
#. Click the ``Add integration`` button.
#. Search for ``netflow`` and then click on the ``NetFlow Records`` integration.
#. The Elastic Integration page will show an overview of the NetFlow Integration. Review all information on the page and then click the `Add NetFlow Records`` button.
#. On the ``Add NetFlow Records integration`` screen, go to the ``UDP host to listen on`` field and change ``localhost`` to ``0.0.0.0``. Verify the ``UDP port to listen on`` field matches what your NetFlow exporter will be sending to. Click the ``Save and continue`` button and then click ``Save and deploy changes``.

Next, allow the traffic from the NetFlow exporter to the NetFlow listener port. These instructions assume that this is the first firewall change you have made and therefore refer to ``customhostgroup0`` and ``customportgroup0``. If those have already been used, select the next available hostgroup and portgroup.

#. Navigate to :ref:`administration` --> Configuration.
#. At the top of the page, click the ``Options`` menu and then enable the ``Show all configurable settings, including advanced settings.`` option.
#. On the left side, go to ``firewall``, select ``hostgroups``, and click the ``customhostgroup0`` group. On the right side, enter the IP address of the NetFlow exporter and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``portgroups``, select the ``customportgroup0`` group, and then click ``udp``. On the right side, enter your desired NetFlow listener port (UDP 2055 by default) and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``role``, and then select the node type that will receive the NetFlow records. Then drill into ``chain`` --> ``INPUT`` --> ``hostgroups`` --> ``customhostgroup0`` --> ``portgroups``. On the right side, enter ``customportgroup0`` and click the checkmark to save.
#. If you would like to apply the rules immediately, click the ``SYNCHRONIZE GRID`` button under the ``Options`` menu at the top of the page.

Once all configuration is complete, you should be able to go to :ref:`dashboards` and select the ``NetFlow`` dashboard to see your NetFlow records.
