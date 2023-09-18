.. _zeek:

Zeek
====

Security Onion includes Zeek for network protocol analysis and metadata.  From https://www.zeek.org/:

    Zeek is a powerful network analysis framework that is much different from the typical IDS you may know. (Zeek is the new name for the long-established Bro system. Note that parts of the system retain the "Bro" name, and it also often appears in the documentation and distributions.)

Zeek logs are sent to :ref:`elasticsearch` for parsing and storage and can then be found in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. Here's an example of Zeek logs in :ref:`hunt`:

.. image:: images/52_hunt.png
  :target: _images/52_hunt.png
  
Community ID
------------

Security Onion enables Zeek's built-in support for :ref:`community-id`.

Packet Loss and Capture Loss
----------------------------

Zeek reports both packet loss and capture loss and you can find graphs of these in :ref:`influxdb`. If Zeek reports packet loss, then you most likely need to adjust the number of Zeek workers as shown below or filter out traffic using :ref:`bpf`. If Zeek is reporting capture loss but no packet loss, this usually means that the capture loss is happening upstream in the tap or span port itself.

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

.. note::

    For more information about determining NUMA domains using ``lscpu`` and ``lstopo``, please see https://github.com/brokenscripts/cpu_pinning.

You can modify Zeek worker count by going to :ref:`administration` --> Configuration --> zeek --> config --> node --> workers.

Disabling
---------

Zeek can be disabled by going to :ref:`administration` --> Configuration --> zeek --> enabled.

Syslog
------

To forward Zeek logs to an external syslog collector, please see the :ref:`syslog-output` section.

Logs
----

Zeek logs are stored in ``/nsm/zeek/logs``. They are collected by :ref:`elastic-agent`, parsed by and stored in :ref:`elasticsearch`, and viewable in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`.

We configure Zeek to output logs in JSON format. If you need to parse those JSON logs from the command line, you can use :ref:`jq`.

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

In addition to Zeek's default logs, we also include protocol analyzers for STUN, TDS, and Wireguard traffic and several different ICS/SCADA protocols. These analyzers are enabled by default.

We also include MITRE BZAR scripts and you can read more about them at https://github.com/mitre-attack/bzar. Please note that the MITRE BZAR scripts are disabled by default. If you would like to enable them, you can do so via :ref:`administration` --> Configuration --> zeek. Once enabled, you can then check for BZAR detections by going to :ref:`dashboards` and selecting the Zeek Notice dashboard.

As you can see, Zeek log data can provide a wealth of information to the analyst, all easily accessible through :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana`.

VLAN Tags
---------

If your network traffic has VLAN tags, then Zeek will log them in conn.log. :ref:`dashboards` includes a VLAN dashboard which shows this data.

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

Diagnostic Logging
------------------

Zeek diagnostic logs can be found in ``/nsm/zeek/logs/``. Look for files like ``reporter.log``, ``stats.log``, ``stderr.log``, and ``stdout.log``. Depending on what you're looking for, you may also need to look at the :ref:`docker` logs for the container:

::

        sudo docker logs so-zeek

More Information
----------------

.. note::

    For more information about Zeek, please see https://www.zeek.org/.
