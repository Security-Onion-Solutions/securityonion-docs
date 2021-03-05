.. _soup:

soup
====

When we release a new version of Security Onion, we update :ref:`release-notes` and publish a blog post to https://blog.securityonion.net. You'll want to review these for any relevant information about the individual updates.

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

Airgap
------

If you have an airgap deployment, please see the :ref:`airgap` section for further information.

log_size_limit
--------------

``soup`` will check your ``log_size_limit`` values to see if they are over the recommended values. If so, it will ask you to update the values in ``/opt/so/saltstack/local/pillar/minions/``. When updating these files, please update any and all instances of ``log_size_limit`` as it may exist as ``elasticsearch:log_size_limit`` or ``manager:log_size_limit``.

Errors
------

When running ``soup``, you may see errors like:

::

    local:
        Data failed to compile:
    ----------
        Rendering SLS 'base:common' failed: Jinja variable 'list object' has no attribute 'values'
        
and/or

::

    Status: Downloaded newer image for quay.io/securityonion/so-acng:2.3.30
    quay.io/securityonion/so-acng:2.3.30
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   543  100   543    0     0   1412      0 --:--:-- --:--:-- --:--:--  1414
    There is a problem downloading the so-acng:2.3.30 image. Details: 
    gpg: Signature made Thu 18 Feb 2021 02:26:10 PM UTC using RSA key ID FE507013 gpg: BAD signature from "Security Onion Solutions, LLC <info@securityonionsolutions.com>"
    
If you see these errors, it most likely means that a salt highstate process was already running when ``soup`` began. You can wait a few minutes and then try ``soup`` again. Alternatively, you can run ``sudo salt-call state.highstate`` and wait for it to complete before running ``soup`` again.

Kibana
------

After ``soup`` completes, if :ref:`kibana` says ``Kibana server is not ready yet`` even after waiting a few minutes for :ref:`kibana` to fully initialize, then check ``/opt/so/log/kibana/kibana.log``. You may see something like:

::

    Another Kibana instance appears to be migrating the index. Waiting for that migration to complete. If no other Kibana instance is attempting migrations, you can get past this message by deleting index .kibana_6 and restarting Kibana
    
If that's the case, then you can do the following (replacing ``.kibana_6`` with the actual index name that was mentioned in your :ref:`kibana` log):

::

    curl -XDELETE localhost:9200/.kibana_6

    sudo so-kibana-restart
