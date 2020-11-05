.. _removing-a-sensor:

Removing a Sensor
=================

.. warning::

   This page has not been updated for Security Onion 2 yet! We'll get it updated soon.
   
There may come a time when you need to disable a sensor interface, delete a sensor's configuration, or get rid of an entire sensor and its data altogether. The steps below outline what is required to accomplish each objective.

Disable sensor interface
------------------------

To disable a sensor interface:

-  stop all sensor processes:

::

   sudo so-sensor-stop
   
-  edit ``/etc/nsm/sensortab`` and comment out the sensor interface line
-  edit ``/opt/bro/etc/node.cfg`` and comment out the sensor interface stanza
-  start all sensor processes:

::

   sudo so-sensor-start

Delete sensor configuration
---------------------------

-  To delete the configuration for a sensor, run ``/usr/sbin/nsm_sensor_del`` on the sensor box for which you wish to delete the configuration.

Wipe sensor configuration and data
----------------------------------

-  To completely wipe sensor configuration and data, run ``sudo sosetup`` on the sensor box for which you wish to wipe the
   data and configuration.

Remove sensor reference from manager node
-----------------------------------------
-  List all keys:
::
   sudo salt-key

-  Remove the sensor by deleting its key from salt:
::
   sudo salt-key -d sensor_key_name

Remove search node reference from manager node Elasticsearch _cluster/settings
------------------------------------------------------------------------------

From Kibana, navigate to ``Dev Tools`` and paste the following text into the window (modifying ``nodename`` to match the name of your node):

::

    PUT _cluster/settings
    {
      "persistent": {
        "search": {
          "remote": {
            "nodename": {
              "skip_unavailable": null,
              "seeds":null
            }
          }
        }
      }  
    }

Click the play button to send the request to Elasticsearch.
