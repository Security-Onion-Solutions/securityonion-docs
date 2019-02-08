Bro
===

From https://www.bro.org/:

    Bro is a powerful network analysis framework that is much different
    from the typical IDS you may know. While focusing on network
    security monitoring, Bro provides a comprehensive platform for more
    general network traffic analysis as well.

Logs
----

Bro logs are stored in ``/nsm/bro/logs``. They are consumed by
`syslog-ng <syslog>`__, parsed and augmented by `Logstash <Logstash>`__,
stored in `Elasticsearch <Elasticsearch>`__, and viewable in
`Kibana <Kibana>`__.

TSV
~~~

By default, we configure Bro to output in JSON for higher performance
and better parsing. We recommend that most folks leave Bro configured
for JSON output. If you really need the traditional Bro TSV (Tab
Separated Values) format, you can disable JSON:

::

    sudo sed -i 's|@load json-logs|#@load json-logs|g' /opt/bro/share/bro/site/local.bro

and then restart Bro:

::

    sudo so-bro-restart

Bro monitors your network traffic and creates logs, such as:

conn.log
~~~~~~~~

-  TCP/UDP/ICMP connections

-  For more information, see:

https://www.bro.org/sphinx-git/scripts/base/protocols/conn/main.bro.html#type-Conn::Info

dns.log
~~~~~~~

-  DNS activity

-  For more information ,see:

https://www.bro.org/sphinx-git/scripts/base/protocols/dns/main.bro.html#type-DNS::Info

ftp.log
~~~~~~~

-  FTP activity

-  For more information, see:

https://www.bro.org/sphinx-git/scripts/base/protocols/ftp/info.bro.html#type-FTP::Info

http.log
~~~~~~~~

-  HTTP requests and replies

-  For more information, see:

https://www.bro.org/sphinx-git/scripts/base/protocols/http/main.bro.html#type-HTTP::Info

ssl.log
~~~~~~~

-  SSL/TLS handshake info

-  For more information, see:

https://www.bro.org/sphinx-git/scripts/base/protocols/ssl/main.bro.html#type-SSL::Info

notice.log
~~~~~~~~~~

-  Bro notices

-  For more information, see:

https://www.bro.org/sphinx-git/scripts/base/frameworks/notice/main.bro.html#type-Notice::Info

| ...and others, which can be researched here:
| https://www.bro.org/sphinx-git/script-reference/log-files.html

As you can see, Bro log data can provide a wealth of information to the
analyst, all easily accessible through
`Kibana <Kibana>`__.

Intel
-----

-  You can add your own Intel to ``/opt/bro/share/bro/intel/intel.dat``.

   -  When editing ``/opt/bro/share/intel/intel.dat``, ensure there are
      no leading/trailing spaces or lines, and that only (single) tabs
      are used as field delimiters.
   -  If you experience an error, or do not notice
      ``/nsm/bro/logs/current/intel.log`` being generated, try having a
      look in ``/nsm/bro/logs/current/reporter.log`` for clues.
   -  You may also want to restart Bro after making changes, by running
      the following command:
      \ ``sudo nsm_sensor_ps-restart --only-bro``.

-  For more information, please see:

   | https://www.bro.org/sphinx-git/frameworks/intel.html\ 
   | http://blog.bro.org/2014/01/intelligence-data-and-bro_4980.html\ 
   | https://github.com/weslambert/securityonion-misp

-  To install and configure an Alienvault OTX Connector, please see:

   `<Alienvault-OTX>`__

Bro \* n
--------

``/opt/bro/etc/node.cfg``

We compile Bro with
`PF\_RING <PF_RING>`__
so that you can spin up multiple Bro workers to handle more traffic.

Custom Scripts
--------------

``/opt/bro/share/bro/site/local.bro``

-  You can add custom scripts in ``/opt/bro/share/bro/policy/`` and then
   reference the scripts in ``/opt/bro/share/bro/site/local.bro``.

Below is an example how to do so:

-  Create a new directory under ``/opt/bro/share/bro/policy/``.
   ``sudo mkdir /opt/bro/share/bro/policy/custom-scripts``
-  Add your custom script(s) and ``__load__.bro`` to this directory.
-  Modify ``__load__.bro`` to reference the scripts in the
   ``custom-scripts`` directory:

   | ``@load ./script1.bro``
   | ``@load ./script2.bro``

-  Edit ``/opt/bro/share/bro/site/local.bro`` so that it will load the
   new scripts in ``/opt/bro/share/bro/policy/custom-scripts``, by
   adding ``@load custom-scripts`` at the bottom of the file and saving
   the file.
-  Restart Bro.
   ``sudo nsm_sensor_ps-restart --only-bro``
-  Check ``/nsm/bro/logs/current/loaded_scripts.log`` to see if your
   custom script(s) has/have been loaded.
-  Check ``/nsm/bro/logs/current/reporter.log`` for clues if your custom
   script(s) is/are not working as desired.

To check and see if a Bro script has fired a Notice, go to ELSA, click
Notice, and then click "Top Notice Types". Alternatively, check for
entries in ``/nsm/bro/logs/current/notice.log``.

**PLEASE NOTE**: In a distributed deployment, all custom scripts created
under ``/opt/bro/share/bro/policy/`` on a master server will be
replicated to sensors via Salt, however, they will not be enabled, as
``/opt/bro/share/bro/site/local.bro`` is not replicated. Therefore, you
will either need to manually add a reference to the scripts in
``/opt/bro/share/bro/site/local.bro``, or add additional configuration
in ``/opt/onionsalt/salt/sensor/init.sls`` for Salt to replicate this
information.

-  Make a symlink to ``local.bro``:

``sudo ln -s /opt/bro/share/bro/site/local.bro /opt/onionsalt/salt/sensor/bro/local.bro``

Then add the following to ``/opt/onionsalt/salt/sensor/init.sls``:

::

    localbro:   
    file.managed:
       - name: /opt/bro/share/bro/site/local.bro
       - source: salt://sensor/bro/local.bro

Then test, using:

``sudo salt "SENSOR" state.highstate``

You can then have Bro automatically restart upon a detected change in
``local.bro`` from the master by modifying ``init.sls`` similar to the
following:

::

    restart-bro
    cmd.wait:
      - name: /usr/sbin/nsm_sensor_ps-restart --only-bro
      - cwd: /
      - watch:
        - file: /opt/bro/share/bro/site/local.bro

Email
-----

``/opt/bro/etc/broctl.cfg``

-  To configure email notifications, please see:

`<Email#how-do-i-configure-bro-to-send-emails>`__

Syslog
------

``/etc/syslog-ng/syslog-ng.conf``

-  To forward Bro logs to an external syslog collector, please see:

`<ThirdPartyIntegration#how-do-i-send-bro-and-ossec-logs-to-an-external-syslog-collector>`__

Top for Bro
-----------

-  To view "top-like" information for Bro logs, consider using BroTop.

-  "Brotop lets you stream your bro logs to the browser for easy
   debugging and a real-time glimpse into whats being processed".

-  Written in Go, BroTop is a dependency-free binary that can be
   downloaded and run immediately, auto-detecting Bro log paths.

-  For more information about BroTop, please see:

| https://github.com/criticalstack/brotop
| 
| For more information about Bro, please see:
| https://www.bro.org/

/nsm/bro/spool/tmp
------------------

If you find that /nsm/bro/spool/tmp contains lots of old crash files,
you can clean them up with:

::

    sudo su sguil -c '/opt/bro/bin/broctl cleanup --all'
