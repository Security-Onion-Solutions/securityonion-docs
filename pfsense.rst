.. _pfsense:

pfSense
=======

pfSense is a free and open firewall that can be found at https://www.pfsense.org/. Security Onion has a couple of options for ingesting logs from pfSense firewalls: a simple parser and the more comprehensive Elastic Integration for pfSense.

Simple Parser
-------------

The first option is to use our simple parser for pfSense firewall logs. Please note that this only supports filterlog (actual firewall logs) and no other logs.

.. warning::

    This simple parser will be phased out over time in favor of the more comprehensive Elastic Integration for pfSense below.

To use the simple parser, first go to :ref:`administration` --> Configuration --> firewall --> hostgroups. 

.. image:: images/config-item-firewall.png
  :target: _images/config-item-firewall.png
   
Once there, select the ``syslog`` option, specify the IP address of the pfSense firewall, and click the checkmark to save. Then click the ``SYNCHRONIZE GRID`` button under the ``Options`` menu at the top of the page.
   
Next, configure your pfSense firewall to send syslog to the IP address of your Security Onion box. If you are using pfSense 2.6.0 or higher, make sure that ``Log Message Format`` is set to ``BSD (RFC 3164, default)``. 

You should then be able to search for your firewall logs in :ref:`dashboards` or :ref:`hunt`.

Elastic Integration for pfSense
-------------------------------

The second option is using the Elastic Integration for pfSense (https://docs.elastic.co/integrations/pfsense). This integration is more comprehensive than the simple parser above and supports more log types.

First, add the pfSense integration and configure the pfSense firewall:

#. Go to :ref:`elastic-fleet`, click the ``Agent policies`` tab, and then click the desired policy (for example ``so-grid-nodes_general``).
#. Click the ``Add integration`` button.
#. Search for ``pfSense`` and then click on the ``pfSense`` integration.
#. The Elastic Integration page will show instructions for configuring pfSense. Follow these instructions but please note that the Elastic Integration expects to receive pfSense logs on port 9001 by default.
#. Once you've configured pfSense, then go back to the Elastic screen and click the ``Add pfSense`` button.
#. On the ``Edit pfSense integration`` screen, go to the ``Syslog Host`` field and change ``localhost`` to ``0.0.0.0``.
#. Click the ``Save and continue`` button and then click ``Save and deploy changes``.

Next, we need to allow the traffic from the pfSense firewall to port 9001:

#. Navigate to :ref:`administration` --> Configuration.
#. At the top of the page, click the ``Options`` menu and then enable the ``Show all configurable settings, including advanced settings.`` option.
#. On the left side, go to ``firewall``, select ``hostgroups``, and click the ``customhostgroup0`` group. On the right side, enter the IP address of the pfSense firewall and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``portgroups``, select the ``customportgroup0`` group, and then click ``udp``. On the right side, enter ``9001`` and click the checkmark to save.
#. On the left side, go to ``firewall``, select ``role``, and then select the node type that will receive the pfSense logs. Then drill into ``chain`` --> ``INPUT`` --> ``hostgroups`` --> ``customhostgroup0`` --> ``portgroups``. On the right side, enter ``customportgroup0`` and click the checkmark to save.
#. If you would like to apply the rules immediately, click the ``SYNCHRONIZE GRID`` button under the ``Options`` menu at the top of the page.

Once all configuration is complete, you should be able to go to :ref:`dashboards` and select the Firewall dashboard to see your firewall logs.
