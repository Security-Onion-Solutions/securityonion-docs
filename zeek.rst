.. _zeek:

Zeek
====

Zeek is formerly known as Bro.  From https://www.zeek.org/:

    Zeek is a powerful network analysis framework that is much different from the typical IDS you may know. (Zeek is the new name for the long-established Bro system. Note that parts of the system retain the "Bro" name, and it also often appears in the documentation and distributions.)

Zeek logs are sent to :ref:`elasticsearch` for parsing and storage and can then be found in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. Here's an example of Zeek conn (connection) logs in :ref:`hunt`:

.. image:: images/hunt.png
  :target: _images/hunt.png
  
Community ID
------------

Security Onion enables Zeek's built-in support for :ref:`community-id`.

Packet Loss and Capture Loss
----------------------------

Zeek reports both packet loss and capture loss and you can find graphs of these in :ref:`grafana`. If Zeek reports packet loss, then you most likely need to adjust the number of Zeek workers as shown below or filter out traffic using :ref:`bpf`. If Zeek is reporting capture loss but no packet loss, this usually means that the capture loss is happening upstream in the tap or span port itself.

Configuration
-------------

You can configure Zeek by going to :ref:`administration` --> Configuration --> zeek. 

HOME_NET
--------

The HOME_NET variable defines the networks that are considered home networks (those networks that you are monitoring and defending). The default value is RFC1918 private address space (10.0.0.0/8, 192.168.0.0/16, and 172.16.0.0/12). You can modify this default value by going to :ref:`administration` --> Configuration --> zeek --> config --> networks --> HOME_NET.

Performance
-----------

Zeek uses :ref:`af-packet` so that you can spin up multiple Zeek workers to handle more traffic.  

If you have multiple physical CPUs, you’ll most likely want to pin sniffing processes to a CPU in the same Non-Uniform Memory Access (NUMA) domain that your sniffing NIC is bound to.  Accessing a CPU in the same NUMA domain is faster than across a NUMA domain.  

.. seealso::

    For more information about determining NUMA domains using ``lscpu`` and ``lstopo``, please see https://github.com/brokenscripts/cpu_pinning.

Syslog
------

To forward Zeek logs to an external syslog collector, please see the :ref:`syslog-output` section.

Logs
----

Zeek logs are stored in ``/nsm/zeek/logs``. They are collected by :ref:`filebeat`, parsed by and stored in :ref:`elasticsearch`, and viewable in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`.

We configure Zeek to output logs in JSON format. If you need to parse those JSON logs from the command line, you can use :ref:`jq`.

If you want to specify what Zeek logs are ingested, you can use :ref:`so-zeek-logs`.

Zeek monitors your network traffic and creates logs, such as:

conn.log
~~~~~~~~

-  TCP/UDP/ICMP connections

-  For more information, see:

https://docs.zeek.org/en/latest/scripts/base/protocols/conn/main.zeek.html#type-Conn::Info

dns.log
~~~~~~~

-  DNS activity

-  For more information, see:

https://docs.zeek.org/en/latest/scripts/base/protocols/dns/main.zeek.html#type-DNS::Info

ftp.log
~~~~~~~

-  FTP activity

-  For more information, see:

https://docs.zeek.org/en/latest/scripts/base/protocols/ftp/info.zeek.html#type-FTP::Info

http.log
~~~~~~~~

-  HTTP requests and replies

-  For more information, see:

https://docs.zeek.org/en/latest/scripts/base/protocols/http/main.zeek.html#type-HTTP::Info

ssl.log
~~~~~~~

-  SSL/TLS handshake info

-  For more information, see:

https://docs.zeek.org/en/latest/scripts/base/protocols/ssl/main.zeek.html#type-SSL::Info

notice.log
~~~~~~~~~~

-  Zeek notices

-  For more information, see:

https://docs.zeek.org/en/latest/scripts/base/frameworks/notice/main.zeek.html#type-Notice::Info

Other Zeek logs
~~~~~~~~~~~~~~~

Zeek also provides other logs by default and you can read more about them at https://docs.zeek.org/en/latest/script-reference/log-files.html.

In addition to Zeek's default logs, we also include protocol analyzers for STUN, TDS, and Wireguard traffic and several different ICS/SCADA protocols. By default, these analyzers are enabled and will log to the filesystem. For new installations, these logs are automatically ingested into Elasticsearch. If you upgrade an existing deployment and would like to ingest these logs, you can enable them via :ref:`so-zeek-logs`.

We also include MITRE BZAR scripts and you can read more about them at https://github.com/mitre-attack/bzar. Please note that the MITRE BZAR scripts are disabled by default. If you would like to enable them, you can add ``bzar`` to your ``global.sls`` as shown in the Custom Scripts section below.

As you can see, Zeek log data can provide a wealth of information to the analyst, all easily accessible through :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana`.

