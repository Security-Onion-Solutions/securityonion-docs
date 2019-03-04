UTC and Time Zones
==================

| When you run Security Onion Setup, it sets the timezone to UTC/GMT
  because that is the recommended/required setting for Sguil:
| http://osdir.com/ml/security.sguil.general/2008-09/msg00003.html
| https://forums.snort.org/forums/linux/topics/barnyard-sguil-time-problem
| 
| Trying to use a non-UTC timezone can result in the following:

-  Time zones that have daylight saving time have a one-hour time warp twice a year. This manifests itself in Sguil not being able to pull transcripts for events within that one-hour time period. This is avoided by using UTC, since there is no daylight saving time.
-  Something similar can happen on a daily basis under certain conditions. If there is a discrepancy between the OS timezone and the Sguil UTC settings, then Sguil will be unable to pull transcripts for events in a window of time around midnight coinciding with the timezone's offset from UTC.

Additionally, UTC comes in quite handy when you have sensors in different time zones and/or are trying to correlate events with other systems or teams.

Kibana by default will render timestamps in the timezone of your local browser (more info below) and Squert allows you to set your timezone.

How do I change the timezone for Ubuntu?
----------------------------------------

When you run our Setup wizard, it should automatically set your OS timezone to UTC. If you've already run Setup and then manually changed your timezone to non-UTC and would like to switch back to UTC, you can execute ``sudo dpkg-reconfigure tzdata``. Scroll to the bottom of the Continents list and select ``None of the above``. In the second list, select ``UTC``.
(http://askubuntu.com/questions/138423/how-do-i-change-my-timezone-to-utc-gmt)
