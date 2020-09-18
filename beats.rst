.. _beats:

Beats
=====

We can use Elastic Beats to facilitate the shipping of endpoint logs to Security Onion's Elastic Stack. Currently, testing has only been performed with Filebeat (multiple log types) and Winlogbeat (Windows Event logs).

.. note::

   In order to receive logs from Beats, Security Onion must be running Logstash. Evaluation Mode and Import Mode do not run Logstash, so you'll need Standalone or a full Distributed Deployment.

Encryption
----------

.. warning::

   Beats communication with Logstash is ``not encrypted`` by default. If you require encryption, please consult the appropriate Elastic documentation to configure the use of TLS.
   
so-allow
--------

Run ``sudo so-allow`` and select ``b`` to allow your Beats agents to send their logs to Logstash port 5044/tcp.

Winlogbeat
----------

Navigate to the Downloads page in :ref:`soc` and download the linked Winlogbeat agent. This will ensure that you get the correct version of Winlogbeat for your Elastic version. Install Winlogbeat and then configure it as follows:

* disable the Elasticsearch output
* make sure that Winlogbeat is NOT configured to load dashboards into Kibana
* enable the logstash output and configure it to send logs to port ``5044`` on your management node
* If you are shipping Sysmon logs, confirm that your Winlogbeat configuration does NOT use the Elastic Sysmon module as Security Onion will do all the necessary parsing

Installation
------------

To install a Beat, follow the instructions provided for the respective Beat, with the exception of loading the index template, as Security Onion uses its own template file to manage Beats fields.

Filebeat

https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html

Winlogbeat

https://www.elastic.co/guide/en/beats/winlogbeat/current/winlogbeat-installation.html

If installing Filebeat on a Linux distribution, you will want to ensure that the service is started after a reboot.  We can ensure this by running the following commands after install:

::

   sudo update-rc.d filebeat defaults

   sudo update-rc.d filebeat enable

Log files
---------

Filebeat
~~~~~~~~

Windows: ``C:\Program Files\Filebeat\filebeat.log``

Linux: ``/var/log/filebeat/filebeat``

Winlogbeat
~~~~~~~~~~

``C:\Program Files\Winlogbeat\winlogbeat.log``

Default fields:
https://www.elastic.co/guide/en/beats/winlogbeat/master/exported-fields-eventlog.html

Data
----

Beats data can be viewed via the ``Beats`` dashboard, (or through the selection of the ``*:logstash-beats-*`` index pattern in ``Discover``) in Kibana.

If you access the Beats dashboard and see logs but the visualizations have errors, you may need to refresh the ``logstash-beats-*`` field list as follows:

-  On the sidebar on the left, click ``Management``.
-  Click ``Index Patterns``.
-  Click ``logstash-beats-*``.
-  Click the circular arrows in the upper right to refresh the field list.