VLAN tags
---------

If you want to include VLAN tags in your conn.log, then you can enable the ``protocols/conn/vlan-logging`` script (already included in Zeek but disabled by default) in your Zeek configuration as shown in the Custom Scripts section below.

Intel
-----

You can add your own intel to ``/opt/so/saltstack/local/salt/zeek/policy/intel/intel.dat`` on the manager and it will automatically replicate to all forward nodes. If the ``/opt/so/saltstack/local/salt/zeek/policy/intel/`` directory is empty, you can copy the default files (both ``intel.dat`` and ``__load__.zeek``) from ``/opt/so/saltstack/default/salt/zeek/policy/intel/`` as follows:

::

    sudo cp /opt/so/saltstack/default/salt/zeek/policy/intel/* /opt/so/saltstack/local/salt/zeek/policy/intel/

Please note that Zeek is very strict about the format of ``intel.dat``. When editing this file, please follow these guidelines:

- no leading spaces or lines
- separate fields with a single literal tab character
- no trailing spaces or lines

The default ``intel.dat`` file follows these guidelines so you can reference it as an example of the proper format.

When finished editing ``intel.dat``, run ``sudo salt $SENSORNAME_$ROLE state.highstate`` to sync ``/opt/so/saltstack/local/salt/zeek/policy/intel/`` to ``/opt/so/conf/zeek/policy/intel/``. If you have a distributed deployment with separate forward nodes, it may take up to 15 minutes for intel to sync to the forward nodes.

If you experience an error, or do not notice ``/nsm/zeek/logs/current/intel.log`` being generated, try having a look in ``/nsm/zeek/logs/current/reporter.log`` for clues. You may also want to restart Zeek after making changes by running ``sudo so-zeek-restart``.

| For more information, please see:
| https://docs.zeek.org/en/latest/frameworks/intel.html\ 
| https://zeek.org/2014/01/23/intelligence-data-and-bro/\ 
| https://github.com/weslambert/securityonion-misp

Custom Scripts
--------------

Custom scripts can be added to ``/opt/so/saltstack/local/salt/zeek/policy/custom/<$custom-module>`` on the manager.  The custom folder is mapped to Zeek through Docker on the minions.  Once the script module is created, the configuration for ``local.zeek`` will need to be updated.  This configuration is abstracted into a :ref:`salt` pillar.  For example, we would copy the following into the ``global.sls`` file, replacing ``$module-name`` on the last line with the actual module name:

::

  zeek:
    local:
      '@load':
        - misc/loaded-scripts
        - tuning/defaults
        - misc/capture-loss
        - misc/stats
        - frameworks/software/vulnerable
        - frameworks/software/version-changes
        - protocols/ftp/software
        - protocols/smtp/software
        - protocols/ssh/software
        - protocols/http/software
        - protocols/dns/detect-external-names
        - protocols/ftp/detect
        - protocols/conn/known-hosts
        - protocols/conn/known-services
        - protocols/ssl/known-certs
        - protocols/ssl/validate-certs
        - protocols/ssl/log-hostcerts-only
        - protocols/ssh/geo-data
        - protocols/ssh/detect-bruteforcing
        - protocols/ssh/interesting-hostnames
        - protocols/http/detect-sqli
        - frameworks/files/hash-all-files
        - frameworks/files/detect-MHR
        - policy/frameworks/notice/extend-email/hostnames
        - ja3
        - hassh
        - intel
        - cve-2020-0601
        - securityonion/bpfconf
        - securityonion/communityid
        - securityonion/file-extraction
        - custom/$module-name
      
One the configuration has been updated, Zeek can be restarted with ``sudo so-zeek-restart`` on applicable nodes to pick up the changes.  Finally, ``/nsm/zeek/logs/current/loaded_scripts.log`` can be checked to ensure the new module has been loaded. For example:

::

    grep mynewmodule /nsm/zeek/logs/current/loaded_scripts.log
    
Custom Script Example: log4j
----------------------------

Corelight has developed a Zeek package to detect log4j exploitation attempts and it can be found at https://github.com/corelight/cve-2021-44228. This package contains Zeek scripts which can easily be loaded into your Security Onion deployment.

First, we need to make sure that the ``custom`` directory exists on the manager:

::

	sudo mkdir -p /opt/so/saltstack/local/salt/zeek/policy/custom/

Next, download the Zeek package to a temporary location:

::

	git clone https://github.com/corelight/cve-2021-44228.git

Now we need to move the Zeek scripts to the Zeek ``custom`` directory:

::

	sudo mv cve-2021-44228/scripts /opt/so/saltstack/local/salt/zeek/policy/custom/cve-2021-44228

Next, we need to configure Zeek to load the new scripts. If ``/opt/so/saltstack/local/pillar/global.sls`` does not already contain a ``zeek:`` section, then copy and paste the following at the end of the file (be careful when pasting to respect yaml indentation):

::

  zeek:
    local:
      '@load':
        - misc/loaded-scripts
        - tuning/defaults
        - misc/capture-loss
        - misc/stats
        - frameworks/software/vulnerable
        - frameworks/software/version-changes
        - protocols/ftp/software
        - protocols/smtp/software
        - protocols/ssh/software
        - protocols/http/software
        - protocols/dns/detect-external-names
        - protocols/ftp/detect
        - protocols/conn/known-hosts
        - protocols/conn/known-services
        - protocols/ssl/known-certs
        - protocols/ssl/validate-certs
        - protocols/ssl/log-hostcerts-only
        - protocols/ssh/geo-data
        - protocols/ssh/detect-bruteforcing
        - protocols/ssh/interesting-hostnames
        - protocols/http/detect-sqli
        - frameworks/files/hash-all-files
        - frameworks/files/detect-MHR
        - policy/frameworks/notice/extend-email/hostnames
        - ja3
        - hassh
        - intel
        - cve-2020-0601
        - securityonion/bpfconf
        - securityonion/communityid
        - securityonion/file-extraction
        - custom/cve-2021-44228

Within 15 minutes, :ref:`salt` should automatically restart Zeek where necessary. If you don't want to wait, you can manually restart Zeek with the following command. If you have a distributed deployment, you could run this command on each sensor manually or use :ref:`salt` to run the command across all sensors at once:

::

	sudo so-zeek-restart

Modifying base protocol scripts
-------------------------------

If you need to modify base protocol scripts, you can do so as follows. In this example, we are modifying the default ports that Zeek considers for the MySQL analyzer:

::

	const ports = { 11434/tcp, 13306/tcp };

	event zeek_init() &priority=5
		{
		Analyzer::register_for_ports(Analyzer::ANALYZER_MYSQL, ports);
		}
	
Diagnostic Logging
------------------

Zeek diagnostic logs can be found in ``/nsm/zeek/logs/``. Look for files like ``reporter.log``, ``stats.log``, ``stderr.log``, and ``stdout.log``. Depending on what you're looking for, you may also need to look at the :ref:`docker` logs for the container:

::

        sudo docker logs so-zeek

Disabling
---------

Zeek can be disabled by setting ``enabled: false`` in the ``zeek`` :ref:`salt` pillar.

If you just want to disable Zeek on a single sensor, then you can edit that sensor's ``minion.sls`` file. If the file doesn't already have a ``zeek`` section, then add the following to the end of the file:

::

	zeek:
	  enabled: false

If you want to disable Zeek globally across all your sensors, then you could add that entry to your ``global.sls`` file.

More Information
----------------

.. seealso::

    For more information about Zeek, please see https://www.zeek.org/.
