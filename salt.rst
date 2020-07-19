.. _salt:

Salt
====

From https://docs.saltstack.com/en/latest/:

   Salt is a new approach to infrastructure management built on a dynamic communication bus. Salt can be used for data-driven orchestration, remote execution for any infrastructure, configuration management for any app stack, and much more.

.. note::

   Salt is a core component of Security Onion 2.0 as it manages all processes on all nodes. In a distributed deployment, the manager node controls all other nodes via salt. These non-manager nodes are referred to as salt minions.

Firewall Requirements
---------------------

Minions must be able to connect to the manager node on ports ``4505/tcp`` and ``4506/tcp``:

http://docs.saltstack.com/topics/tutorials/firewall.html

Checking Status
---------------

You can use salt's ``test.ping`` to verify that all your nodes are up:

::

    sudo salt '*' test.ping

Remote Execution
----------------

Similarly, you can use salt's ``cmd.run`` to execute a command on all your nodes at once. For example, to check disk space on all nodes:

::

    sudo salt '*' cmd.run 'df'

Configuration
-------------

Many of the options that are configurable in Security Onion 2.0 are done via pillar assignments in either the static or minion pillar files. Pillars are a Saltstack concept, formatted typically in YAML, that can be used to parameterize states via templating. Saltstack states are used to ensure the state of objects on a minion. In many of the use cases below, we are providing the ability to modify a configuration file by editing either the static or minion pillar file.

Static pillar file: This is the pillar file that can be used to make global pillar assignments to the nodes. It is located at ``/opt/so/saltstack/local/pillar/static.sls``.

Minion pillar file: This is the minion specific pillar file that contains pillar definitions for that node. Any definitions made here will override anything defined in other pillar files, including global. This is located at ``/opt/so/saltstack/pillar/minions/<minionid>.sls``.

Default pillar file: This is the pillar file located under ``/opt/so/saltstack/default/pillar/``. Files here should not be modified as changes would be lost during a code update.

Local pillar file: This is the pillar file under ``/opt/so/saltstack/local/pillar/``. These are the files that will need to be changed in order to customize nodes.

Below is an example of how we would modify ``local.zeek``.
We can see the default pillar assignments used for ``local.zeek`` in ``/opt/so/saltstack/default/pillar/zeek/init.sls``. This file should never be modified as it could be updated in the future and any modification made would be overwritten. The static or minion pillar files should be used for making changes as they are stored in ``/opt/so/saltstack/local/``, and that directory isn’t overwritten during a Security Onion code update.

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

Under ``zeek:local``, there are three keys: ``@load``, ``@load-sigs``, and ``redef``. In the pillar definition, ``@load`` and ``@load-sigs`` are wrapped in quotes due to the ``@`` character. Under each of the keys, there is a list of  items that will be added to the ``local.zeek`` file with the appropriate directive of either ``@load``, ``@load-sigs`` or ``redef``. In order to modify either of the lists, the entire list must redefined in either the static or minion pillar file.

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

