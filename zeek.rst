Zeek
====

Zeek is formerly known as Bro.  From https://www.zeek.org/:

    Zeek is a powerful network analysis framework that is much different from the typical IDS you may know. (Zeek is the new name for the long-established Bro system. Note that parts of the system retain the "Bro" name, and it also often appears in the documentation and distributions.)

Performance
-----------

``/opt/bro/etc/node.cfg``

Zeek uses `<AF-PACKET>`_ so that you can spin up multiple Zeek workers to handle more traffic.  For best performance, Zeek should be pinned to specific CPUs. In most cases, you’ll want to pin sniffing processes to the same CPU that your sniffing NIC is bound to.  You can do this using the ``pin_cpus`` setting as shown at https://docs.zeek.org/en/stable/configuration/#using-pf-ring.

Logs
----

Zeek logs are stored in ``/nsm/zeek/logs``. They are consumed by `syslog-ng <syslog>`__, parsed and augmented by `Logstash <Logstash>`__, stored in `Elasticsearch <Elasticsearch>`__, and viewable in `Kibana <Kibana>`__.

We configure Zeek to output logs in JSON format for higher performance and better parsing. We recommend that most folks leave Zeek configured for JSON output.  If you need to parse those JSON logs from the command line, you can use `<jq>`_.

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

As you can see, Zeek log data can provide a wealth of information to the analyst, all easily accessible through `Kibana <Kibana>`__.

Email
-----

``/opt/bro/etc/broctl.cfg``

-  To configure email notifications, please see the `email <email#zeek>`__ section.

Syslog
------

``/etc/syslog-ng/syslog-ng.conf``

-  To forward Zeek logs to an external syslog collector, please see the `<syslog-output>`__ section.

Intel
-----

-  You can add your own Intel to ``/opt/bro/share/bro/intel/intel.dat``.

   -  When editing ``/opt/bro/share/intel/intel.dat``, ensure there are no leading/trailing spaces or lines, and that only (single) tabs are used as field delimiters.
   -  If you experience an error, or do not notice ``/nsm/bro/logs/current/intel.log`` being generated, try having a look in ``/nsm/bro/logs/current/reporter.log`` for clues.
   -  You may also want to restart Zeek after making changes, by running the following command:
      \ ``sudo so-zeek-restart``.

-  For more information, please see:

   | https://docs.zeek.org/en/latest/frameworks/intel.html\ 
   | http://blog.bro.org/2014/01/intelligence-data-and-bro_4980.html\ 
   | https://github.com/weslambert/securityonion-misp

-  To install and configure an Alienvault OTX Connector, please see the `<Alienvault-OTX>`__ section.

Custom Scripts
--------------

``/opt/bro/share/bro/site/local.bro``

-  You can add custom scripts in ``/opt/bro/share/bro/policy/`` and then reference the scripts in ``/opt/bro/share/bro/site/local.bro``.

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
-  Restart Zeek.
   ``sudo so-zeek-restart``
-  Check ``/nsm/bro/logs/current/loaded_scripts.log`` to see if your
   custom script(s) has/have been loaded.
-  Check ``/nsm/bro/logs/current/reporter.log`` for clues if your custom
   script(s) is/are not working as desired.

To check and see if a Zeek script has fired a Notice, go to Kibana and check our ``Zeek Notices`` dashboard. Alternatively, you can check for entries in ``/nsm/bro/logs/current/notice.log``.

.. note::

    In a distributed deployment, all custom scripts created under ``/opt/bro/share/bro/policy/`` on a master server will be replicated to sensors via Salt, however, they will not be enabled, as ``/opt/bro/share/bro/site/local.bro`` is not replicated. Therefore, you will either need to manually add a reference to the scripts in ``/opt/bro/share/bro/site/local.bro``, or add additional configuration in ``/opt/onionsalt/salt/sensor/init.sls`` for Salt to replicate this information.

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

You can then have Zeek automatically restart upon a detected change in ``local.bro`` from the master by modifying ``init.sls`` similar to the following:

::

    restart-bro
    cmd.wait:
      - name: /usr/sbin/nsm_sensor_ps-restart --only-bro
      - cwd: /
      - watch:
        - file: /opt/bro/share/bro/site/local.bro

Import
------
You can import Zeek logs into Elasticsearch by dropping them into ``/nsm/import/bro/``.  Logstash monitors that directory as defined in ``0007_input_import.conf``.

/nsm/bro/spool/tmp
------------------

If you find that /nsm/bro/spool/tmp contains lots of old crash files,
you can clean them up with:

::

    sudo su sguil -c '/opt/bro/bin/broctl cleanup --all'

More Information
----------------
For more information about Zeek, please see https://www.zeek.org/.
