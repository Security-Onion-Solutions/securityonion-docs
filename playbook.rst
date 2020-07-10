.. _playbook:

Playbook
========

Overview
--------

Playbook is a web application that allows you to create a Detection Playbook, which itself consists of individual plays. These plays are fully self-contained and describe the different aspects around the particular detection strategy.

The key components of a play are:

 #. Objective & Context - what exactly are we trying to accomplish and why?
 #. What are the follow-up actions required to validate and/or remediate when results are seen?
 #. The actual query needed to implement the play's objective. In our case, the :ref:`elastalert` / :ref:`elasticsearch` configuration.

Any results from a Play will generate an Alert within :ref:`hive`.

The final piece to Playbook is automation. Once a Play is made active, the following happens:

 - The required :ref:`elastalert` config is put into production
 - Case Template for :ref:`hive` is created
 - :ref:`attack-navigator` layer is updated to reflect current coverage

Logging in
----------

You can access Playbook by going to :ref:`soc`, clicking the Playbook link, and then logging in with the following credentials:

| Username: analyst
| Password: changeme

If you need administrator access to Playbook, you can login with the following admin credentials. However, the Playbook UI is designed to be used with a user that has an analyst role. Using an admin account will be very confusing to newcomers to Playbook, since many of the fields will now be shown and editable and it will look much more cluttered.

| Username: admin
| Password: changeme

Creating a new Play
-------------------

To create a new play, click on the ``Sigma Editor`` menu link. Paste the Sigma signature into the Sigma field and then click Create. If successful, you will be redirected to the newly created Play.

Putting a Play into Production
------------------------------

When you are ready to start alerting on your Play, change the Status of the play to Active. This will create :ref:`hive` case template & the :ref:`elastalert` config. When results are found, an alert is created in :ref:`hive` - this alert will be linked to the Play as well as the case template.

Misc Notes
----------

Every 5 minutes, ``so-playbook-sync`` runs. This script queries Playbook for all active plays, and then checks to make sure that there is an :ref:`elastalert` config and TheHive case template for each play. It also runs through the same process for inactive plays.

Quick test
----------

If you want to do a quick test, import the following Sigma and then enable the Play:

https://gist.github.com/defensivedepth/3b0656569a797d86eb04068b5546b78c

This play alerts on Zeek HTTP events, so expect to get a number of alerts in TheHive.

Log Sources
-----------

Sigma support currently extends to the following log sources in Security Onion:
 - :ref:`osquery`
 - network (via :ref:`zeek` logs)
 - Windows Eventlogs + :ref:`sysmon` (via :ref:`osquery`)

Logging
-------
Playbook logs can be found in ``/opt/so/log/playbook/``.
