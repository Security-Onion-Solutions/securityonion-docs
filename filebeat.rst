.. _filebeat:

Filebeat
========

From https://www.elastic.co/beats/filebeat:

     Filebeat helps you keep the simple things simple by offering a lightweight way to forward and centralize logs and files.
     
In Security Onion 2.1, Filebeat collects logs from the filesystem. On an Evaluation installation, Filebeat sends those logs directly to :ref:`elasticsearch`. For other installation types, Filebeat sends to :ref:`logstash`.

Configuration
-------------

You can configure Filebeat inputs and output using :ref:`salt`. An example of the filebeat pillar can be seen at https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/filebeat/pillar.example

Any inputs that are added the pillar definition will be in addition to the default defined inputs. In order to prevent a :ref:`zeek` log from being used as input, the ``brologs:enabled`` pillar will need to be modified. Find the default definition at https://github.com/Security-Onion-Solutions/securityonion/blob/master/pillar/brologs.sls. Copy the contents of this file and place it in either the static or minion pillar file depending on if you want the changes to be global or specific to that individual node. If there is a log file that you would like to disable, move that entry from the enabled list to the disabled list. Be sure to follow the proper indentation for YAML.

Logging
-------

Filebeat's log can be found in ``/opt/so/log/filebeat/``.

More Information
----------------

.. seealso::

    For more information about Filebeat, please see https://www.elastic.co/beats/filebeat.
