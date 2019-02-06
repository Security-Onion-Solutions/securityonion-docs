Introduction
============

| Not long ago, the MISP project announced the ability to export NIDS
  rules created from events/indicators.
| https://www.circl.lu/doc/misp/automation/#get-eventsnids-nids-rules-export

We can leverage this functionality by quickly and easily setting up an
automated mechanism to pull NIDS rules from a MISP instance and add them
to our local rules for Security Onion. To do so, we just need to follow
the simple steps below:

Warning
=======

Please keep in mind we do not officially support this integration, so
installation is at your own risk.

Installation
============

| Clone the repo:
| ``git clone https://github.com/weslambert/securityonion-misp``

| Run the setup script:
| ``sudo securityonion-misp/so-misp-setup``

| Update rules (if desired):
| ``sudo rule-update``

| Confirm rules in place:
| ``grep -i misp /etc/nsm/rules/downloaded.rules``

| You should now be up and running!
| MISP rules will be downloaded via cron-job at the interval specified
  in ``/etc/cron.d/download-misp``.
