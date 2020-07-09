.. _filebeat:

Filebeat
========

From https://www.elastic.co/beats/filebeat:

     Filebeat helps you keep the simple things simple by offering a lightweight way to forward and centralize logs and files.
     
In Security Onion 2.0, filebeat collects logs from the filesystem. On an Evaluation installation, Filebeat send those logs directly to :ref:`elasticsearch`. For other installation types, Filebeat sends to :ref:`logstash`.
