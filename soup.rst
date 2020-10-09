.. _soup:

soup
====

As we make updates to Security Onion, we publish blog posts to https://blog.securityonion.net. You'll want to review these blog posts for any relevant information about the individual updates.

Once you're ready to install an update, use the ``soup`` command:

::

    sudo soup

If necessary, ``soup`` will update itself and then ask you to run ``soup`` again. Once ``soup`` is fully updated, it will then update :ref:`salt` and the :ref:`docker` images.

.. warning::

    Please note that ``soup`` only updates Security Onion components and does NOT update the underlying operating system (OS). There is an option during :ref:`Configuration` to automatically update the OS packages.
    
Agents
------

If you've previously added any external agents (:ref:`wazuh`, :ref:`beats`, etc.), be sure to upgrade them to match the version of your upgraded components.

Distributed deployments
-----------------------

If you have a distributed deployment with a manager node and separate sensor nodes and/or search nodes, you **only** need to run ``soup`` on the manager. Once ``soup`` has completed, other nodes should update themselves at the next :ref:`salt` highstate (typically within 15 minutes).
