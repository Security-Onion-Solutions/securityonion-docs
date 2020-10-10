.. _zeek:

Zeek
====

Zeek is formerly known as Bro.  From https://www.zeek.org/:

    Zeek is a powerful network analysis framework that is much different from the typical IDS you may know. (Zeek is the new name for the long-established Bro system. Note that parts of the system retain the "Bro" name, and it also often appears in the documentation and distributions.)

Zeek logs are sent to :ref:`elasticsearch` for parsing and storage and can then be found in :ref:`hunt` and :ref:`kibana`.

Zeek logs in :ref:`hunt`:

.. image:: https://user-images.githubusercontent.com/1659467/95373696-56957f80-08ab-11eb-9ccd-4b8632bd7470.png
  :target: https://user-images.githubusercontent.com/1659467/95373696-56957f80-08ab-11eb-9ccd-4b8632bd7470.png
  
Community ID
------------

Security Onion enables Zeek's native support for :ref:`community-id`.

Performance
-----------

Zeek uses :ref:`af-packet` so that you can spin up multiple Zeek workers to handle more traffic.  

To change the number of AF-PACKET workers for :ref:`zeek`:

-  Stop Zeek:

   ::

      sudo so-zeek-stop

-  Edit ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls`` and change the ``zeek_lbprocs`` variable to the desired number of cores.

-  Start Zeek:

   ::

      sudo so-zeek-start
      
For best performance, Zeek should be pinned to specific CPUs. In most cases, you’ll want to pin sniffing processes to the same CPU that your sniffing NIC is bound to.  You can do this using the ``pin_cpus`` setting as shown at https://docs.zeek.org/en/stable/configuration/#using-pf-ring.

Email
-----

To configure email notifications, please see the :ref:`email` section.

Syslog
------

To forward Zeek logs to an external syslog collector, please see the :ref:`syslog-output` section.

Intel
-----

You can add your own Intel to ``/opt/so/saltstack/local/salt/zeek/policy/intel/intel.dat``. When writing this file, ensure there are no leading/trailing spaces or lines, and that only a single tab is used to separate fields. If you experience an error, or do not notice ``/nsm/zeek/logs/current/intel.log`` being generated, try having a look in ``/nsm/zeek/logs/current/reporter.log`` for clues. You may also want to restart Zeek after making changes by running ``sudo so-zeek-restart``.

For more information, please see:

| https://docs.zeek.org/en/latest/frameworks/intel.html\ 
| http://blog.bro.org/2014/01/intelligence-data-and-bro_4980.html\ 
| https://github.com/weslambert/securityonion-misp

Custom Scripts
--------------

Custom scripts can be added to ``/opt/so/conf/zeek/``.

Logs
----

Zeek logs are stored in ``/nsm/zeek/logs``. They are collected by :ref:`filebeat`, parsed by and stored in :ref:`elasticsearch`, and viewable in :ref:`hunt` and :ref:`kibana`.

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

| ...and others, which can be researched here:
| https://docs.zeek.org/en/latest/script-reference/log-files.html

As you can see, Zeek log data can provide a wealth of information to the analyst, all easily accessible through :ref:`hunt` or :ref:`kibana`.

Configuration
-------------
You can use :ref:`salt` to manage Zeek's ``local.zeek``, ``node.cfg`` and ``zeekctl.cfg``:
 
``local.zeek``: The allowed options for this file are ``@load``, ``@load-sigs`` and ``redef``. An example of configuring this pillar can be seen below. 
 
``node.cfg``: The pillar items to modify this file are located under the sensor pillar in the minion pillar file. The options that can be customized in the file include: ``interface``, ``lb_procs``, ``pin_cpus``, and ``af_packet_buffer_size``.
 
``zeekctl.cfg``: An example of customizing this can be seen below. The allowed options can be seen in https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/zeek/files/zeekctl.cfg.jinja.

Here is an example of how we would modify ``local.zeek``. We can see the default pillar assignments used for ``local.zeek`` in ``/opt/so/saltstack/default/pillar/zeek/init.sls``. This file should never be modified as it could be updated in the future and any modification made would be overwritten. The global or minion pillar files should be used for making changes as they are stored in ``/opt/so/saltstack/local/``, and that directory isn’t overwritten during a Security Onion code update.

