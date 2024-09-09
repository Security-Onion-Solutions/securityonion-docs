

.. _rbac:

Role-Based Access Control (RBAC)
=================================

The ability to restrict or grant specific privileges to a subset of users is covered by role-based access control, or "RBAC" for short. RBAC is an authorization technique in which users are assigned one of a small set of roles, and then the roles are associated to many low-level privileges. This provides the ability to build software with fine-grained access control, but without the need to maintain complex associations of users to large numbers of privileges. Users are traditionally assigned a single role, one which correlates closely with their role in the organization. However, it's possible to assign a user to multiple roles, if necessary.

RBAC in Security Onion covers both Security Onion privileges and Elastic stack privileges. Security Onion privileges are only involved with functionality specifically provided by the components developed by Security Onion, while Elastic stack privileges are only involved with the :ref:`elasticsearch`, :ref:`kibana`, and related Elastic stack. For example, Security Onion will check if a user has permission to create a PCAP request, while Elastic will check if the same user has permission to view a particular index or document stored in :ref:`elasticsearch`. 

Default Roles
-------------

Security Onion ships with the following user roles: ``superuser``, ``analyst``, ``limited-analyst``, ``auditor``, and ``limited-auditor``.

See the table below which explains the specific Security Onion privileges granted to each role. 

.. list-table::
    :widths: 50 10 10 10 10 10
    :header-rows: 1
    :name: role-table

    * - 
      - superuser
      - analyst
      - limited-analyst
      - auditor
      - limited-auditor
    * - View alerts
      - X
      - X
      - X
      - X
      - X
    * - Acknowledge alerts
      - X
      - X
      - X
      - 
      -
    * - Escalate alerts and events
      - X
      - X
      - X
      - 
      -
    * - View detections
      - X
      - X
      - X
      - X
      - X
    * - Modify (and Delete) detections
      - X
      - X
      - 
      - 
      - 
    * - View events in Hunt
      - X
      - X
      - X
      - X
      - X
    * - View own PCAP jobs
      - X
      - X
      - X
      - O
      - O
    * - View all PCAP jobs
      - X
      - X
      - 
      - X
      - 
    * - Pivot to PCAP job from event
      - X
      - X
      - X
      - 
      -  
    * - Request arbitrary PCAP jobs
      - X
      - X
      -  
      -  
      -  
    * - Delete own PCAP job
      - X
      - X
      - X
      - O
      - O
    * - Delete any PCAP job
      - X
      - X
      -  
      -  
      -  
    * - View all nodes in grid
      - X
      - X
      - X
      - X
      - X
    * - View all users
      - X
      - X
      -  
      - X
      -  
    * - View all users' roles
      - X
      - X
      -  
      - X
      -  
    * - View own user
      - X
      - X
      - X
      - X
      - X
    * - View own user roles
      - X
      - X
      - X
      - X
      - X
    * - Change own password
      - X
      - X
      - X
      - X
      - X
    * - Add, update, and reset SOC users
      - X
      - 
      - 
      - 
      - 
    * - Modify and synchronize grid config
      - X
      - 
      - 
      - 
      - 
    * - Manage grid membership of nodes
      - X
      - 
      - 
      - 
      - 
    * - Initiate node actions (Ex: reboot)
      - X
      - 
      - 
      - 
      - 

.. note::

    Both ``auditor`` and ``limited-auditor`` roles can interact with previously created PCAPs if they were created before a user was converted to that role (e.g. user was downgraded from ``analyst`` to ``auditor``). This is denoted by **O** in the above table.

.. note::

    A system role called ``agent`` is used by the Security Onion agent that runs on each node of the Security Onion grid. This special role is given the  *jobs/process*, *nodes/read*, and *nodes/write* permissions (defined at the bottom of this page). Avoid creating custom roles that share the same name as Security Onion-provided roles.


Superusers
----------

After a new installation of Security Onion completes, a single administrator user will be created and assigned the ``superuser`` role. Additional users can also be assigned to the ``superuser`` role, if desired.

Adding a User With a Specific Role
----------------------------------

In the :ref:`administration` interface, navigate to the Users screen and click the + icon to add a new user. In the popup dialog you can check the roles you would like to assign to the new user.

Modifying User Roles
----------------------

In the :ref:`administration` interface, navigate to the Users screen and click the > icon to the left of the email address needing adjusting. Check or uncheck the desired roles. 


Creating Custom Roles
---------------------

.. warning:: 

    The creation of custom RBAC roles is an advanced feature that is recommended only for experienced administrators.

These steps will guide you through an example where we wish to introduce a new role called ``eastcoast-analyst``, which will inherit the same Security Onion permissions as a limited-analyst, but will be restricted to only view a subset of documents in the Elastic stack. We base this role on the ``limited-analyst`` instead of the ``analyst`` role so that the user does not have the ability to create arbitrary PCAPs on any sensor.

1. For the Security Onion role: Follow the instructions in the next section entitled "Defining Security Onion Roles" to create a new role named ``eastcoast-analyst``.

