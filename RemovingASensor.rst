Removing a Sensor
=================

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

Remove sensor reference from master server
------------------------------------------

-  In MySQL database ``securityonion_db``, edit ``sensor`` table (you can simply set active='N'), then restart sguild.
-  Stop sguild ``sudo so-sensor-stop``
-  Show sensor entries:

::

   sudo mysql --defaults-file=/etc/mysql/debian.cnf -Dsecurityonion_db -e 'select * from sensor';
   
-  Set sensor as inactive:

::

   sudo mysql --defaults-file=/etc/mysql/debian.cnf -Dsecurityonion_db -e "update sensor set active='N' where sid in (<SID1>,<SID2>)";
   
-  Start sguild:

::

   sudo so-sensor-start

-  If running salt, remove the sensor from ``/opt/onionsalt/salt/top.sls`` and then delete the key from salt:

::

   sudo salt-key -d sensor_key_name

-  PLEASE NOTE: This step is only required if you are still running ELSA. ELSA reached EOL on October 9, 2018.  On the master server, edit ``/etc/elsa_web.conf``, remove the sensor from the ``peers`` section, then restart Apache (``sudo service apache2 restart``).

Remove storage node reference from Master server Elasticsearch ``_cluster/settings``
------------------------------------------------------------------------------------

From Kibana, navigate to ``Dev Tools`` and paste the following text into
the window (modifying ``nodename`` to match the name of your node):

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