::

   zeek:
     zeekctl:
       MailTo: root@localhost
       MailConnectionSummary: 1
       MinDiskSpace: 5
       MailHostUpDown: 1
       LogRotationInterval: 3600
       LogExpireInterval: 0
       StatsLogEnable: 1
       StatsLogExpireInterval: 0
       StatusCmdShowAll: 0
       CrashExpireInterval: 0
       SitePolicyScripts: local.zeek
       LogDir: /nsm/zeek/logs
       SpoolDir: /nsm/zeek/spool
       CfgDir: /opt/zeek/etc
       CompressLogs: 1
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
       '@load-sigs':
         - frameworks/signatures/detect-windows-shells
       redef:
         - LogAscii::use_json = T;
         - LogAscii::json_timestamps = JSON::TS_ISO8601;

In this file, there are two keys under zeek, ``zeekctl`` and ``local``. We will be using ``zeek:local`` for this example since we are modifying the ``zeek.local`` file. We will address ``zeek:zeekctl`` in another example where we modify the ``zeekctl.cfg`` file. 

Under ``zeek:local``, there are three keys: ``@load``, ``@load-sigs``, and ``redef``. In the pillar definition, ``@load`` and ``@load-sigs`` are wrapped in quotes due to the ``@`` character. Under each of the keys, there is a list of  items that will be added to the ``local.zeek`` file with the appropriate directive of either ``@load``, ``@load-sigs`` or ``redef``. In order to modify either of the lists, the entire list must redefined in either the global or minion pillar file.

If we have a node where ``protocols/ssh/detect-bruteforcing`` is generating a lot of noise and we want to tell Zeek to stop loading that script, we would do the following. Since we just want to turn it off for that specific node, we would open ``/opt/so/saltstack/local/pillar/minions/<minionid>.sls``. At the bottom, we would append the following:

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

We redefined the ``@load`` list in the minion pillar file, but we left out the ```protocols/ssh/detect-bruteforcing``. This will override the value defined in the ``/opt/so/saltstack/default/pillar/zeek/init.sls`` and the global pillar file if it is defined there, and prevent the script from being added to the ``local.zeek`` file. If we wanted to add a script to be loaded, then we would add out script to the list. Since we aren’t changing ``@load-sigs`` or ``redef``, then we do not need to add them here. Once the file is saved, and the node checks in the with manager, the ``local.zeek`` file will be updated and the ``so-zeek`` docker container will be restarted.

Let's see an example of how we would modify the ``zeekctl.cfg`` file. From the example above, we know that the default pillar values are set for zeek in ``/opt/so/saltstack/default/pillar/zeek/init.sls``. The default pillar values for ``zeekctl.cfg`` are as follows:

::

   zeek:
     zeekctl:
       MailTo: root@localhost
       MailConnectionSummary: 1
       MinDiskSpace: 5
       MailHostUpDown: 1
       LogRotationInterval: 3600
       LogExpireInterval: 0
       StatsLogEnable: 1
       StatsLogExpireInterval: 0
       StatusCmdShowAll: 0
       CrashExpireInterval: 0
       SitePolicyScripts: local.zeek
       LogDir: /nsm/zeek/logs
       SpoolDir: /nsm/zeek/spool
       CfgDir: /opt/zeek/etc
       CompressLogs: 1

For anything not defined here, Zeek will use its own defaults. The options that are allowed to be managed with the pillar can be found at https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/zeek/files/zeekctl.cfg.jinja.

In order to add or modify an option in ``zeekctl``, we will need to modify either the ``global`` or ``minion`` pillar file. For example, if we wanted to turn log compression off and change the timeout for Broker communication events to 20 seconds globally, we would add the following to the global pillar file.

::

   zeek:
     zeekctl:
       compresslogs: 0
       commtimeout: 20

Since ``zeek:zeekctl`` is a dictionary with dictionary values, we do not need to redefine the entire pillar here like we did for ``zeek:local`` above. Once the pillar file is saved and the node checks in with the manager, the ``zeekctl.cfg`` file will be updated and the ``so-zeek container`` will be restarted.

More Information
----------------

.. seealso::

    For more information about Zeek, please see https://www.zeek.org/.
