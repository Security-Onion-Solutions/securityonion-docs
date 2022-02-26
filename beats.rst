.. _beats:

Beats
=====

We can use Elastic Beats to facilitate the shipping of endpoint logs to Security Onion's Elastic Stack. Currently, testing has only been performed with Filebeat (multiple log types) and Winlogbeat (Windows Event logs).

.. note::

   In order to receive logs from Beats, Security Onion must be running :ref:`logstash`. Evaluation Mode and Import Mode do not run :ref:`logstash`, so you'll need Standalone or a full Distributed Deployment. For more information, please see the :ref:`architecture` section.

so-allow
--------

Run ``sudo so-allow`` and select the ``b`` option to allow your Beats agents to send their logs to :ref:`logstash` port ``5044/tcp``.

Version
-------

When downloading a Beats agent, make sure the version number matches the version of Elastic running on your Security Onion deployment.

Winlogbeat
----------

Navigate to the Downloads page in :ref:`soc` and download the linked Winlogbeat agent. This will ensure that you get the correct version of Winlogbeat for your Elastic version.

Install Winlogbeat and copy ``winlogbeat.example.yml`` to ``winlogbeat.yml`` if necessary. Then configure ``winlogbeat.yml`` as follows:

* Make sure that the ``setup.dashboards.enabled`` setting is commented out or disabled.
* Disable the ``output.elasticsearch`` output.
* Enable the ``output.logstash`` output and configure it to send logs to port ``5044`` on your management node.
* If you are shipping :ref:`sysmon` logs, confirm that your Winlogbeat configuration simply collects the :ref:`sysmon` logs and does NOT use the Elastic Sysmon ``processors`` section as Security Onion will do all the necessary parsing.

Once ``winlogbeat.yml`` is configured properly, start the Winlogbeat service.

.. seealso::

	Check out our Winlogbeat video at https://youtu.be/Xz-7oDrZdQY!

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

Encryption
----------

.. warning::

   Beats communication with :ref:`logstash` is ``not encrypted`` by default. If you require encryption, you will need to manually configure it.

Configuring Encryption for Beats
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a few considerations when enabling encryption for Beats. If you enable it on the default port then all connections on 5044 will be required to use encryption. The other option is to create a custom port for encryption and send only encrypted beats to that port.  
   
Using the Beats default port 5044 with encryption
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Copy 0009_input_beats.conf to the local directory:

::

    cp /opt/so/saltstack/default/salt/logstash/pipelines/config/so/0009_input_beats.conf /opt/so/saltstack/local/salt/logstash/pipelines/config/so/0009_input_beats.conf    

Copy your certificates to the proper directory on the manager. You will need a cert from the ca that you are signing the cert from, as well as the cert and key.

::

    cp myca.crt /opt/so/saltstack/local/salt/logstash/etc/certs/
    cp mybeats.crt /opt/so/saltstack/local/salt/logstash/etc/certs/
    cp mybeats.key /opt/so/saltstack/local/salt/logstash/etc/certs/
    
Next make your config look like the one below. Note that the paths are not the same due to docker.
        
::
    
    input {
      beats {
        port => "5044"
        ssl => true
        ssl_certificate_authorities => ["/usr/share/logstash/myca.crt"]
        ssl_certificate => "/usr/share/logstash/certs/mybeats.crt"
        ssl_key => "/usr/share/logstash/certs/mybeats.key"
        tags => [ "beat-ext" ]
      }
    }

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

In :ref:`kibana`, you can find Beats data on the ``Host`` dashboard or by searching for ``_index:"*:so-beats-*"`` in Discover.

In :ref:`hunt`, you can find Beats data by searching for ``_index:"*:so-beats-*"``.
