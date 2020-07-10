.. _data-fields:

Data Fields
===========

This page references the various types of data fields utilized by the Elastic Stack in Security Onion.

The various fields types are described below.

Fields
------

| :ref:`alert-data-fields`
| :ref:`elastalert-fields`
| :ref:`zeek-fields`

Template files
--------------

Fields are mapped to their proper type using template files found in ``/opt/so/conf/logastash/etc/``. The current template files include:

| ``so-common-template.json`` - mapping information for logs going into ``so-*`` indices
| ``so-zeek-template.json`` - mapping information for logs going into ``so-zeek-*`` indices.
