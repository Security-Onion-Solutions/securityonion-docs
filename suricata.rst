.. _suricata:

Suricata
========

From https://suricata-ids.org:

    Suricata is a free and open source, mature, fast and robust network threat detection engine. Suricata inspects the network traffic using
    a powerful and extensive rules and signature language, and has powerful Lua scripting support for detection of complex threats.

Suricata NIDS alerts can be found in :ref:`alerts`, :ref:`hunt`, and :ref:`kibana`. Here's an example of Suricata NIDS alerts in :ref:`alerts`:

.. image:: images/alerts.png
  :target: _images/alerts.png
  
If enabled, Suricata metadata (protocol logs) can be found in :ref:`hunt` and :ref:`kibana`.

Community ID
------------

Security Onion enables Suricata's native support for :ref:`community-id`.

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

You can configure Suricata's ``suricata.yaml`` using :ref:`salt`. The defaults for this have been defined in https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/suricata/defaults.yaml. Under ``suricata:config``, the pillar structure follows the same YAML structure of the ``suricata.yaml`` file. 

For example, suppose you want to change Suricata's ``EXTERNAL_NET`` setting from the default of ``any`` to ``!$HOME_NET``. You could add the following to the global pillar file (``/opt/so/saltstack/local/pillar/global.sls``) or minion pillar file (``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls``) on the manager:

::

    suricata:
      config:
        vars:
          address-groups:
            EXTERNAL_NET: "!$HOME_NET"
            
From the manager, then run:

::

    sudo salt $SENSORNAME_$ROLE state.highstate

Some of the settings normally found in ``suricata.yaml`` can be found in the sensor pillar instead of the Suricata pillar. These options are: ``HOMENET``, ``default-packet-size``, and the CPU affinity settings for pinning the processes to CPU cores or how many processes to run.

If you would like to configure/manage IDS rules, please see the :ref:`rules` and :ref:`managing-alerts` sections.

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

File Extraction
---------------

If you choose Suricata for metadata, it will extract files from network traffic and :ref:`strelka` will then analyze those extracted files. If you would like to extract additional file types, then you can add file types as shown at https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/idstools/sorules/extraction.rules.

Diagnostic Logging
------------------

If you need to troubleshoot Suricata, check ``/opt/so/log/suricata/suricata.log``.

Stats
-----

For detailed Suricata statistics, check ``/opt/so/log/suricata/stats.log``.

More Information
----------------

.. seealso::

    For more information about Suricata, please see https://suricata-ids.org.
