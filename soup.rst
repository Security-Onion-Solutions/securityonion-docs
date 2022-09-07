.. _soup:

soup
====

``soup`` stands for ``Security Onion UPdater``.  To install updates, run the ``soup`` command:

::

	sudo soup

If necessary, ``soup`` will update itself and then ask you to run ``soup`` again. Once ``soup`` is fully updated, it will then check for other updates. This includes Security Onion version updates, Security Onion hotfixes, and operating system (OS) updates.

After running ``soup`` or rebooting a Security Onion node, it may take a few minutes for services to display an ``OK`` status when running :ref:`so-status`. This may be due to the intial on-boot :ref:`salt` highstate running. If services do not appear to be fully up and running within 15 minutes, try running the following command:

::

	sudo salt-call state.highstate

.. warning::

	If you have a production deployment, we recommend that you test the upgrade process on a test deployment if possible before deploying to production.

Security Onion Version Updates
------------------------------

When we release a new version of Security Onion, we update the :ref:`release-notes` section and publish a blog post to https://blog.securityonion.net. You'll want to review these for any relevant information about the individual updates. 

If ``soup`` finds a full version update, then it will update the Security Onion version in ``/etc/soversion``, all :ref:`salt` code, and all :ref:`docker` images.

``soup`` automatically keeps the previous version of :ref:`docker` images. These older unused :ref:`docker` images will be automatically removed at the next version update. If you need to remove these older :ref:`docker` images immediately, first verify that the upgrade completed successfully and that everything is working properly. You could then remove the older images individually or all at once using a command like:

::

	sudo docker system prune -a

However, please note that this an aggressive option and you should exercise caution if you have any non-standard :ref:`docker` images or configuration. You may want to test it on a test system first.

Security Onion Hotfixes
-----------------------

``soup`` checks for Security Onion hotfixes. Hotfixes typically include updates to the :ref:`salt` code and small configuration changes that do not warrant a full version update. This does not include Docker images since that would require a full version update. 

After applying a hotfix, you may notice that the Security Onion version in ``/etc/soversion`` stays the same. The application of the hotfix is tracked on the manager in the ``/etc/sohotfix`` file.

OS Updates
----------

There is an option during :ref:`Configuration` to automatically install OS updates.

``soup`` checks for missing OS updates and ask if you want to install them.

Local Configurations
--------------------

``soup`` will check for local configurations in ``/opt/so/saltstack/local/`` that may cause issues and flag them with the message ``Potentially breaking changes found in the following files``. Please examine the output of ``soup`` and review any local configurations for possible issues.

Log
---

If ``soup`` displays any errors, you can check ``/root/soup.log`` for additional clues.

ssh
---

If you run soup via ssh and the ssh session terminates, then any processes running in that session would terminate. You should avoid leaving soup unattended especially if the machine you are ssh'ing from is configured to sleep after a period of time. You might also consider using something like screen or tmux so that if your ssh session terminates, the processes will continue running on the server.

Airgap
------

When you run ``soup`` on an :ref:`airgap` install, it will ask for the location of the upgrade media. You can do one of the following:

- burn the latest ISO image to a DVD and insert it in the DVD drive

- flash the ISO image to a USB drive and insert that USB drive

- simply copy the ISO file itself to the airgapped manager

You can also specify the path on the command line using the ``-f`` option. For example (change this to reflect the actual path to the ISO image):

::

	sudo soup -y -f /home/YourUser/securityonion-2.4.XYZ-YYYYMMDD.iso
	
Agents
------

If you've previously added any external agents (:ref:`wazuh`, :ref:`beats`, etc.), be sure to upgrade them to match the version of your upgraded components.

log_size_limit
--------------

``soup`` will check your :ref:`elasticsearch` ``log_size_limit`` values to see if they are over the recommended values. If so, it will ask you to update the values in ``/opt/so/saltstack/local/pillar/minions/``. When updating these files, please update any and all instances of ``log_size_limit`` as it may exist as ``elasticsearch:log_size_limit`` or ``manager:log_size_limit``.

Kibana
------

After ``soup`` completes, if :ref:`kibana` says ``Kibana server is not ready yet`` even after waiting a few minutes for it to fully initialize, then take a look at the Diagnostic Logging section of the :ref:`kibana` page.

If Kibana loads but the dashboards display errors that they didn't before the upgrade, first shift-reload your browser to make sure there are no cache issues. If that doesn't resolve the issue, then you may need to reload the dashboards on your manager:

::

	sudo rm /opt/so/state/kibana_*.txt
	sudo salt-call state.apply kibana.so_savedobjects_defaults -l info queue=True

Automation
----------

``soup`` can be automated as follows (assuming you've previously accepted the Elastic license):

::

	sudo soup -y

This will make ``soup`` proceed unattended, automatically answering ``yes`` to any prompt.  If you have an airgap installation, you can specify the path to the ISO image using the ``-f`` option as follows:

::

	sudo soup -y -f /home/user/securityonion.iso
	
Errors
------

Pillars and sls files
~~~~~~~~~~~~~~~~~~~~~

``soup`` will check :ref:`salt` pillars to make sure they can be rendered. If not, it will output a message like this:

::

	There is an issue rendering the manager's pillars. Please correct the issues in the sls files mentioned below before running SOUP again.

This usually means that somebody has modified the :ref:`salt` sls files and introduced a typo. 

Downloading images
~~~~~~~~~~~~~~~~~~

As ``soup`` is downloading container images, it may encounter errors if there are Internet connection issues or if the disk runs out of free space. Once you've resolved the underlying condition, you can manually refresh your container images using ``so-docker-refresh``.

Highstate already running
~~~~~~~~~~~~~~~~~~~~~~~~~

Here are some other errors that you may see when running ``soup``:

::

    local:
        Data failed to compile:
    ----------
        Rendering SLS 'base:common' failed: Jinja variable 'list object' has no attribute 'values'
        
and/or

::

    There is a problem downloading the so-xyz:2.4.0 image. Details: 
    gpg: Signature made Thu 18 Feb 2021 02:26:10 PM UTC using RSA key ID FE507013 gpg: BAD signature from "Security Onion Solutions, LLC <info@securityonionsolutions.com>"
    
If you see these errors, it most likely means that a salt highstate process was already running when ``soup`` began. You can wait a few minutes and then try ``soup`` again. Alternatively, you can run ``sudo salt-call state.highstate`` and wait for it to complete before running ``soup`` again.

Distributed deployments
-----------------------

If you have a distributed deployment with a manager node and separate sensor nodes and/or search nodes, you **only** need to run ``soup`` on the manager. Once ``soup`` has completed, other nodes should update themselves at the next :ref:`salt` highstate (typically within 15 minutes).

.. warning::

    Just because the update completed on the manager does NOT mean the upgrade is complete on other nodes in the grid. Do not manually restart anything until you know that all the search/heavy nodes in your deployment are updated. This is especially important if you are using true clustering for :ref:`elasticsearch`.

    Each minion is on a random 15 minute check-in period and things like network bandwidth can be a factor in how long the actual upgrade takes. If you have a heavy node on a slow link, it is going to take a while to get the containers to it. Depending on what changes happened between the versions, :ref:`elasticsearch` might not be able to talk to said heavy node until the update is complete.

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


