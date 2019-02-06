Why does Security Onion use UTC?
================================

| When you run Security Onion Setup, it sets the timezone to UTC/GMT
  because that is the recommended/required setting for Sguil:
| http://osdir.com/ml/security.sguil.general/2008-09/msg00003.html
| https://forums.snort.org/forums/linux/topics/barnyard-sguil-time-problem
| 
| Trying to use a non-UTC timezone can result in the following:

-  Time zones that have daylight saving time have a one-hour time warp
   twice a year. This manifests itself in Sguil not being able to pull
   transcripts for events within that one-hour time period. This is
   avoided by using UTC, since there is no daylight saving time.
-  Something similar can happen on a daily basis under certain
   conditions. If there is a discrepancy between the OS timezone and the
   Sguil UTC settings, then Sguil will be unable to pull transcripts for
   events in a window of time around midnight coinciding with the
   timezone's offset from UTC.

Additionally, UTC comes in quite handy when you have sensors in
different time zones and/or are trying to correlate events with other
systems or teams.

Squert and Kibana allow you to render event timestamps in your local
timezone. ELSA by default will render timestamps in the timezone of your
local browser (more info below) and Squert allows you to change your
timezone.

How do I change the timezone for Ubuntu?
========================================

When you run our Setup wizard, it should automatically set your timezone
to UTC. If you've already run Setup and then manually changed your
timezone to non-UTC and would like to switch back to UTC, you can
execute ``sudo dpkg-reconfigure tzdata``. Scroll to the bottom of the
Continents list and select ``None of the above``. In the second list,
select ``UTC``.
(http://askubuntu.com/questions/138423/how-do-i-change-my-timezone-to-utc-gmt)

How do I change the timezone in Squert?
=======================================

-  click the time interval (labeled INTERVAL)
-  on the right side, click the two arrows pointing right
-  de-select UTC
-  set your timezone offset (labeled TZ OFFSET)
-  click the "save TZ" button

Why are the timestamps in Kibana not in UTC?
============================================

By default, Kibana will display timestamps in the timezone of your local
browser. You can force Kibana to always display timestamps in UTC/GMT by
setting dateFormat:tz to ``UTC`` in Kibana (Management > Advanced
Settings) .

Why are the timestamps in ELSA not in UTC?
==========================================

| By default, ELSA will display timestamps in the timezone of your local
  browser. You can force ELSA to always display timestamps in UTC/GMT by
  configuring the ``use_utc`` setting in your ELSA Preferences panel.
| 
| Known issue in ELSA 713 (old ELSA package): If you access ELSA from a
  browser whose local timezone is not UTC and you haven't enabled the
  use\_utc setting in your ELSA Preferences, then each search rolls the
  From time back the same number of hours as the UTC offset. For
  example, suppose you login to ELSA and notice that the From defaults
  to 2013-05-05 18:01:50. When you then perform a search, the From
  changes to 2013-05-05 14:01:50.
| 
| The workaround is to enable the use\_utc setting in your ELSA
| Preferences (which is probably a good idea anyway to ensure that your
| timestamps in ELSA match your timestamps in Sguil/Squert):
| 

#. Navigate to ELSA -> Preferences:
#. Select Actions -> Add New Preference:
#. Enter the following into the new Preference:
   Type = default\_settings
   Name = use\_utc
   Value = 1
