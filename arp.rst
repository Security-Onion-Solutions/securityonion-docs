.. _arp:

ARP Visibility
==============

Most enterprise deployments are monitoring network traffic from a choke point where the only ARP/MAC traffic seen would be firewalls and routers and not actual endpoint devices. However, if you are monitoring network traffic from a location where you can view actual endpoint ARP traffic, then you can enable ARP/MAC ingestion as follows.

By default, our :ref:`zeek` configuration should be writing ARP and MAC data to ``/nsm/zeek/logs/current/ecat_arp_info.log``. However, this log is not ingested into :ref:`elasticsearch` by default.

To ingest the data into :ref:`elasticsearch`, go to your :ref:`zeek` excluded configuration as shown in the :ref:`zeek` configuration section, remove ``ecat_arp_info`` from the list, and save the configuration. Wait 15 minutes for the configuration to take effect or force it immediately.

Once this data is flowing into :ref:`elasticsearch`, you should be able to go to :ref:`dashboards` and paste the following for a simple MAC address dashboard:

        ::
        
                tags:ecat_arp_info | groupby source.mac | groupby -sankey source.mac ecat.arp.type | groupby ecat.arp.type | groupby -sankey ecat.arp.type destination.mac | groupby destination.mac

If you want to see the MAC/IP relationships as well:

        ::

                tags:ecat_arp_info | groupby source.ip | groupby -sankey source.ip source.mac | groupby source.mac | groupby -sankey source.mac ecat.arp.type | groupby ecat.arp.type | groupby -sankey ecat.arp.type destination.mac | groupby destination.mac | groupby -sankey destination.mac destination.ip | groupby destination.ip