2. For the Elastic stack role: Create a new json role file named ``eastcoast-analyst.json`` under ``/opt/so/saltstack/local/salt/elasticsearch/roles``. In this example we will define the new role that only allows access to documents from sensors on the east coast of the United States. Specifically, the role will include a query filter that limits search results to only include documents originating from sensors having a name prefixed with ``nyc`` (New York City) or ``atl`` (Atlanta). 

    ``eastcoast-analyst.json`` :
    ::

        {
          "cluster": [
            "cancel_task",
            "create_snapshot",
            "monitor",
            "monitor_data_frame_transforms",
            "monitor_ml",
            "monitor_rollup",
            "monitor_snapshot",
            "monitor_text_structure",
            "monitor_transform",
            "monitor_watcher",
            "read_ccr",
            "read_ilm",
            "read_pipeline",
            "read_slm"
          ],
          "indices": [
            {
              "names": [
                "so-*"
              ],
              "privileges": [
                "index",
                "maintenance",
                "monitor",
                "read",
                "read_cross_cluster",
                "view_index_metadata"
              ],
              "query": "{ \"bool\": { \"should\": [ { \"prefix\": { \"observer.name\": \"nyc\" }}, { \"prefix\": { \"observer.name\": \"atl\" }} ]}}"
            }
          ],
          "applications": [
            {
              "application": "kibana-.kibana",
              "privileges": [
                "feature_discover.all",
                "feature_dashboard.all",
                "feature_canvas.all",
                "feature_maps.all",
                "feature_ml.all",
                "feature_logs.read",
                "feature_visualize.all",
                "feature_infrastructure.read",
                "feature_apm.read",
                "feature_uptime.read",
                "feature_siem.read",
                "feature_dev_tools.read",
                "feature_advancedSettings.read",
                "feature_indexPatterns.read",
                "feature_savedObjectsManagement.read",
                "feature_savedObjectsTagging.read",
                "feature_fleet.all",
                "feature_actions.read",
                "feature_stackAlerts.read"
              ],
              "resources": [
                "*"
              ]
            }
          ],
          "run_as": []
        }

    .. note::

        The format of the json in this file must match the request body outlined in the Elastic docs here: https://www.elastic.co/guide/en/elasticsearch/reference/current/security-api-put-role.html#security-api-put-role-request-body.

        The available cluster and indices permissions are explained in the Elastic docs here: https://www.elastic.co/guide/en/elasticsearch/reference/current/security-privileges.html.

        The available kibana permissions can be obtained by running the following command on the manager node:

        ::

            sudo so-elasticsearch-query _security/privilege/kibana-.kibana | jq '. | map_values(keys)'


3. Run so-checkin from the manager:

    ::

        sudo so-checkin


Defining Security Onion Roles
-----------------------------

There are two ways to define a custom Security Onion role: 

1) Building it from scratch using the built-in permissions and default roles available as outlined later in this document, or 

2) Inheriting the permissions of another role, and optionally adding more permissions to the new custom role.

.. note::
    
    The ``custom_roles`` file contains further instructions on modifying roles that are not within the scope of this documentation.


The common syntax for either method of defining a role is as such:

.. code-block:: text

    <existing role or permission>:<new role>


1. Creating the role for the above east coast analyst using the first method, building the custom role from scratch, would be written like so:

    ::
        
        case-admin:eastcoast-analyst
        event-admin:eastcoast-analyst
        node-monitor:eastcoast-analyst
        user-monitor:eastcoast-analyst
        job-user:eastcoast-analyst

2. Alternatively, the ``eastcoast-analyst`` role could be created by inheriting the permissions of the analyst role:

    ::

        limited-analyst:eastcoast-analyst


Security Onion Privileges and Default Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The available low-level Security Onion privileges are listed in the table below:

.. list-table::
    :widths: 25 50
    :header-rows: 0

    * - *cases/read*
      - Read all case-related information for all cases
    * - *cases/write*
      - Create and update cases, and escalate events to cases
    * - *config/read*
      - Read system configuration parameters
    * - *config/write*
      - Update and in some cases duplicate system configuration parameters
    * - *detections/read*
      - Read all detection related details
    * - *detections/write*
      - Create and update detections and overrides
    * - *events/read*
      - Read from Elasticsearch
    * - *events/read*
      - Read from Elasticsearch
    * - *events/write*
      - Write to Elasticsearch
    * - *events/ack*
      - Acknowledge alerts
    * - *grid/read*
      - Read information about the grid and its node memberships
    * - *grid/write*
      - Accept and reject grid memberships from new and existing nodes
    * - *jobs/read*
      - View all PCAP jobs
    * - *jobs/pivot*
      - Pivot to PCAP job from event
    * - *jobs/write*
      - Request arbitrary PCAP jobs
    * - *jobs/delete*
      - Delete any PCAP job
    * - *jobs/process*
      - Update, read, and attach packets to all pending PCAP jobs †
    * - *nodes/read*
      - View all nodes in grid
    * - *nodes/write*
      - Update node information †
    * - *roles/read*
      - View all users' roles
    * - *roles/write*
      - Change any user's role
    * - *users/read*
      - View all users
    * - *users/write*
      - Change any user's password
    * - *users/delete*
      - Delete any user

These discrete privileges are then collected into privilege groups as defined below:

.. list-table::
    :widths: 25 50
    :header-rows: 0

    * - case-admin
      - *cases/read*, *cases/write*
    * - case-monitor
      - *cases/read*
    * - config-admin
      - *config/read*, *config/write*
    * - config-monitor
      - *config/read*
    * - detections-admin
      - *detections/read*, *detections/write*
    * - detections-monitor
      - *detections/read*
    * - event-admin
      - *events/read*, *events/write*, *events/ack*
    * - event-monitor
      - *events/read*
    * - grid-admin
      - *grid/read*, *grid/write*
    * - grid-monitor
      - *grid/read*
    * - job-admin
      - *jobs/read*, *jobs/pivot*, *jobs/write*, *jobs/delete*
    * - job-monitor
      - *jobs/read*
    * - job-user
      - *jobs/pivot*
    * - job-processor
      - *jobs/process* †
    * - node-admin
      - *nodes/read*, *nodes/write*
    * - node-monitor
      - *nodes/read*
    * - user-admin
      - *roles/read*, *roles/write*, *users/read*, *users/write*, *users/delete*
    * - user-monitor
      - *roles/read*, *users/read*

† intended for use by Sensoroni agents only
