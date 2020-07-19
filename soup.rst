.. _soup:

soup
====

As we make updates to Security Onion, we publish blog posts to https://blog.securityonion.net. You'll want to review these blog posts for any relevant information about the individual updates.

Once you're ready to install an update, use the ``soup`` command:

::

    sudo soup

Please pay attention to the output of this command as it may request that you take specific action, such as manually restarting services. 

.. warning::

    Please note that ``soup`` only updates Security Onion components and does NOT update the underlying operating system (OS). There is an option during :ref:`Configuration` to automatically update the OS packages.
    
Agents
------

If you've previously added any external agents (Wazuh, filebeat, winlogbeat, etc.), be sure to upgrade them to match the version of your upgraded components.

Distributed deployments
-----------------------

If you have a distributed deployment with a manager node and separate sensor nodes and/or search nodes, you **only** need to run ``soup`` on the manager. Once ``soup`` has completed, other nodes should update themselves at the next salt highstate (typically within 15 minutes).
