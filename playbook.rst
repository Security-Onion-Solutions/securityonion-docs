.. _playbook:

Playbook
========

:ref:`soc` includes a link on the sidebar that takes you to Playbook which allows you to create a **Detection Playbook**, which itself consists of individual **Plays**. These Plays are fully self-contained and describe the different aspects around a particular detection strategy.

.. image:: https://user-images.githubusercontent.com/1659467/87230271-c5cb0880-c37c-11ea-8a36-24cabf137ed2.png
 :target: https://user-images.githubusercontent.com/1659467/87230271-c5cb0880-c37c-11ea-8a36-24cabf137ed2.png

The key components of a Play are:

 #. Objective and context - what exactly are we trying to detect and why?
 #. What are the follow-up actions required to validate and/or remediate when results are seen?
 #. The actual query needed to implement the Play's objective. In our case, the :ref:`elastalert` / :ref:`elasticsearch` configuration.

Any results from a Play (low, medium, high, critical severity) are available to view within :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana`. High or critical severity results from a Play will generate an Alert within the Security Onion Console :ref:`alerts` interface.

The final piece to Playbook is automation. Once a Play is made active, the following happens:

 - The required :ref:`elastalert` config is put into production
 - :ref:`attack-navigator` layer is updated to reflect current coverage

Getting Started
---------------

You can access Playbook by logging into :ref:`soc` and clicking the Playbook link. You will see over 500 plays already created that have been imported from the Sigma Community repostory of rules at https://github.com/Neo23x0/sigma/tree/master/rules.

Creating a new Play
-------------------

Plays are based on Sigma rules - from https://github.com/Neo23x0/sigma:

    Sigma is a generic and open signature format that allows you to describe relevant log events in a straightforward manner. The rule format is very flexible, easy to write and applicable to any type of log file. The main purpose of this project is to provide a structured form in which researchers or analysts can describe their once developed detection methods and make them shareable with others.

To create a new play, click on the ``Sigma Editor`` menu link. Either ``Load`` a sample Sigma rule or paste one into the Sigma field and click ``Convert``. This will convert the Sigma into a query that you can use in :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana` to confirm that it will work for your target log.  

Refer to the Log Sources and Field Names section below for details around what field names to use in the Sigma etc.

Once you are ready to create the Play, click ``Create Play From Sigma``. If the Play creation is successful, you will be redirected to the newly created Play - it will have a status of ``Draft``.

The lifecycle of a Play is as follows: 
 #. Draft (Initial state)  
 #. Active (In Production)  
 #. Inactive (Temporarily moved out of production)  
 #. Archived (Play has been superseded/retired)  

A Play can also have the status of Disabled, which means that it is broken in some way and should not be made Active.

Editing a Play
--------------

Click on ``Edit`` to edit a Play. There will only be a few fields that you can modify - to make edits to the others (``Title``, ``Description``, etc), you will need to edit the Sigma inside the Sigma field. Keep in mind that the Sigma is YAML formatted, so if you have major edits to make it is recommended to lint it and/or ``Convert`` it through the Sigma Editor to confirm that it is formatted correctly. Be sure to remove the prepended and postpended Playbook-specific syntax highlighting before linting/converting - ``{{collapse(View Sigma) <pre><code class="yaml">`` and ``</code></pre>}}``.

Once you save your changes, Playbook will update the rest of the fields to match your edits, including regenerating the Elastalert rule if needed.

Putting a Play into Production
------------------------------

When you are ready to start alerting on your Play, change the Status of the play to ``Active``. This will create the :ref:`elastalert` config. Any edits made to the Play in Playbook will automatically update the :ref:`elastalert` configuration.

The Elastalert rules are located under ``/opt/so/rules/elastalert/playbook/<PlayID>.yaml``. Elastalert rules created by Playbook will run every 3 minutes, with a ``buffer_time`` of 15 minutes.

Performance testing is still ongoing. We recommend avoiding the ``Malicious Nishang PowerShell Commandlets`` play as it can cause serious performance problems. You may also want to avoid others with a status of ``experimental``.

Viewing Playbook Alerts
-----------------------

When results from your Plays are found (ie alerts), they are available to view within :ref:`alerts`.

Tuning Plays
------------

If you have a Play that is generating false positives, you can tune it by adding a `Custom Filter` to the Play.

For example, suppose you are seeing a large amount of ``Suspicious Service Path Modification`` alerts. Drilling down into the alerts, it appears to be a legitimate configuration change by one of the IT Ops Service Accounts. This can be tuned out by doing the following:

