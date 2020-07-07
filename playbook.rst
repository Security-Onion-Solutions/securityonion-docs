.. _playbook:

Playbook
========

Overview
--------

Playbook is a web application that allows you to create Detection Playbooks, which itself consists of individual plays. These plays are fully self-contained and describe the different aspects around the particular detection strategy.

The key components of a play are:

 #. Objective & Context - what exactly are we trying to accomplish and why
 #. What are the follow-up actions required to validate and/or remediate when results are seen
 #. The actual query needed to implement the play's objective. In our case, the ElastAlert / Elasticsearch configuration.

Any results from a Play will generate an Alert within TheHive.

The final piece to Playbook is automation. Once a Play is made active, the following happens:

 - The required ElastAlert config is put into production
 - Case Template for TheHive is created
 - ATT&CK Navigator layer is updated to reflect current coverage

Logging in
----------

You can access Playbook by navigating to: https://MASTER/playbook and login with the following credentials:

| Username: analyst
| Password: changeme

If you need administrator access to Playbook, you can login with the following credentials - however, the Playbook UI is designed to be used with a user that has an analyst role - using an admin account will be very confusing to newcomers to Playbook, since many of the fields will now be shown and editable - it will look much more cluttered.

| Username: admin
| Password: changeme

Creating a new Play
-------------------

To create a new play, click on the Sigma Editor menu link. Paste the Sigma signature into the Sigma field and then click Create. If successful, you will be redirected to the newly created Play.

Putting a Play into Production
------------------------------

When you are ready to start alerting on your Play, change the Status of the play to Active. This will create TheHive case template & the ElastAlert config. When results are found, an alert is created in TheHive - this alert will be linked to the Play as well as the case template.

Misc Notes
----------

Every 5 minutes, so-playbook-sync runs. This script queries Playbook for all active plays, and then checks to make sure that there is an Elastalert config & TheHive case template for each play. It also runs through the same process for inactive plays.

Quick test
----------

Import the following Sigma and enable the Play - it alerts on bro_http events, so expect to get a number of alerts in TheHive.

https://gist.github.com/defensivedepth/3b0656569a797d86eb04068b5546b78c

Log Sources
-----------

Sigma support currently extends to the following logsources in Security Onion
 - osquery
 - network (via bro logs)
 - Windows Eventlogs + Sysmon (via osquery)
