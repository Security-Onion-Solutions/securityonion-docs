GA now available
================

| Our Elastic Stack integration has reached General Availability! We
  highly recommend performing a fresh installation rather than trying to
  upgrade pre-release installations!
| https://blog.securityonion.net/2018/04/security-onion-elastic-stack-general.html

Warning
=======

Our Elastic integration is still considered experimental and so the
usual warnings and disclaimers apply:

Experimental Setup is BLEEDING EDGE and TOTALLY UNSUPPORTED!

-  If this breaks your system, you get to keep both pieces!
-  This is a work in progress and is in constant flux.
-  Do NOT run this on a system that you care about!
-  Do NOT run this on a system that has data that you care about!
-  This should only be run on a TEST box with TEST data!
-  Experimental Setup may result in nausea, vomiting, or a burning
   sensation.

NOT Officially Supported
========================

Performing an in-place upgrade from previous Alpha/Beta/RC releases to
the current Release Candidate is NOT officially supported. If you're
currently running RC1, here are the steps you can try to update to RC2.
If you encounter any issues, please perform a fresh installation of the
current Release Candidate.

Distributed Deployments
=======================

If you're updating a distributed deployment, please perform the
following steps on the master server before upgrading any sensors.

Updating
========

First, update all packages:

::

    sudo soup

Then restart services:

::

    sudo so-restart

Bro Logs
========

Please note that RC2 configures Bro to output in JSON for higher
performance and better parsing. We recommend that most folks leave Bro
configured for JSON output. If you switch from JSON back to the original
tab separated values (TSV) format, you may run into field conflict
issues. These field conflict issues will be resolved in RC3. If you
really need the traditional Bro TSV format and are willing to risk field
conflict issues, you can disable JSON:

::

    sudo sed -i 's|@load json-logs|#@load json-logs|g' /opt/bro/share/bro/site/local.bro

and then restart Bro:

::

    sudo nsm_sensor_ps-restart --only-bro
