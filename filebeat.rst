.. _filebeat:

Filebeat
========

From https://www.elastic.co/beats/filebeat:

     Filebeat helps you keep the simple things simple by offering a lightweight way to forward and centralize logs and files.
     
In Security Onion 2.0, Filebeat collects logs from the filesystem. On an Evaluation installation, Filebeat sends those logs directly to :ref:`elasticsearch`. For other installation types, Filebeat sends to :ref:`logstash`.

Configuration
-------------

Filebeat's configuration can be found in ``/opt/so/conf/filebeat/``.

Logging
-------

Filebeat's log can be found in ``/opt/so/log/filebeat/``.

More Information
----------------

.. seealso::

    For more information about Filebeat, please see https://www.elastic.co/beats/filebeat.
