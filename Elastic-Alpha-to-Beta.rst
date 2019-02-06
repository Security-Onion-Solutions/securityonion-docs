GA now available
================

| Our Elastic Stack integration has reached General Availability! We
  highly recommend performing a fresh installation rather than trying to
  upgrade pre-release installations!
| https://blog.securityonion.net/2018/04/security-onion-elastic-stack-general.html

Introduction
============

| Our Elastic Alpha was released on 9/15/2017:
| http://blog.securityonion.net/2017/09/elastic-stack-alpha-release-and.html

| Our Elastic Beta was released on 11/1/2017:
| http://blog.securityonion.net/2017/11/elastic-stack-beta-release-and-security.html

Warning
=======

Our Elastic integration is currently in Beta and so the usual warnings
and disclaimers apply:

Experimental Setup is BLEEDING EDGE and TOTALLY UNSUPPORTED!

-  If this breaks your system, you get to keep both pieces!
-  This is a work in progress and is in constant flux.
-  This is intended to build a quick prototype proof of concept so you
   can see what our ultimate Elastic configuration might look like. This
   configuration will change drastically over time leading up to the
   final release.
-  Do NOT run this on a system that you care about!
-  Do NOT run this on a system that has data that you care about!
-  This should only be run on a TEST box with TEST data!
-  Experimental Setup may result in nausea, vomiting, or a burning
   sensation.

NOT Officially Supported
========================

Upgrading from Elastic Alpha to Elastic Beta is NOT officially
supported, but here are the steps you can try. If you encounter any
issues, please perform a fresh installation of Elastic Beta.

Single Standalone Box
=====================

If you're just upgrading a single standalone box, you should just need
to update all files and Docker images:

::

    sudo soup
    sudo so-elastic-configure

You may also need to manually update other settings like ``disk_space``
in ``/etc/curator/action/delete.yml``.

Distributed Deployment
======================

Master Server
-------------

If you're upgrading a distributed deployment, first run the following on
the master server:

::

    sudo soup
    sudo so-elastic-configure

You may also need to manually update other settings like ``disk_space``
in ``/etc/curator/action/delete.yml``.

Sensors
-------

Once the master is updated to Beta, then do the following on each
sensor:

-  Update all files and Docker images:

   ::

       sudo soup
       sudo so-elastic-configure

-  | Edit /etc/elasticsearch/elasticsearch.yml and add the following
   | (replacing ``$DOCKER_INTERFACE`` and ``$REVERSE_PORT`` with their
     respective
   | values from ``/root/.ssh/securityonion_ssh.conf``):

   ::

       transport.bind_host: 0.0.0.0
       transport.publish_host: $DOCKER_INTERFACE
       transport.publish_port: $REVERSE_PORT

-  Restart Elasticsearch:

   ::

       sudo docker restart so-elasticsearch

You may also need to manually update other settings like ``disk_space``
in ``/etc/curator/action/delete.yml``.
