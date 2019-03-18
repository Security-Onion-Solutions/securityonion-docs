Syslog
======

From https://syslog-ng.org:

    syslog-ng allows you to flexibly collect, parse, classify, and
    correlate logs from across your infrastructure and store or route
    them to log analysis tools.

Usage
-----

Security Onion uses syslog-ng as its primary syslog collector and to send logs to `Logstash <Logstash>`__ where they are parsed and augmented before being written to `Elasticsearch <Elasticsearch>`__.

Configuration
-------------

syslog-ng's configuration file is located at ``/etc/syslog-ng/syslog-ng.conf``.

Forwarding
----------

You can configure syslog-ng to `forward <syslog-output>`_ Bro / Wazuh / IDS logs to external systems.

More Information
----------------

For more information about syslog-ng, please see https://syslog-ng.org/.

| syslog-ng listens on port 514 (TCP and UDP) for incoming syslog from other devices (you may need to run `<so-allow>`__ to allow traffic from the IP address of your syslog sender). This gives you basic log collection. If you'd like those logs collected from other devices to be analyzed, another option is to configure Wazuh to receive syslog directly on a port other than the syslog-ng port of 514.  For more information, please see:
| http://ossec-docs.readthedocs.org/en/latest/syntax/head_ossec_config.remote.html
| http://www.ossec.net/ossec-docs/OSSEC-book-ch3.pdf
