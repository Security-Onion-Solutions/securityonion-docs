.. _soup:

soup
====

``SOUP`` stands for ``Security Onion UPdater``.  To install updates, run the ``soup`` command:

::

    sudo soup

If necessary, ``soup`` will update itself and then ask you to run ``soup`` again. Once ``soup`` is fully updated, it will then check for other updates.

Security Onion Version Updates
------------------------------

When we release a new version of Security Onion, we update the :ref:`release-notes` section and publish a blog post to https://blog.securityonion.net. You'll want to review these for any relevant information about the individual updates. For a full version update, soup will update :ref:`salt` code and all :ref:`docker` images. It will also update the Security Onion version in ``/etc/soversion``.

Security Onion Hotfixes
-----------------------

Starting in Security Onion 2.3.50, ``soup`` can check for Security Onion hotfixes. Hotfixes will typically include updates to the :ref:`salt` code and small configuration changes that do not warrant a full release. This does not include Docker images since that would require a full release. 

After applying a hotfix, you may notice that the Security Onion version in ``/etc/soversion`` stays the same. The application of the hotfix is tracked on the manager in the ``/etc/sohotfix`` file.

Airgap
------

If you have an airgap deployment, please see the :ref:`airgap` section for further information.

OS Updates
----------

There is an option during :ref:`Configuration` to automatically install OS updates.

Starting in Security Onion 2.3.50, ``soup`` will check for missing OS updates and ask if you want to install them.
    
Agents
------

If you've previously added any external agents (:ref:`wazuh`, :ref:`beats`, etc.), be sure to upgrade them to match the version of your upgraded components.

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

log_size_limit
--------------

``soup`` will check your :ref:`elasticsearch` ``log_size_limit`` values to see if they are over the recommended values. If so, it will ask you to update the values in ``/opt/so/saltstack/local/pillar/minions/``. When updating these files, please update any and all instances of ``log_size_limit`` as it may exist as ``elasticsearch:log_size_limit`` or ``manager:log_size_limit``.

Kibana
------

After ``soup`` completes, if :ref:`kibana` says ``Kibana server is not ready yet`` even after waiting a few minutes for it to fully initialize, then take a look at the Diagnostic Logging section of the :ref:`kibana` page.

Distributed deployments
-----------------------

If you have a distributed deployment with a manager node and separate sensor nodes and/or search nodes, you **only** need to run ``soup`` on the manager. Once ``soup`` has completed, other nodes should update themselves at the next :ref:`salt` highstate (typically within 15 minutes).

.. warning::

    Just because the update completed on the manager does NOT mean the upgrade is complete on other nodes in the grid. Do not manually restart anything until you know that all the search/heavy nodes in your deployment are updated. This is especially important if you are using true clustering for :ref:`elasticsearch`.

    Each minion is on a random 15 minute check-in period and things like network bandwidth can be a factor in how long the actual upgrade takes. If you have a heavy node on a slow link, it is going to take a while to get the containers to it. Depending on what changes happened between the versions, :ref:`elasticsearch` might not be able to talk to said heavy node until the update is complete. This will definitely be the case when upgrading to 2.3.40 because of the way the basic license SSL works.

    If it looks like you're missing data after the upgrade, please avoid restarting services and instead make sure at least one search node has completed its upgrade. The best way to do this is to run ``sudo salt-call state.highstate`` from a search node and make sure there are no errors. Typically if it works on one node it will work on the rest. Forward nodes are less complex and will update as they check in so you can monitor those from the :ref:`grid` section of :ref:`soc`.
    
When you run ``soup`` on the manager, it does the following:

- Checks to see if it is running on a manager.
- Checks to see if the grid is in :ref:`airgap` mode. If so, it will then ask for the location of the ISO or mount point.
- Checks to see if we're running the latest version of ``soup``. If not, it will put the latest in the correct place and ask you to re-run ``soup``.
- Compares the installed version with what is available on github or the ISO image.
- Checks to see if :ref:`salt` needs to be updated (more on this later).
- Downloads the new :ref:`docker` images or, if airgap, copies them from the ISO image.
- Stops the :ref:`salt` master and minion and restarts it in a restricted mode. This mode only allows the manager to connect to it so that we make sure the manager is done before any of the minions are updated.
- Updates :ref:`salt` if necessary. This will cause the master and minion services to restart but still in restricted mode.
- Makes any changes to pillars that are needed such as adding new settings or renaming values. This varies from release to release.
- If the grid is in :ref:`airgap` mode, then it copies the latest ET Open rules and yara rules to the manager.
- The new :ref:`salt` code is put into place on the manager.
- If :ref:`fleet` is enabled, then it generates new :ref:`osquery` packages.
- Runs a highstate on the manager which is the actual upgrade where it will use the new :ref:`salt` code and :ref:`docker` containers.
- Unlocks the :ref:`salt` master service and allows minions to connect again.
- Issues a command to all minions to update :ref:`salt` if necessary. This is important to note as it takes time to to update the :ref:`salt` minion on all minions. If the minion doesn't respond for whatever reason, it will not be upgraded at this time. This is not an issue because the first thing that gets checked when a minion talks to the master is if :ref:`salt` needs to be updated and will apply the update if it does.
- Nodes connect back to the manager and actually perform the upgrade to the new version.


