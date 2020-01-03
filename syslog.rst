Syslog
======

From https://www.syslog-ng.com/products/open-source-log-management/:

    With syslog-ng, you can collect logs from any source, process them in real time and deliver them to a wide variety of destinations. syslog-ng allows you to flexibly collect, parse, classify, rewrite and correlate logs from across your infrastructure and store or route them to log analysis tools.

Usage
-----
Security Onion uses syslog-ng as its primary syslog collector and to send logs to `Logstash <Logstash>`__ where they are parsed and augmented before being written to `Elasticsearch <Elasticsearch>`__.

Configuration
-------------
syslog-ng's configuration file is located at ``/etc/syslog-ng/syslog-ng.conf``.

Forwarding
----------
You can configure syslog-ng to `forward <syslog-output>`_ Zeek / Wazuh / IDS logs to external systems.

Monitoring
----------
Regardless of whether syslog-ng is sending to the Elastic stack or some other external system, you should check to see that syslog-ng is not dropping logs.  sostat now has a syslog-ng section that shows stats and it will also check for any dropped logs.

Collection
----------
syslog-ng listens on port 514 (TCP and UDP) for incoming syslog from other devices.  You may need to run `<so-allow>`__ to allow traffic from the IP address of your syslog sender.

Analysis
--------
If you'd like to analyze logs collected from other devices, another option is to configure Wazuh to receive syslog directly on a port other than the syslog-ng port of 514.  For more information, please see http://ossec-docs.readthedocs.org/en/latest/syntax/head_ossec_config.remote.html.


More Information
----------------
For more information about syslog-ng, please see https://www.syslog-ng.com/products/open-source-log-management/.

