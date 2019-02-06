Introduction
============

This page references the various types of data fields utilized by
Security Onion on the Elastic Stack.

The various fields types are described below.

Fields
======

| `Alert Data <Alert-Data-Fields>`__
| `Bro <Bro-Fields>`__
| `Elastalert <Elastalert-Fields>`__

Template files
==============

Fields are mapped to their proper type using template files, found in
``/etc/logstash/``. The current template files include:

| ``logstash-template.json`` - mapping information for logs going into
  ``logstash-*`` indices
| ``beats-template.json`` - mapping information for logs going into
  ``logstash-beats-*`` indices.
