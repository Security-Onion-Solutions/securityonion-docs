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
If you would like to create a custom Curator action, you will need to create a Curator action file and corresponding script file and then update Curator's state file.

Curator action file
~~~~~~~~~~~~~~~~~~~
You can add the action file to ``/opt/so/saltstack/local/salt/curator/files/action/``. Make sure the file ownership is ``curator:socore``. The file will automatically get copied into ``/opt/so/conf/curator/action/``.

Script file
~~~~~~~~~~~
The script file is what actually executes Curator and specifies the action file. This script file must be placed in ``/opt/so/saltstack/local/salt/curator/files/bin/``. See ``/opt/so/saltstack/default/salt/curator/files/bin/`` for examples of script files and copy one over to modify if needed.

State file
~~~~~~~~~~
Next, Curator's state file (``init.sls``) must be modified. This will be located at ``/opt/so/saltstack/local/salt/curator/`` and will copy files and create the cron job. 

If ``/opt/so/saltstack/local/salt/curator/init.sls`` does not already exist, you can copy ``/opt/so/saltstack/default/salt/curator/init.sls`` to ``/opt/so/saltstack/local/salt/curator/init.sls`` and modify as shown below.

If ``/opt/so/saltstack/local/salt/curator/init.sls`` does already exist, create a backup of the file by copying it to a safe directory. Then, copy the default file located at ``/opt/so/saltstack/default/salt/curator/init.sls`` to the location of the current file and run a ``diff`` against the two ``init.sls`` files. Inside this file that was just copied over, the "cur" and "cron" sections must be added for your Curator job along with anything included in the ``diff`` output. Do not edit the original file in the directory.

To add the new Curator job, copy and modify one of the existing sections or use these examples:

For the "cur" section:

::

  cur<custom-name>:
    file.managed:
      - name: /usr/sbin/so-curator-<custom-name>
      - source: salt://curator/files/bin/<your_script_file_name>
      - user: 934
      - group: 939
      - mode: 755

For the "cron" section:

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

This particular cron section will run the task every minute. After this, restart Curator with ``sudo so-curator-restart`` and note any errors (changes are not errors).

To confirm that the job was added correctly, run ``crontab -l`` and look for the new task's cron job. 

If the task's cron job does not show up, then there may have been errors during the restart process. You must fix those errors for the cron job to be created.

Logs
----
When Curator completes an action, it logs its activity in a log file found in ``/opt/so/log/curator/``.

More Information
----------------

.. seealso::

    | For more information about Curator, please see:
    | https://www.elastic.co/guide/en/elasticsearch/client/curator/current/about.html#about
