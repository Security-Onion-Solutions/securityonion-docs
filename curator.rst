.. _curator:

Curator
=======

From https://www.elastic.co/guide/en/elasticsearch/client/curator/current/about.html#about:

    Elasticsearch Curator helps you curate, or manage, your Elasticsearch indices and snapshots by:

    #. Obtaining the full list of indices (or snapshots) from the cluster, as the actionable list
    #. Iterate through a list of user-defined filters to progressively remove indices (or snapshots) from this actionable list as needed.
    #. Perform various actions on the items which remain in the actionable list.

Configuration
-------------
Curator ``actions`` are stored in ``/opt/so/conf/curator/action/``. These actions are run by cron jobs managed by :ref:`salt`.

Curator defaults to closing indices older than 30 days. To modify this, change ``cur_close_days`` in ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls``.

As your disk reaches capacity, Curator starts deleting old indices to prevent your disk from filling up. To change the limit, modify ``log_size_limit`` in ``/opt/so/saltstack/local/pillar/minions/$SENSORNAME_$ROLE.sls``.

Creating Actions
----------------
New action files should be added in ``/opt/so/saltstack/local/salt/curator/files/action/``, owned by ``curator:socore``, and will be copied into ``/opt/so/conf/curator/action/``.

Next, the script file tells Salt what to run in order to run your Curator job must be created for the new action. This script file must be placed in ``/opt/so/saltstack/local/salt/curator/files/bin/``. 
See ``/opt/so/saltstack/default/salt/curator/files/bin/`` for examples of script files, copy one over to modify if needed.

Next, the Saltstack configuration file for the Curator (``init.sls``) must be modified. This file is located at ``/opt/so/saltstack/local/salt/curator`` and will copy files over as well as set up the cronjob.
Create a backup of this file by copying it to a safe directory. Then, copy the default file located at ``/opt/so/saltstack/default/salt/curator/init.sls`` to the location of the current file and run a ``diff`` against the two ``init.sls``. Inside this file that was just copied over, the "cur" and "cron" sections must be added for your Curator job along with anything included in the ``diff`` command. Do not edit the original file in the directory.

To add the new Curator job, copy one of the existing sections and modify it, or use these examples:

For the "cur" section...
::
  cur<custom-name>:
    file.managed:
      - name: /usr/sbin/so-curator-<custom-name>
      - source: salt://curator/files/bin/<your_script_file_name>
      - user: 934
      - group: 939
      - mode: 755

For the "cron" section...
::
  so-curator<custom-name>:
   cron.present:
     - name: /usr/sbin/so-curator-<custom-name> > /opt/so/log/curator/<your_logfile>.log 2>&1
     - user: root
     - minute: '*'
     - hour: '*'
     - daymonth: '*'
     - month: '*'
     - dayweek: '*'

This particular cron section will run the task every minute. After this, restart the curator with ``so-curator-restart`` and note any errors. Changes are not errors.

To confirm that the job was added correctly, run ``crontab -l`` and look for the new task's cronjob. 

If the task's cronjob does not show up, there were errors during the restart process. You must fix those errors for the cronjob to be created.

Logs
----
When Curator completes an action, it logs its activity in a log file found in ``/opt/so/log/curator/``.

More Information
----------------

.. seealso::

    | For more information about Curator, please see:
    | https://www.elastic.co/guide/en/elasticsearch/client/curator/current/about.html#about