We redefined the ``@load`` list in the minion pillar file, but we left out the ```protocols/ssh/detect-bruteforcing``. This will override the value defined in the ``/opt/so/saltstack/default/pillar/zeek/init.sls`` and the static pillar file if it is defined there, and prevent the script from being added to the ``local.zeek`` file. If we wanted to add a script to be loaded, then we would add out script to the list. Since we aren’t changing ``@load-sigs`` or ``redef``, then we do not need to add them here. Once the file is saved, and the node checks in the with manager, the ``local.zeek`` file will be updated and the ``so-zeek`` docker container will be restarted.

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

In order to add or modify an option in ``zeekctl``, we will need to modify either the ``static`` or ``minion`` pillar file. For example, if we wanted to turn log compression off and change the timeout for Broker communication events to 20 seconds globally, we would add the following to the static pillar file.

::

   zeek:
     zeekctl:
       compresslogs: 0
       commtimeout: 20

Since ``zeek:zeekctl`` is a dictionary with dictionary values, we do not need to redefine the entire pillar here like we did for ``zeek:local`` above. Once the pillar file is saved and the node checks in with the manager, the ``zeekctl.cfg`` file will be updated and the ``so-zeek container`` will be restarted.

Below is a list of items that can be customized with pillar settings:

Filebeat:
 Inputs and the output can be customized for filebeat. An example of the filebeat pillar can be see. at https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/filebeat/pillar.example
 Any inputs that are added the pillar definition, will be in addition to the default defined inputs. In order to prevent a Zeek log from being used as input, the brologs:enabled pillar will need to be modified. Find the default definition at, https://github.com/Security-Onion-Solutions/securityonion/blob/master/pillar/brologs.sls. Copy the contents of this file and place it in either the static or minion pillar file depending on if you want the changes to be global or specific to that individual node. If there is a log file that you would like to disable, move that entry from the enabled list to the disabled list. Be sure to follow the proper indentation for YAML.
 
Firewall: 
  Much of information and functionality that follows is handled with :ref:`so-allow` or so-firewall, but could help provide a better understanding of what those two scripts are doing under the hood.
 The firewall state and pillars were designed around the idea of creating port groups and host groups and creating an allow rule by assigning a port group to a host group. A node that has a port group / host group combination assigned to it, will allow the hosts in that group to connect to those ports on that node. There are many default rules that have already been assigned, they can be viewed here: 
 
  Default port groups: https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/firewall/portgroups.yaml
  
  Default host groups: https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/firewall/hostgroups.yaml
  
  Default port group assignments: https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/firewall/assigned_hostgroups.map.yaml
  
 During setup, the files from securityonion/files/firewall/ (https://github.com/Security-Onion-Solutions/securityonion/tree/master/files/firewall), are copied to the local directory located at: /opt/so/saltstack/local/salt/firewall/. Once setup is complete and so-allow or so-firewall are called in the future, they modify the appropriate yaml files that are located under /opt/so/saltstack/local/salt/firewall/. Since these yaml files are under /opt/so/saltstack/local/ they will not be changed during a code update.
 
IDS Tools:
 To enable or disable SIDS for Suricata, the ``idstools`` pillar can be used. The same concept applies to the ``idstools`` pillar being placed in static or the minion pillar file if you want the setting to be global or specific to the node.  
 
 If SID 1234 is commented out and you want to enable it, add the following to the appropriate static or minion pillar file:
 
::

   idstools:
     sids:
       enabled:
         - 1234

If SID 4321 is noisy, you can disable it as follows:

::

   idstools:
     sids:
       disabled:
         - 4321

Suricata:
 For Suricata, the ability to manage ``suricata.yaml`` has been provided. The defaults for this have been defined in https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/suricata/defaults.yaml. Under ``suricata:config``, the pillar structure follows the same YAML structure of the ``suricata.yaml`` file. For some of the settings to modify here, we have simplified the pillar configuration by placing the option in the sensor pillar instead of the Suricata pillar. These options are: ``HOMENET``, ``default-packet-size``, and the CPU affinity settings for pinning the processes to CPU cores or how many processes to run.

Thresholding: 
  To enable thresholding for SIDS, reference the example pillar at ``/opt/so/saltstack/default/pillar/thresholding/pillar.example``. To view the acceptable syntax, view the file located at ``/opt/so/saltstack/default/pillar/thresholding/pillar.usage``. This pillar can be added to either the static or minion pillar file.

Zeek:
 For Zeek, the ability to manage ``local.zeek``, ``node.cfg`` and ``zeekctl.cfg`` have been provided.
 
 ``local.zeek``: The allowed options for this file are ``@load``, ``@load-sigs`` and ``redef``. An example of configuring this pillar can be seen in the example above. 
 
 ``node.cfg``: The pillar items to modify this file are located under the sensor pillar in the minion pillar file. The options that can be customized in the file include: ``interface``, ``lb_procs``, ``pin_cpus``, and ``af_packet_buffer_size``.
 
 ``zeekctl.cfg``: An example of customizing this can be seen above. The allowed options can be seen in https://github.com/Security-Onion-Solutions/securityonion/blob/dev/salt/zeek/files/zeekctl.cfg.jinja.

More Information
----------------

.. seealso::

    For more information about Salt, please see https://docs.saltstack.com/en/latest/.
