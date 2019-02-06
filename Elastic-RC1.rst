GA now available
================

| Our Elastic Stack integration has reached General Availability! We
  highly recommend performing a fresh installation rather than trying to
  upgrade pre-release installations!
| https://blog.securityonion.net/2018/04/security-onion-elastic-stack-general.html

Warning
=======

Our Elastic integration is still considered experimental and so the
usual warnings and disclaimers apply:

Experimental Setup is BLEEDING EDGE and TOTALLY UNSUPPORTED!

-  If this breaks your system, you get to keep both pieces!
-  This is a work in progress and is in constant flux.
-  Do NOT run this on a system that you care about!
-  Do NOT run this on a system that has data that you care about!
-  This should only be run on a TEST box with TEST data!
-  Experimental Setup may result in nausea, vomiting, or a burning
   sensation.

NOT Officially Supported
========================

Performing an in-place upgrade from previous Alpha/Beta releases to the
current Release Candidate is NOT officially supported, but here are the
steps you can try. If you encounter any issues, please perform a fresh
installation of the current Release Candidate.

Single Standalone Box
=====================

If you're just upgrading a single standalone box, start with updating to
the latest packages:

::

    sudo soup

Then delete the Kibana index and template and reconfigure Kibana:

::

    curl -XDELETE http://localhost:9200/_template/kibana
    curl -XDELETE http://localhost:9200/.kibana
    sudo so-elastic-configure-kibana

Then clear Logstash:

::

    sudo so-elastic-clear-queue

Finally, delete ElastAlert indices and template and restart ElastAlert:

::

    sudo docker stop so-elastalert
    curl -XDELETE http://localhost:9200/elastalert_status
    curl -XDELETE http://localhost:9200/elastalert_status_silence
    curl -XDELETE http://localhost:9200/elastalert_status_error
    curl -XDELETE http://localhost:9200/elastalert_status_status
    curl -XDELETE http://localhost:9200/elastalert_status_past
    curl -XDELETE http://localhost:9200/_template/elastalert
    sudo docker start so-elastalert

Distributed Deployment
======================

Master Server
-------------

If you're upgrading a distributed deployment, please perform the
following steps on the master server before upgrading any sensors.

First, update all packages:

::

    sudo soup

Then delete the Kibana index and template and reconfigure Kibana:

::

    curl -XDELETE http://localhost:9200/_template/kibana
    curl -XDELETE http://localhost:9200/.kibana
    sudo so-elastic-configure-kibana

Then clear Logstash:

::

    sudo so-elastic-clear-queue

Finally, delete ElastAlert indices and template and restart ElastAlert:

::

    sudo docker stop so-elastalert
    curl -XDELETE http://localhost:9200/elastalert_status
    curl -XDELETE http://localhost:9200/elastalert_status_silence
    curl -XDELETE http://localhost:9200/elastalert_status_error
    curl -XDELETE http://localhost:9200/elastalert_status_status
    curl -XDELETE http://localhost:9200/elastalert_status_past
    curl -XDELETE http://localhost:9200/_template/elastalert
    sudo docker start so-elastalert

Sensors
-------

Once the master is updated, then perform the following steps on each
sensor.

First, update all packages:

::

    sudo soup

Then delete the Kibana index and template:

::

    curl -XDELETE http://localhost:9200/_template/kibana
    curl -XDELETE http://localhost:9200/.kibana

Then clear Logstash:

::

    sudo so-elastic-clear-queue

Finally, delete ElastAlert indices and template and disable ElastAlert:

::

    sudo docker stop so-elastalert
    curl -XDELETE http://localhost:9200/elastalert_status
    curl -XDELETE http://localhost:9200/elastalert_status_silence
    curl -XDELETE http://localhost:9200/elastalert_status_error
    curl -XDELETE http://localhost:9200/elastalert_status_status
    curl -XDELETE http://localhost:9200/elastalert_status_past
    curl -XDELETE http://localhost:9200/_template/elastalert
    sudo sed -i 's|ELASTALERT_ENABLED="yes"|ELASTALERT_ENABLED="no"|g' /etc/nsm/securityonion.conf
