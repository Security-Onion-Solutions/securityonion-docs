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

Performing an in-place upgrade from previous Alpha/Beta/RC releases to
the current Release Candidate is NOT officially supported. If you're
currently running RC2, here are the steps you can try to update to RC3.
If you encounter any issues, please perform a fresh installation of the
current Release Candidate.

Distributed Deployments
=======================

If you're updating a distributed deployment, please perform the
following steps on the master server before upgrading any nodes. Any
nodes running logstash/elasticsearch will need to perform these steps as
well.

Updating
========

First, delete logstash templates before updating:

::

    curl -XDELETE localhost:9200/_template/logstash*

Next, update to new packages and images:

::

    sudo soup

Finally, if you have mapping conflicts in Kibana, then delete old
indices (this will delete all logstash data in Elasticsearch):

::

    curl -XDELETE localhost:9200/logstash-*
