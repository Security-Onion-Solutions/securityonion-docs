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

For best performance, Suricata processes should be pinned to specific CPUs. In most cases, you’ll want to pin sniffing processes to the same CPU that your sniffing NIC is bound to. You can use the affinity settings in ``suricata.yaml`` as shown in https://suricata.readthedocs.io/en/latest/configuration/suricata-yaml.html#threading.

Also see https://suricata.readthedocs.io/en/latest/performance/tuning-considerations.html.

Community ID
------------

We enable Suricata's native support for :ref:`community-id`.

Configuration
-------------

You can configure Suricata's ``suricata.yaml`` using :ref:`salt`. The defaults for this have been defined in https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/suricata/defaults.yaml. Under ``suricata:config``, the pillar structure follows the same YAML structure of the ``suricata.yaml`` file. For some of the settings to modify here, we have simplified the pillar configuration by placing the option in the sensor pillar instead of the Suricata pillar. These options are: ``HOMENET``, ``default-packet-size``, and the CPU affinity settings for pinning the processes to CPU cores or how many processes to run.

If you would like to configure/manage IDS rules, please see the :ref:`rules` and :ref:`managing-alerts` sections.

Thresholding
------------

To enable thresholding for SIDS, reference the example pillar at https://github.com/Security-Onion-Solutions/securityonion/blob/master/pillar/thresholding/pillar.example. 

To view the acceptable syntax, view the file located at https://github.com/Security-Onion-Solutions/securityonion/blob/master/pillar/thresholding/pillar.usage. 

This pillar can be added to :ref:`salt` in either the global pillar file (``/opt/so/saltstack/local/pillar/global.sls``) or minion pillar file (``/opt/so/saltstack/local/pillar/minions/<minionid>.sls``).

Logging
-------

If you need to troubleshoot Suricata, check ``/opt/so/log/suricata/suricata.log``.

Stats
-----

For detailed Suricata statistics, check ``/opt/so/log/suricata/stats.log``.

More Information
----------------

.. seealso::

    For more information about Suricata, please see https://suricata-ids.org.
