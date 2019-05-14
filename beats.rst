Beats
=====

We can use Elastic Beats to facilitate the shipping of endpoint logs to Security Onion's Elastic Stack. Currently, testing has only been performed with Filebeat (multiple log types) and Winlogbeat (Windows Event logs).

Download
--------

To download a Beat, choose the correct version from the Past Releases page:   

https://www.elastic.co/downloads/past-releases   


PLEASE NOTE: Choosing a Beat version that is greater than the Elastic version is not supported and may not work as expected.    

To check your current version of Elastic, navigate to the Management section in Kibana.  The version should be displayed on the screen.    

Alternatively, run the following command from your master server, or Dev tools:   

`curl localhost:9200`


Installation
------------

To install a Beat, follow the instructions provided for the respective Beat, with the exception of loading the index template, as Security Onion uses its own template file to manage Beats fields.

Filebeat

https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-installation.html

Winlogbeat

https://www.elastic.co/guide/en/beats/winlogbeat/current/winlogbeat-installation.html

*If installing Filebeat on a Linux distribution, you will want to ensure that the service is started after a reboot.  We can ensure this by running the following commands after install:

::

   sudo update-rc.d filebeat defaults

   sudo update-rc.d filebeat enable

Firewall
--------

To ensure a Beat is allowed to talk to Logstash on the Security Onion box, we need to run `<so-allow>`_, and choose the ``b`` option for ``Beats``. After choosing this option, simply provide the IP address of the machine on which the Beat is installed and press ``ENTER`` to confirm.

Log files
---------

Filebeat
~~~~~~~~

Windows: ``C:\\Program Files\Filebeat\filebeat.log``

Linux: ``/var/log/filebeat/filebeat``

Winlogbeat
~~~~~~~~~~

``C:\\Program Files\Winlogbeat\winlogbeat.log``

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

Encryption
----------

Beats communication with Elasticsearch/Logstash is ``not encrypted`` by default. If you require encryption, please consult the appropriate Elastic documentation to configure the use of TLS.
