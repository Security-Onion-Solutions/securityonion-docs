.. _filebeat:

Filebeat
========

From https://www.elastic.co/beats/filebeat:

     Filebeat helps you keep the simple things simple by offering a lightweight way to forward and centralize logs and files.
     
On an Evaluation installation, Filebeat sends logs directly to :ref:`elasticsearch`. For other installation types, Filebeat sends to :ref:`logstash`.

Configuration
-------------

You can configure Filebeat inputs and output using :ref:`salt`. An example of the filebeat pillar can be seen at https://github.com/Security-Onion-Solutions/securityonion/blob/master/salt/filebeat/pillar.example

Any inputs that are added to the pillar definition will be in addition to the default defined inputs. In order to prevent a :ref:`zeek` log from being used as input, the ``zeeklogs:enabled`` pillar will need to be modified. The easiest way to do this is via :ref:`so-zeek-logs`. 

Diagnostic Logging
------------------

Filebeat's log can be found in ``/opt/so/log/filebeat/``.

To debug Filebeat, copy ``/opt/so/saltstack/default/salt/filebeat/etc/filebeat.yml`` to ``/opt/so/saltstack/local/salt/filebeat/etc/filebeat.yml``, then change the ``logging.level`` value to ``debug``. Next, restart Filebeat with ``so-filebeat-restart``.  Be sure to remove the ``local`` file after debugging.

Modules
-------

Starting in Security Onion 2.3.60, we support official Filebeat modules. You can learn more about Filebeat modules at https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-modules.html.

