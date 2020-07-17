.. _playbook:

Playbook
========

Overview
--------

Playbook is a web application that allows you to create a Detection Playbook, which itself consists of individual plays. These plays are fully self-contained and describe the different aspects around the particular detection strategy.

.. image:: https://user-images.githubusercontent.com/1659467/87230271-c5cb0880-c37c-11ea-8a36-24cabf137ed2.png

The key components of a play are:

 #. Objective & Context - what exactly are we trying to accomplish and why?
 #. What are the follow-up actions required to validate and/or remediate when results are seen?
 #. The actual query needed to implement the play's objective. In our case, the :ref:`elastalert` / :ref:`elasticsearch` configuration.

Any high or critical severity results from a Play will generate an Alert within :ref:`hive`. Low and medium severity results are available to view within Hunt or Kibana.

The final piece to Playbook is automation. Once a Play is made active, the following happens:

 - The required :ref:`elastalert` config is put into production
 - Case Template for :ref:`hive` is created
 - :ref:`attack-navigator` layer is updated to reflect current coverage

Getting Started
----------

You can access Playbook by logging into :ref:`soc`, and clicking the Playbook link.

Creating a new Play
-------------------

To create a new play, click on the ``Sigma Editor`` menu link. Paste the Sigma signature into the Sigma field and then click Create. If successful, you will be redirected to the newly created Play.

Putting a Play into Production
------------------------------

When you are ready to start alerting on your Play, change the Status of the play to Active. This will create :ref:`hive` case template & the :ref:`elastalert` config. When results are found, an alert is created in :ref:`hive` - this alert will be linked to the Play as well as the case template.

User Accounts
------------------------------

By default, once a user has authenticated through SOC, they have can access Playbook without having to login again to the app itself - this anonymous access has the permissions of the analyst role. If you need your team to login with individual user accounts, you can disable this anonymous access and create new user accounts and add them to the analyst group - this will give them all the relevant permissions.

If you need administrator access to Playbook, you can login with the following admin credentials. However, the Playbook UI is designed to be used with a user that has an analyst role. Using an admin account will be very confusing to newcomers to Playbook, since many of the fields will now be shown and editable and it will look much more cluttered.

| Username: admin
| Password: changeme


Misc Notes
----------

Every 5 minutes, ``so-playbook-sync`` runs. This script queries Playbook for all active plays, and then checks to make sure that there is an :ref:`elastalert` config and TheHive case template for each play. It also runs through the same process for inactive plays.

Log Sources
-----------

Sigma support currently extends to the following log sources in Security Onion:
 - :ref:`osquery`
 - network (via :ref:`zeek` logs)
 - Windows Eventlogs + :ref:`sysmon` (via :ref:`osquery`)

Logging
-------
Playbook logs can be found in ``/opt/so/log/playbook/``.
