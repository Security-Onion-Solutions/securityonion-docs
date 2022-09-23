.. _suricata:

Suricata
========

From https://suricata.io:

    Suricata is a free and open source, mature, fast and robust network threat detection engine. Suricata inspects the network traffic using
    a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats.

Suricata NIDS alerts can be found in :ref:`alerts`, :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. Here's an example of Suricata NIDS alerts in :ref:`alerts`:

.. image:: images/alerts.png
  :target: _images/alerts.png
  
If enabled, Suricata metadata (protocol logs) can be found in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`.

Community ID
------------

Security Onion enables Suricata's built-in support for :ref:`community-id`.

Performance
-----------

If Suricata is experiencing packet loss, then you may need to do one or more of the following: tune the ruleset (see the :ref:`managing-alerts` section), apply a :ref:`bpf`, adjust ``max-pending-packets`` in the Suricata configuration, or adjust :ref:`af-packet` workers.

To change the number of workers:

-  Stop sensor processes:

   ::

      sudo so-suricata-stop

-  Edit ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls`` and change the ``suriprocs`` variable to the desired number of workers.

-  Start sensor processes:

   ::

      sudo so-suricata-start

.. seealso::

    | For other tuning considerations, please see:
    | https://suricata.readthedocs.io/en/latest/performance/tuning-considerations.html

For best performance, Suricata should be pinned to specific CPUs. In most cases, you’ll want to pin sniffing processes to a CPU in the same Non-Uniform Memory Access (NUMA) domain that your sniffing NIC is bound to.  Accessing a CPU in the same NUMA domain is faster than across a NUMA domain.  

.. seealso::

    | For more information about determining NUMA domains using ``lscpu`` and ``lstopo``, please see:
    | https://github.com/brokenscripts/cpu_pinning
    
To pin Suricata workers to specific CPUs:

- Stop sensor processes:

  ::

     sudo so-suricata-stop
       
- Edit ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls`` and add the following under ``sensor:`` 

  ::
  
     suripins:  
       - <cpu_1>  
       - <cpu_2>  
       - <cpu_3> 

- Note: To avoid inconsistent Suricata workers being allocated, ensure ``suriprocs`` is removed from under ``sensor:`` or is equivalent to the number of cpu cores being pinned. 

- Start sensor processes:

  ::
  
     sudo so-suricata-start
     
Configuration
-------------

You can configure Suricata by going to :ref:`administration` --> Configuration --> suricata.

If you would like to configure/manage IDS rules, please see the :ref:`rules` and :ref:`managing-alerts` sections.

HOME_NET
--------

The HOME_NET variable defines the networks that are considered home networks (those networks that you are monitoring and defending). The default value is RFC1918 private address space (10.0.0.0/8, 192.168.0.0/16, and 172.16.0.0/12). You can modify this default value by going to :ref:`administration` --> Configuration --> suricata --> config --> vars --> address-groups --> HOME_NET.

EXTERNAL_NET
------------

By default, EXTERNAL_NET is set to ``any`` (which includes ``HOME_NET``) to detect lateral movement inside your environment. You can modify this default value by going to :ref:`administration` --> Configuration --> suricata --> config --> vars --> address-groups --> EXTERNAL_NET.

Thresholding
------------

To enable thresholding for SIDS, reference the example pillar at https://github.com/Security-Onion-Solutions/securityonion/blob/master/pillar/thresholding/pillar.example. 

To view the acceptable syntax, view the file located at https://github.com/Security-Onion-Solutions/securityonion/blob/master/pillar/thresholding/pillar.usage. 

This pillar can be added to :ref:`salt` in either the global pillar file (``/opt/so/saltstack/local/pillar/global.sls``) or minion pillar file (``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls``).

.. warning::

   Salt sls files are in YAML format. When editing these files, please be very careful to respect YAML syntax, especially whitespace. For more information, please see https://docs.saltproject.io/en/latest/topics/troubleshooting/yaml_idiosyncrasies.html.

Metadata
--------

Depending on what options you choose in Setup, it may ask if you want to use :ref:`zeek` or :ref:`suricata` for metadata. If you choose :ref:`suricata` and later find that some metadata is unnecessary, you can filter out the unnecessary metadata by writing rules. We have included some examples at https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/idstools/sorules/filters.rules.

The global pillar on your manager node controls the metadata engine on each sensor. Only one metadata engine at a time is supported.

To change your grid's metadata engine from Zeek to Suricata:

-  On the manager, edit the global pillar file (``/opt/so/saltstack/local/pillar/global.sls``) and change the ``mdengine`` variable from ``ZEEK`` to ``SURICATA``.

-  Stop Zeek on all nodes:

   ::

      sudo salt '*' cmd.run 'so-zeek-stop'

-  Update all nodes:

   ::

      sudo salt '*' state.highstate
      
-  You may need to remove ``so-zeek`` from ``/opt/so/conf/so-status/so-status.conf`` on each sensor node.

File Extraction
---------------

If you choose Suricata for metadata, it will extract files from network traffic and :ref:`strelka` will then analyze those extracted files. If you would like to extract additional file types, then you can add file types as shown at https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/idstools/sorules/extraction.rules.

Disabling
---------

Suricata can be disabled by setting ``enabled: false`` in the ``suricata`` :ref:`salt` pillar.

If you just want to disable Suricata on a single sensor, then you can edit that sensor's ``minion.sls`` file. If the file doesn't already have a ``suricata`` section, then add the following to the end of the file:

::

	suricata:
	  enabled: false

If you want to disable Suricata globally across all your sensors, then you could add that entry to your ``global.sls`` file.


Diagnostic Logging
------------------

If you need to troubleshoot Suricata, check ``/opt/so/log/suricata/suricata.log``. Depending on what you’re looking for, you may also need to look at the :ref:`docker` logs for the container:

::

	sudo docker logs so-suricata

Troubleshooting Alerts
----------------------

If you're not seeing the Suricata alerts that you expect to see, here are some things that you can check:

- If you have metadata enabled, check to see if you have metadata for the connections. Depending on your configuration, this could be Suricata metadata or :ref:`zeek` metadata.

- If you have metadata enabled but aren't seeing any metadata, then something may be preventing the process from seeing the traffic. Check to see if you have any :ref:`bpf` configuration that may cause the process to ignore the traffic. If you're sniffing traffic from the network, verify that the traffic is reaching the NIC using tcpdump. If importing a pcap file, verify that file contains the traffic you expect and that the Suricata process can read the file and any parent directories.

- Check your HOME_NET configuration to make sure it includes the networks that you're watching traffic for.

- Check to see if you have a full NIDS ruleset with rules that should specifically alert on the traffic and that those rules are enabled.

- Check to see if you have any threshold or suppression configuration that might be preventing alerts.

- Check the Suricata log for additional clues.

- Check the :ref:`filebeat`, :ref:`logstash`, and :ref:`elasticsearch` logs for any pipeline issues that may be preventing the alerts from being written to the ``so-ids`` indices.

- Try installing a simple import node (perhaps in a VM) following the steps in the :ref:`first-time-users` section and see if you get alerts there. If so, compare the working system to the non-working system and determine where the differences are.

Stats
-----

For detailed Suricata statistics, check ``/opt/so/log/suricata/stats.log``.

Testing Rules
-------------

To test a new rule, use the following utility on a node that runs Suricata (ie Forward or Import).

::

	sudo so-suricata-testrule <Filename> /path/to/pcap/test.pcap

The file should contain the new rule that you would like to test. The pcap should contain network data that will trigger the rule.

More Information
----------------

.. seealso::

    For more information about Suricata, please see https://suricata.io.
