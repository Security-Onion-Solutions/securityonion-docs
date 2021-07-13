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

Walkthrough: Google Workspace Audit Logs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this brief walkthrough, we’ll use the ``google_workspace`` module for Filebeat to ingest ``admin`` and ``user_accounts`` logs from Google Workspace into Security Onion.  

Please follow the steps below to get started.

The official Elastic documentation for the Google Workspace module can be found here;

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


More Information
----------------

.. seealso::

    For more information about Filebeat, please see https://www.elastic.co/beats/filebeat.