- Open the Play and click ``Edit``
- Add the following filter in the ``Custom Filter`` field (YAML Formatting!):

::

  sofilter:
    User: SA_ITOPS

The ``sofilter`` syntax is important - add as many top-level filter clauses as you need, but they should all start with ``sofilter`` - for example ``sofilter1``, ``sofilter2``

- Click ``Submit`` and Playbook will take care of the rest, which includes automatically adding the custom filter to the rule when it is converted.

Custom filters are applied right away (written out to the backend ElastAlert rule file), but ElastAlert could take a couple minutes to pick up on the change, as it runs rules every 3 minutes.

It is not recommended to edit the Sigma directly for Community rules, as if there is ever an update for that Sigma rule from the Sigma rules repo, your changes will get overwritten.

Finally, if you are seeing legitimate executions that are not unique to your environment, you might consider submitting a PR to the rule in the Sigma repo (https://github.com/SigmaHQ/sigma/tree/master/rules).

User Accounts
-------------

By default, once a user has authenticated through SOC they can access Playbook without having to login again to the app itself. This anonymous access has the permissions of the analyst role. 

If you need administrator access to Playbook, you can login as ``admin`` with the randomized password found via ``sudo salt-call pillar.get secrets``. However, the Playbook UI is designed to be used with a user that has an analyst role. Using an admin account will be very confusing to newcomers to Playbook, since many of the fields will now be shown/editable and it will look much more cluttered.

Disable Anonymous Access and Create User Accounts
-------------------------------------------------

If you need your team to login with individual user accounts, you can disable anonymous access and create new user accounts and add them to the analyst group which will give them all the relevant permissions. 

To do this, login with a user that has administrative access, and navigate to Administration --> Users --> New User. Fill out the relevant fields. By default, Playbook is not connected to an email server so password resets via email will not work. Once the new user has been created, go back to Administration --> Users and select the newly created user. There will be a Groups tab, from which you can add the user to the Analyst group. This will give the user all the needed permissions.

To disable anonymous access, login with a user that has administrative access and navigate to Administration --> Projects --> Detection Playbooks. Unselect the Public checkbox.


Misc Notes
----------

``so-playbook-sync`` runs every 5 minutes. This script queries Playbook for all active plays and then checks to make sure that there is an :ref:`elastalert` config for each play. It also runs through the same process for inactive plays.

Log Sources and Field Names
---------------------------

Sigma support currently extends to the following log sources in Security Onion:
 - Windows Eventlogs and :ref:`sysmon` (via :ref:`elastic-agent`)
 - osquery (via :ref:`elastic-agent`)
 - network (via :ref:`zeek` logs)

The pre-loaded Plays depend on Sysmon and Windows Eventlogs shipped with :ref:`elastic-agent`.

For best compatibility, use the following Sigma Taxonomy:
 - Process Creation: https://github.com/Neo23x0/sigma/wiki/Taxonomy#process-creation-events
 - Network: https://github.com/Neo23x0/sigma/wiki/Taxonomy#specific
 
The current Security Onion Sigmac field mappings can be found here: https://github.com/Security-Onion-Solutions/securityonion-image/blob/master/so-soctopus/so-soctopus/playbook/securityonion-baseline.yml

.Security subfield
------------------

Playbook uses the ``.security`` subfield that is generated by a special analyzer (https://github.com/neu5ron/es_stk). This analyzer allows case insensitive wildcard searches and is designed specifically for security logs.

Adding Additional Rulesets
--------------------------

As previously mentioned, the pre-loaded Plays come from the community Sigma repository at https://github.com/Neo23x0/sigma/tree/master/rules. The default config is to only pull in the Windows rules. The rest of the rules from the community repository can be pulled in by editing a pillar value under ``/opt/so/saltstack/local/pillar/global.sls``:

::

  soctopus:
    playbook:
      rulesets:
        - windows
      
Add one or more of the following:

``application,cloud,compliance,linux,macos,network,proxy,web``

These are based on the top level directories from the Sigma community repository rule's folder.

Next, restart SOCtopus:

::

  so-soctopus-restart

Finally, tell Playbook to pull in the new rules:

::

  so-playbook-ruleupdate

This can take a few minutes to complete if pulling in a large amount of new rules.

Diagnostic Logging
------------------

Playbook logs can be found in ``/opt/so/log/playbook/``. Depending on what you're looking for, you may also need to look at the :ref:`docker` logs for the container:

::

        sudo docker logs so-playbook

More Information
----------------

.. seealso::

	Check out our Detecting Hashes video at https://youtu.be/pK8mS60Sk5s!
