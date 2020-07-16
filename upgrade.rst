.. _upgrade:

soup
====

To update to the latest version of Security Onion 2.0, use the ``soup`` command:

::

    sudo soup

Please pay attention to the output of this command as it may request that you take specific action, such as manually restarting services. Also refer to the relevant blog entry for the update at https://blog.securityonion.net as there may be additional information there.

Agents
------

If you've previously added any external agents (Wazuh, filebeat, winlogbeat, etc.), be sure to upgrade them to match the version of your upgraded components.

Distributed deployments
-----------------------

If you have a distributed deployment with a manager node and separate sensor nodes and/or search nodes, you **only** need to run ``soup`` on the manager. Once ``soup`` has completed, other nodes should update themselves at the next salt highstate (typically within 15 minutes).
