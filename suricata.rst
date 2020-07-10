.. _suricata:

Suricata
========

From https://suricata-ids.org:

    Suricata is a free and open source, mature, fast and robust network threat detection engine. Suricata inspects the network traffic using
    a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats.

Performance
-----------

Suricata uses :ref:`af-packet` to allow you to spin up multiple workers to handle more traffic.  

To change the number of Suricata workers:

-  Stop sensor processes:

   ::

      sudo so-suricata-stop

-  Edit ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls`` and change the ``suriprocs`` variable to the desired number of workers.

-  Start sensor processes:

   ::

      sudo so-suricata-start

-  ``so-suricata-start`` automatically copies ``$IDS_LB_PROCS`` into ``suricata.yaml`` and then Suricata creates the appropriate number of AF-PACKET workers.

For best performance, Suricata processes should be pinned to specific CPUs. In most cases, you’ll want to pin sniffing processes to the same CPU that your sniffing NIC is bound to. You can use the affinity settings in ``suricata.yaml`` as shown in https://suricata.readthedocs.io/en/latest/configuration/suricata-yaml.html#threading.

Also see https://suricata.readthedocs.io/en/latest/performance/tuning-considerations.html.

Community ID
------------

We enable Suricata's native support for :ref:`community-id`.

Configuration
-------------

You can configure Suricata in the :ref:`salt` pillar.

If you would like to configure/manage IDS rules, please see the :ref:`rules` and :ref:`alerts` sections.

Logging
-------

If you need to troubleshoot Suricata, check ``/opt/so/log/suricata/suricata.log``.

Stats
-----

For detailed Suricata statistics, check ``/opt/so/log/suricata/stats.log``.

More Information
----------------

For more information about Suricata, please see https://suricata-ids.org.