Example 1: AWS Cloudtrail Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you would like to parse AWS Cloudtrail logs using the Filebeat ``cloudtrail`` module, you can add something like the following to a minion pillar (for example, the manager's minion pillar in ``/opt/so/saltstack/local/pillar/minions/$managername_manager.sls``) :

::
  
  filebeat:
    third_party_filebeat:
      modules:
        aws:
          cloudtrail:
            enabled: true
            var.queue_url: https://sqs.$REGION.amazonaws.com/$ACCOUNTID/$QUEUENAME
            var.access_key_id: ABCD1234
            var.secret_access_key: ABCD1234ABCD1234

Access key details can be found within the AWS console by navigating to ``My Security Credentials`` -> ``Access Keys``.

Example 2: Fortinet Logs
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to parse Fortinet logs using the Filebeat fortinet module, you can add something like the following to a minion pillar (for example, the manager's minion pillar in ``/opt/so/saltstack/local/pillar/minions/$managername_manager.sls``):

::

  filebeat:
    third_party_filebeat:
      modules:
        fortinet:
          firewall:
            enabled: true
            var.input: udp
            var.syslog_host: 0.0.0.0
            var.syslog_port: 9004

(Please note that :ref:`firewall` ports still need to be opened on the minion to accept the Fortinet logs.)

Walkthrough: AWS Cloudtrail Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this brief walkthrough, we’ll use the ``aws`` module for Filebeat to ingest ``cloudtrail`` logs from Amazon Web Services into Security Onion.  

Credit goes to Kaiyan Sheng and Elastic for having an excellent starting point on which to base this walkthrough: https://www.elastic.co/blog/getting-aws-logs-from-s3-using-filebeat-and-the-elastic-stack.

Please follow the steps below to get started.

The official Elastic documentation for the Google Workspace module can be found here:

https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-aws.html

NOTE: This module requires that the user have a valid AWS service account, and credentials/permissions to access to the SQS queue we will be configuring.

**AWS Cloudtrail Configuration**

`Create an SQS queue`:

Navigate to ``Amazon SQS`` -> ``Queues``, and click ``Create queue``.

Specify queue details, choosing to use a ``Standard`` queue, and providing a name:

.. image:: https://user-images.githubusercontent.com/16829864/125963350-b6f10fa0-c2d7-436b-8e52-ba0c4e3888a5.png
 :target: https://user-images.githubusercontent.com/16829864/125963350-b6f10fa0-c2d7-436b-8e52-ba0c4e3888a5.png
 

Specify an Advanced policy and add policy configuration (changing to suit your environment, as needed):

:: 

  {
   "Version": "2012-10-17",
   "Id": "example-ID",
   "Statement": [
    {
     "Sid": "example-statement-ID",
     "Effect": "Allow",
     "Principal": {
       "Service": "s3.amazonaws.com"  
     },
     "Action": [
      "SQS:SendMessage"
     ],
     "Resource": "arn:aws:sqs:<region>:<account-id>:<queue-name>",
     "Condition": {         
        "StringEquals": { "aws:SourceAccount": "<account-id" }
     } 
    }
   ]
  }

After the queue has been created, you will be redirected to a summary screen.  

From here, copy the provided ``URL`` value.  This value will be used to populate the queue URL in Security Onion’s Filebeat configuration.

`Create a Trail`:

We’ll create a trail using the AWS Cloudtrail console. To get to the Cloudtrail console, search for ``cloudtrail`` in the AWS search bar at the top of the screen within the main console, and select CloudTrail:

.. image:: https://user-images.githubusercontent.com/16829864/125963488-d84adeda-a366-473f-9eaf-e1191312337d.png
 :target: https://user-images.githubusercontent.com/16829864/125963488-d84adeda-a366-473f-9eaf-e1191312337d.pn

From the main page of the Cloudtrail console, we can create our trail by clicking ``Create a trail``:

.. image:: https://user-images.githubusercontent.com/16829864/125963551-044f4fca-58a1-47c4-bc9a-da084d490de3.png
 :target: https://user-images.githubusercontent.com/16829864/125963551-044f4fca-58a1-47c4-bc9a-da084d490de3.png

Next, we'll configure some basic details, and choose to use a new s3 bucket with our trail:

.. image:: https://user-images.githubusercontent.com/16829864/125963927-c7b41fe1-91db-41f0-85db-4ddbb3732d1a.png
 :target: https://user-images.githubusercontent.com/16829864/125963927-c7b41fe1-91db-41f0-85db-4ddbb3732d1a.png

We’ll also need to specify an alias for a KMS key:

.. image:: https://user-images.githubusercontent.com/16829864/125967848-21d859bd-ce4a-4950-a4ce-d33d3ae1e467.png
 :target: https://user-images.githubusercontent.com/16829864/125967848-21d859bd-ce4a-4950-a4ce-d33d3ae1e467.png

Scroll down, and click ``Next``.

From here, we'll select the type of log events we want to include with our trail:

.. image:: https://user-images.githubusercontent.com/16829864/125967981-0c10c52a-bd08-4e81-b2c3-6784f1559910.png
 :target: https://user-images.githubusercontent.com/16829864/125967981-0c10c52a-bd08-4e81-b2c3-6784f1559910.png

We'll then review our changes and click ``Create Trail``:

.. image:: https://user-images.githubusercontent.com/16829864/125968101-4d7aac8b-688c-4ee1-b8d6-eb182224c031.png
 :target: https://user-images.githubusercontent.com/16829864/125968101-4d7aac8b-688c-4ee1-b8d6-eb182224c031.png

The trail should now be created and viewable in ``Cloudtrail`` -> ``Trails``.  The ``Status`` column should display as ``Logging``.  Because we chose to create a new bucket when creating the trail, an s3 bucket should already be created.

We’ll need to ensure our bucket is configured correctly by modifying the event notification properties.  To do this, we’ll navigate to ``Amazon S3`` ->  ``$BucketName`` -> ``Properties`` -> ``Event notifications`` -> ``Create event notification``:

.. image:: https://user-images.githubusercontent.com/16829864/125964090-aea00fd8-8a96-4cfa-97e2-773731a411ae.png
 :target: https://user-images.githubusercontent.com/16829864/125964090-aea00fd8-8a96-4cfa-97e2-773731a411ae.png

Under ``Event Types``, we can select the type of events for which we would like to receive notifications to our SQS queue:

.. image:: https://user-images.githubusercontent.com/16829864/125964111-0b4aac39-fbf3-4867-ba06-4a9810a1007d.png
 :target: https://user-images.githubusercontent.com/16829864/125964111-0b4aac39-fbf3-4867-ba06-4a9810a1007d.png

We’ll also need to select the queue where events will be published:

.. image:: https://user-images.githubusercontent.com/16829864/125984529-d6337aee-1277-4dfe-9a93-9929e2d2f70c.png 
 :target: https://user-images.githubusercontent.com/16829864/125984529-d6337aee-1277-4dfe-9a93-9929e2d2f70c.png

If we would like to log bucket access events, we can enable ``Server Access Logging`` (within the bucket ``Properties`` section):

.. image:: https://user-images.githubusercontent.com/16829864/125983931-4473075f-f44a-4b06-82ae-58b25e7223e3.png 
 :target: https://user-images.githubusercontent.com/16829864/125983931-4473075f-f44a-4b06-82ae-58b25e7223e3.png

**Security Onion Configuration**

Now that we’ve configured our Cloudtrail trail and SQS queue, we need to place our credential information into our Filebeat module configuration within Security Onion. In this example, we’ll edit the minion pillar for the node we want to pull in the AWS Cloudtrail logs -- in this case, a standalone node.  In a distributed environment, this would likely be the manager node.

Edit ``/opt/so/saltstack/local/pillar/minions/$minion_standalone.sls``, adding the following configuration (if you are already using other modules, simply append the module specific configuration without adding the filebeat.third_party_filebeat.modules portion):


::

  filebeat:
    third_party_filebeat:
      modules:
        aws:
          cloudtrail:
            enabled: true
            var.queue_url: https://sqs.us-east-2.amazonaws.com/$youraccountid/demo-queue
            var.access_key_id: ABCDE1234
            var.secret_access_key: AbCdeFG...


Next, restart Filebeat on the node, with ``so-filebeat-restart``.

After a few minutes, assuming there are logs to be gathered, Filebeat should pull in those logs from AWS, and an Elasticsearch index named ``so-aws-$DATE`` should be created.  This can be verified by navigating to Hunt or Kibana, searching for ``event.module:aws``:

.. image:: https://user-images.githubusercontent.com/16829864/125967430-284b9038-657d-402f-bc59-7e4cc6ef1968.png
 :target: https://user-images.githubusercontent.com/16829864/125967430-284b9038-657d-402f-bc59-7e4cc6ef1968.png


We can also run the ``so-elasticsearch-query`` command, like so:

``so-elasticsearch-query _cat/indices | grep aws``

.. image:: https://user-images.githubusercontent.com/16829864/125966682-ee85f41d-628b-4c9c-89f7-72a8fe25e27e.png
 :target: https://user-images.githubusercontent.com/16829864/125966682-ee85f41d-628b-4c9c-89f7-72a8fe25e27e.png

Congratulations! You’ve ingested AWS Cloudtrail logs into Security Onion!


Walkthrough: Google Workspace Audit Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this brief walkthrough, we’ll use the ``google_workspace`` module for Filebeat to ingest ``admin`` and ``user_accounts`` logs from Google Workspace into Security Onion.  

Please follow the steps below to get started.

The official Elastic documentation for the Google Workspace module can be found here:

https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-google_workspace.html

NOTE: This module requires that the user have a valid Google Workspace administrator account. You’ll also need to set up a project within Google Cloud if that has not already been done (will set up as needed during the walkthrough).

**Google Cloud/Workspace Configuration**

Google provides documentation for setting up a service account here:

https://support.google.com/workspacemigrate/answer/9222993?hl=en

In this example, we’ll choose the automated method of service account creation (using a script and the Cloud Shell).

We can enter the Cloud Shell by clicking the Cloud Shell icon (right-hand side of screen) from **console.cloud.google.com** (signed in as our Google Workspaces Super Administrator):

.. image:: https://user-images.githubusercontent.com/16829864/125333193-f2ab5600-e317-11eb-95b7-08ac4c758549.png
 :target: https://user-images.githubusercontent.com/16829864/125333193-f2ab5600-e317-11eb-95b7-08ac4c758549.png

Once opened, we will run the following command:

``python3 <(curl -s -S -L https://git.io/gwm-create-service-account)``

.. image:: https://user-images.githubusercontent.com/16829864/125333342-24bcb800-e318-11eb-942c-8a8ffa70e8b8.png
 :target: https://user-images.githubusercontent.com/16829864/125333342-24bcb800-e318-11eb-942c-8a8ffa70e8b8.png

After running the command, we will be provided a menu (press Enter to continue):

.. image:: https://user-images.githubusercontent.com/16829864/125333417-3900b500-e318-11eb-8fca-872169fb42a6.png
 :target: https://user-images.githubusercontent.com/16829864/125333417-3900b500-e318-11eb-8fca-872169fb42a6.png
 
The script will proceed through the steps until the first phase of setup is complete:

.. image:: https://user-images.githubusercontent.com/16829864/125333649-7c5b2380-e318-11eb-8fb8-5709ac8100c7.png
 :target: https://user-images.githubusercontent.com/16829864/125333649-7c5b2380-e318-11eb-8fb8-5709ac8100c7.png

After the first phase of setup, you will be provided a URL to visit and authorize the changes.  When authorizing changes, make sure to add the following OAuth scope to the client:

``https://www.googleapis.com/auth/admin.reports.audit.readonly``

.. image:: https://user-images.githubusercontent.com/16829864/125333682-8715b880-e318-11eb-8bfc-b6d938bba530.png
 :target: https://user-images.githubusercontent.com/16829864/125333682-8715b880-e318-11eb-8bfc-b6d938bba530.png

Navigate back to the Cloud Shell and press Enter to proceed through the rest of the setup:

.. image:: https://user-images.githubusercontent.com/16829864/125333704-8f6df380-e318-11eb-99f7-d374c9b4fd30.png
 :target: https://user-images.githubusercontent.com/16829864/125333704-8f6df380-e318-11eb-99f7-d374c9b4fd30.png

You will be prompted to download a file containing the service account credentials: 

.. image:: https://user-images.githubusercontent.com/16829864/125333721-939a1100-e318-11eb-9526-5aed29aabbfb.png
 :target: https://user-images.githubusercontent.com/16829864/125333721-939a1100-e318-11eb-9526-5aed29aabbfb.png


Ensure this file is kept safe. We will provide it to Filebeat in the Security Onion Filebeat module configuration.

**Security Onion Configuration**

Now that we’ve set up a service account and obtained a credentials file, we need to place it into our Filebeat module configuration within Security Onion. In this example, we’ll edit the minion pillar for the node we want to pull in the Google Workspace logs -- in this case, a standalone node.  In a distributed environment, this would likely be the manager node.

Copy the credentials file to ``/opt/so/conf/filebeat/modules/`` as ``credentials_file.json``.

Edit ``/opt/so/saltstack/local/pillar/minions/$minion_standalone.sls``, adding the following configuration (if you are already using other modules, simply append the module specific configuration without adding the filebeat.third_party_filebeat.modules portion):


::

  filebeat:
    third_party_filebeat:
      modules:
        google_workspace:
          admin:
             enabled: true
             var.jwt_file: "/usr/share/filebeat/modules.d/credentials_file.jsonn
             var.delegated_account: "adminuser@yourdomain.com"
          user_accounts:
             enabled: true
             var.jwt_file: "/usr/share/filebeat/modules.d/credentials_file.jsonn
             var.delegated_account: "adminuser@yourdomain.com"

Next, restart Filebeat on the node, with ``so-filebeat-restart``.

After a few minutes, assuming there are logs to be gathered, Filebeat should pull in those logs from Google Workspace, and an Elasticsearch index named ``so-google_workspace-$DATE`` should be created.  This can be verified by navigating to Hunt or Kibana, searching for ``event.module:google_workspace``:

.. image:: https://user-images.githubusercontent.com/16829864/125335491-9c8be200-e31a-11eb-87e9-f328b4d7a07e.png
 :target: https://user-images.githubusercontent.com/16829864/125335491-9c8be200-e31a-11eb-87e9-f328b4d7a07e.png
 

We can also run the ``so-elasticsearch-query`` command, like so:

``so-elasticsearch-query _cat/indices | grep google_workspace``

.. image:: https://user-images.githubusercontent.com/16829864/125335044-18d1f580-e31a-11eb-8857-2e2040154a52.png
 :target: https://user-images.githubusercontent.com/16829864/125335044-18d1f580-e31a-11eb-8857-2e2040154a52.png
 

Congratulations!  You’ve ingested Google Workspace logs into Security Onion! 

Walkthrough: Okta System Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this brief walkthrough, we’ll use the ``okta`` module for Filebeat to ingest ``system`` logs from Okta into Security Onion.  Please follow the steps below to get started.

The official Elastic documentation for the Okta module can be found here:

https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-okta.html

NOTE: This module requires that the user have a valid API token for access to their Okta instance.

**Okta Configuration**

Within the Okta administrative console, from the pane on the left-hand side of the screen, navigate to ``Security-> API``.  

.. image:: https://user-images.githubusercontent.com/16829864/125307798-5cb70180-e2fe-11eb-8cb5-a635fbed8c3e.png
 :target: https://user-images.githubusercontent.com/16829864/125307798-5cb70180-e2fe-11eb-8cb5-a635fbed8c3e.png


Next, navigate to Tokens, and click ``Create Token``:


.. image:: https://user-images.githubusercontent.com/16829864/125307833-650f3c80-e2fe-11eb-93df-9bd8bd891093.png
 :target: https://user-images.githubusercontent.com/16829864/125307833-650f3c80-e2fe-11eb-93df-9bd8bd891093.png


Enter a name for the token, then click ``Create Token``:


.. image:: https://user-images.githubusercontent.com/16829864/125307857-6b051d80-e2fe-11eb-9951-9c89d2138849.png
 :target: https://user-images.githubusercontent.com/16829864/125307857-6b051d80-e2fe-11eb-9951-9c89d2138849.png


A confirmation message like the following should appear:


.. image:: https://user-images.githubusercontent.com/16829864/125307880-70fafe80-e2fe-11eb-94c2-f2cac8225991.png
 :target: https://user-images.githubusercontent.com/16829864/125307880-70fafe80-e2fe-11eb-94c2-f2cac8225991.png

Ensure the token provided below the message is saved and stored securely.

**Security Onion Configuration**

Now that we’ve got our token, we need to place it into our Filebeat module configuration within Security Onion. In this example, we’ll edit the minion pillar for the node we want to pull in the Okta logs -- in this case, a standalone node.  In a distributed environment, this would likely be the manager node.

Edit ``/opt/so/saltstack/local/pillar/minions/$minion_standalone.sls``, adding the following configuration (if you are already using other modules, simply append the module specific configuration without adding the filebeat.third_party_filebeat.modules portion):


::

  filebeat:
    third_party_filebeat:
      modules:
        okta:
          system:
            enabled: true
            var.url: https://$yourdomain/api/v1/logs
            var.api_key: "'$yourtoken'"


Next, restart Filebeat on the node, with ``so-filebeat-restart``.

After a few minutes, assuming there are logs to be gathered, Filebeat should pull in those logs from Okta, and an Elasticsearch index named ``so-okta-$DATE`` should be created.  This can be verified by navigating to Hunt or Kibana, searching for ``event.module:okta``:

.. image:: https://user-images.githubusercontent.com/16829864/125307921-7c4e2a00-e2fe-11eb-9fca-49b5112f647e.png
 :target: https://user-images.githubusercontent.com/16829864/125307921-7c4e2a00-e2fe-11eb-9fca-49b5112f647e.png

We can also run the ``so-elasticsearch-query`` command, like so:

``so-elasticsearch-query _cat/indices | grep okta``

.. image:: https://user-images.githubusercontent.com/16829864/125307904-77897600-e2fe-11eb-84bc-1998b71e48db.png
 :target: https://user-images.githubusercontent.com/16829864/125307904-77897600-e2fe-11eb-84bc-1998b71e48db.png
 

Congratulations!  You’ve ingested Okta logs into Security Onion! 

Walkthrough: Netflow Logs
~~~~~~~~~~~~~~~~~~~~~~~~~

In this brief walkthrough, we’ll use the ``netflow`` module for Filebeat to ingest Netflow logs into Security Onion.

Credit goes to Matthew Gracie for his YouTube video on setting up Netflow ingest: https://www.youtube.com/watch?v=ew5gtVjAs7g

Please follow the steps below to get started.

The official Elastic documentation for the Netflow module can be found here:

https://www.elastic.co/guide/en/beats/filebeat/current/filebeat-module-netflow.html

Overview of steps:

- enable third party module
- update docker config
- update firewall config
- build logstash pipeline

**Enable third party module**

Edit ``/opt/so/saltstack/local/pillar/minions/so-mgr_manager.sls``.  Add the code block below to the bottom of the file: 

::

  filebeat:
    third_party_filebeat:
      modules:
        netflow:
          log:
            enabled: true
            var.netflow_host: 0.0.0.0
            var.netflow_port: 2055

**Update docker config**

Next, we need to add an extra listening port to the Filebeat container.  We'll start by making a local copy the filebeat ``init.sls`` file.

::

  sudo cp /opt/so/saltstack/default/salt/filebeat/init.sls /opt/so/saltstack/local/salt/filebeat/init.sls

Next, set permissions on the file:

::

  chown socore:socore /opt/so/saltstack/local/salt/filebeat/init.sls

Edit ``/opt/so/saltstack/local/salt/filebeat/init.sls`` and add port ``2055`` to the ``port_bindings`` section of the so-filebeat config: 

::

  - port_bindings:
      - 0.0.0.0:514:514/udp
      - 0.0.0.0:514:514/tcp
      - 0.0.0.0:2055:2055/udp
      - 0.0.0.0:5066:5066/tcp

Save the file and run ``sudo salt-call state.apply filebeat`` to allow Salt to recreate the container.  You can check that the config has applied by running ``docker ps | grep so-filebeat``.  You should see ``0.0.0.0:2055->2055/udp`` among the other existing listening ports.

**Update firewall config**

The next step is to add a host group and port group for Netflow traffic to allow it through the firewall.  Replace ``172.30.0.0/16`` with whatever is appropriate for your network. 

::

  so-firewall addhostgroup netflow
  so-firewall addportgroup netflow
  so-firewall includehost netflow 172.30.0.0/16
  so-firewall addport netflow udp 2055

Edit ``/opt/so/saltstack/local/pillar/minions/<manager.sls>`` to add iptables rules to allow the new netflow groups: 

::

  firewall:
    assigned_hostgroups:
      chain:
        DOCKER-USER:
          hostgroups:
            netflow:
              portgroups:
                - portgroups.netflow
        INPUT:
          hostgroups:
            netflow:
              portgroups:
                - portgroups.netflow

Save the file and then run ``sudo salt-call state.apply firewall`` to enable the new firewall rules.

**Build logstash pipeline**

Now the module is enabled, the container is listening on the right port, and the firewall is allowing traffic to get to the container.  Next is to ensure that the Netflow pipeline is enabled, or the data will not be saved to the ES database.

Note:  If you have a distributed setup, you need to run the following command on the search nodes as well.

``sudo docker exec -i so-filebeat filebeat setup modules -pipelines -modules netflow -c /usr/share/filebeat/module-setup.yml``

You should see ``Loaded Ingest pipelines``.  Once that is complete run ``sudo so-filebeat-restart``.

Assuming you have Netflow sources sending data, you should now start to see data in :ref:`hunt`.  Group by ``event.dataset`` and you should now have netflow.log entries appearing.

More Information
----------------

.. seealso::

    For more information about Filebeat, please see https://www.elastic.co/beats/filebeat.
