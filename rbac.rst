

.. _rbac:

RBAC
====

RBAC in Security Onion covers both SOC privileges and Elastic privileges. 
The initial release of RBAC focuses on providing the capability for advanced administrators to customized their grid in order to limit direct search access to specific Elastic data. 
Additional RBAC features for SOC will be rolled out in future releases.


Default Roles
-------------

Security Onion by default ships with the following user roles: ``superuser``, ``analyst``, ``limited-analyst``, ``auditor``, and ``limited-auditor`` that have SOC permissions as shown in the below table. There is also a system role called ``agent`` used by the SOC agent that is given the  *jobs/process*, *nodes/read*, and *nodes/write* permissions (defined at the bottom of this page). 

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


.. note::

    Both ``auditor`` and ``limited-auditor`` roles can interact with previously created PCAPs if they were created before a user was converted to that role (e.g. user was downgraded from ``analyst`` to ``auditor``). This is denoted by **O** in the above table.


Adding a User With a Specific Role
----------------------------------

To add a user with a role other than the default ``analyst`` role, use the ``so-user add`` command with an additional parameter for the role. 
For example, to add the user ``tom@example.com`` with the ``auditor`` role:

::

    sudo so-user add "tom@example.com" auditor


Modifying User Roles
----------------------

To add a role to an existing user you can use the ``so-user addrole`` command. For example to add the ``analyst`` role to the user ``tom@example.com``:

::

    sudo so-user addrole "tom@example.com" superuser

Conversely to remove a role from a user use the ``so-user delrole`` command. To remove the ``analyst`` role from ``tom@example.com`` run:

::

    sudo so-user delrole "tom@example.com" superuser


Creating Custom Roles
---------------------

.. warning:: 

    The creation of custom RBAC roles is an advanced feature that is recommended only for experienced users.

To create a custom RBAC role in Security Onion, follow the steps below:

1. Create a new json role file under ``/opt/so/saltstack/local/salt/elasticsearch/roles`` for the Elasticsearch portion of the role. For example, a role that matches the analyst role but only allows access to documents from nodes on the east coast - in this example represented by having a name prefixed with ``nyc`` or ``atl`` - would be written like so. Note the "query" field under "indices":

    ``eastcoast_analyst.json`` :
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

        The format of the json in this file must match the request body outlined in the Elastic docs here: https://www.elastic.co/guide/en/elasticsearch/reference/7.x/security-api-put-role.html#security-api-put-role-request-body.

        The available cluster and indices permissions are explained in the Elastic docs here: https://www.elastic.co/guide/en/elasticsearch/reference/7.x/security-privileges.html.

        The available kibana permissions can be obtained by running the following command on the manager:

        ::

            sudo so-elasticsearch-query _security/privilege/kibana-.kibana | jq '. | map_values(keys)'


2. Add a custom role with the same name as the json file above to the ``custom_roles`` file located at ``/opt/so/saltstack/local/salt/soc/files/soc/custom_roles`` as outlined in "Defining SOC Roles".

3. Run a salt highstate from the manager:

    ::

        sudo salt-call state.highstate


Defining SOC Roles
------------------

There are two ways to define a custom SOC role, by 1) building it from scratch using the permissions and base roles available as outlined below, or 2) inheriting the permissions of another role and optionally adding more permissions to the new custom role.

.. note::
    
    The ``custom_roles`` file contains further instructions on modifying roles that are not within the scope of this documentation.


The common syntax for either method of defining a role is as such:

.. code-block:: text

    <role or permission>:<custom role name>


1. Creating the role for the above east coast analyst using the first method, building the custom role from scratch, would be written like so:

    ::
        
        case-admin:eastcoast_analyst
        event-admin:eastcoast_analyst
        node-monitor:eastcoast_analyst
        user-monitor:eastcoast_analyst
        job-admin:eastcoast_analyst

2. Alternatively, the east cost analyst could be created by inheriting the permissions of the analyst role:

    ::

        analyst:eastcoast_analyst


SOC Permissions and Base Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
The available permissions in SOC are listed in the table below:

.. list-table::
    :widths: 25 50
    :header-rows: 0

    * - *cases/write*
      - Escalate events
    * - *events/read*
      - Read from Elasticsearch
    * - *events/write*
      - Write to Elasticsearch
    * - *events/ack*
      - Acknowledge alerts
    * - *jobs/read*
      - View all PCAP jobs
    * - *jobs/pivot*
      - Pivot to PCAP job from event
    * - *jobs/write*
      - Request arbitrary PCAP jobs
    * - *jobs/delete*
      - Delete any PCAP job
    * - *jobs/process*
      - Update, read, and attach packets to all pending PCAP jobs
    * - *nodes/read*
      - View all nodes in grid
    * - *nodes/write*
      - Update node information
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

These permissions are then collected into base roles as defined below:

.. list-table::
    :widths: 25 50
    :header-rows: 0

    * - case-admin
      - *cases/write*
    * - event-admin
      - *events/read*, *events/write*, *events/ack*
    * - event-monitor
      - *events/read*
    * - job-admin
      - *jobs/read*, *jobs/pivot*, *jobs/write*, *jobs/delete*
    * - job-monitor
      - *jobs/read*
    * - job-user
      - *jobs/pivot*
    * - job-processor
      - *jobs/process*
    * - node-admin
      - *nodes/read*, *nodes/write*
    * - node-monitor
      - *nodes/read*
    * - user-admin
      - *roles/read*, *roles/write*, *users/read*, *users/write*, *users/delete*
    * - user-monitor
      - *roles/read*, *users/read*
