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

If you have a distributed deployment with a management server and separate sensor boxes and/or search nodes, always update the management server first before updating other boxes. Then make sure to update the remaining boxes shortly thereafter. This will help to ensure that all boxes in your deployment are running the same code versions and help to avoid any incompatibilities.
