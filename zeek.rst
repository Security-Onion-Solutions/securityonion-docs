.. _zeek:

Zeek
====

Zeek is formerly known as Bro.  From https://www.zeek.org/:

    Zeek is a powerful network analysis framework that is much different from the typical IDS you may know. (Zeek is the new name for the long-established Bro system. Note that parts of the system retain the "Bro" name, and it also often appears in the documentation and distributions.)

Performance
-----------

Zeek uses :ref:`af-packet` so that you can spin up multiple Zeek workers to handle more traffic.  

To change the number of AF-PACKET workers for :ref:`zeek`:

-  Stop Zeek:

   ::

      sudo so-zeek-stop

-  Edit ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls`` and change the ``bro_lbprocs`` variable to the desired number of cores.

-  Start Zeek:

   ::

      sudo so-zeek-start
      
For best performance, Zeek should be pinned to specific CPUs. In most cases, you’ll want to pin sniffing processes to the same CPU that your sniffing NIC is bound to.  You can do this using the ``pin_cpus`` setting as shown at https://docs.zeek.org/en/stable/configuration/#using-pf-ring.

Community ID
------------

We enable Zeek's native support for :ref:`community-id`.

Logs
----

Zeek logs are stored in ``/nsm/zeek/logs``. They are collected by :ref:`filebeat` or :ref:`logstash`, parsed by and stored in :ref:`elasticsearch`, and viewable in :ref:`hunt` and :ref:`kibana`.

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

As you can see, Zeek log data can provide a wealth of information to the analyst, all easily accessible through :ref:`kibana`.

Email
-----

-  To configure email notifications, please see the :ref:`email` section.

Syslog
------

-  To forward Zeek logs to an external syslog collector, please see the :ref:`syslog-output` section.

Intel
-----

-  You can add your own Intel to ``/opt/zeek/share/zeek/intel/intel.dat``.

   -  When editing ``/opt/zeek/share/intel/intel.dat``, ensure there are no leading/trailing spaces or lines, and that only (single) tabs are used as field delimiters.
   -  If you experience an error, or do not notice ``/nsm/zeek/logs/current/intel.log`` being generated, try having a look in ``/nsm/zeek/logs/current/reporter.log`` for clues.
   -  You may also want to restart Zeek after making changes, by running the following command:
      \ ``sudo so-zeek-restart``.

-  For more information, please see:

   | https://docs.zeek.org/en/latest/frameworks/intel.html\ 
   | http://blog.bro.org/2014/01/intelligence-data-and-bro_4980.html\ 
   | https://github.com/weslambert/securityonion-misp

-  To install and configure an Alienvault OTX Connector, please see the :ref:`alienvault-otx` section.

Custom Scripts
--------------

TODO: add information here

More Information
----------------

.. seealso::

    For more information about Zeek, please see https://www.zeek.org/.
