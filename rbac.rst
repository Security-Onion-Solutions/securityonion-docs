.. _rbac:

RBAC
====

.. note::

    RBAC in Security Onion covers both SOC privileges and Elastic privileges. 
    The initial release of RBAC focuses on providing the capability for advanced administrators to customized their grid in order to limit direct search access to specific Elastic data. 
    Additional RBAC features for SOC will be rolled out in future releases.


Default Roles
-------------

Security Onion by default ships with the following roles:

* **analyst** - ``Default Role``

  * **SOC** - Full access to Hunt, Grid and PCAP; can change own password
  * **ES** - Read and update access to ``so-*`` indices, read/write access to kibana features (dashboards, etc) and fleet features, read access to other application features, read access to cluster operations

* **auditor**

  * **SOC** - Full Hunt and Grid access, read only access to PCAP; can change own password 
  * **ES** - Read access to ``so-*`` indices, read access to kibana features (dashboards, etc) and fleet features, read access to other application features, read access to cluster operations

* **superuser**

  * **SOC** - Full access to Hunt, Grid, and PCAP; can change any user's password
  * **ES** - Full access to all Elastic and Kibana features


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

Creating a custom RBAC role in Security Onion, follow the steps below:

1. Create a new json role file under ``/opt/so/saltstack/local/salt/elasticsearch/roles`` for the Elasticsearch portion of the role. For example, a role that matches the analyst role but only allow access to documents from nodes on the east coast - in this example represented by having a name prefixed with ``nyc`` or ``atl`` - would be written like so. Note the "query" field under "indices":

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

There are two ways to define a custom SOC role, by 1) building it from scratch using the permissions and base roles available as outlined below, or 2) inheriting the permissions of another role (and optionally adding more permissions to the new custom role).

The common syntax for either method of defining a role is as such:

.. code-block:: text

    <role or permission>:<custom role name>


1. Creating the role for the above east coast analyst using the first method, building the custom role from scratch, would be written like so:

    ::

        grid-monitor:eastcoast_analyst
        user-monitor:eastcoast_analyst
        job-admin:eastcoast_analyst

2. Alternatively, the east cost analyst could be created by inheriting the permissions of the analyst role:

    ::

        analyst:eastcoast_analyst



SOC Permissions and Base Roles
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^


* **LIST TBD**


.. note::
    
    The ``custom_roles`` file contains further instructions on modifying roles that are not within the scope of this documentation.


