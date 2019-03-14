Help
====

Having problems? Try the suggestions below.

-  Are you running the `latest version of Security Onion <Upgrade>`__?
-  Check the `FAQ <FAQ>`__.
-  Search the `Security Onion Mailing List <MailingLists>`__.
-  Search the documentation and mailing lists of the tools contained
   within Security Onion: `Tools <Tools>`__
-  Run ``sostat`` for some diagnostics:

   ::

       sudo sostat | less

-  If any of the NSM processes show up as failed, try restarting them:

   ::

       sudo service nsm restart

-  Check log files in ``/var/log/nsm/`` or other locations for any
   errors or possible clues:

   -  Setup ``/var/log/nsm/sosetup.log``
   -  Daily Log / PCAPs
      ``/nsm/sensor_data/{ HOSTNAME-INTERFACE }/dailylogs``
   -  sguil ``/var/log/nsm/securityonion/sguild.log``
   -  Suricata ``/var/log/nsm/{ HOSTNAME-INTERFACE }/suricata.log``
   -  barnyard2 ``/var/log/nsm/ { HOSTNAME-INTERFACE }/barnyard2.log``
   -  netsniff-ng
      ``/var/log/nsm/{ HOSTNAME-INTERFACE }/netsniff-ng.log``
   -  Bro ``/nsm/bro/logs/current``
   -  snort\_agent
      ``/var/log/nsm/{ HOSTNAME-INTERFACE }/snort_agent.log``
   -  Elasticsearch ``/var/log/elasticsearch/<hostname>.log``
   -  Kibana ``/var/log/kibana/kibana.log``
   -  Logstash ``/var/log/logstash/logstash.log``
   -  Elastalert ``/var/log/elastalert/elastalert_stderr.log``

-  If this is a sensor sending alerts to master server, is autossh
   running?

   ::

       sudo so-autossh-status

-  Having trouble with MySQL? Check all databases to see if any tables
   are are marked as crashed or corrupt.

   ::

       sudo mysqlcheck -A

-  Check specific MySQL databases by running something similar to the
   following:

   ::

       sudo mysqlcheck -c securityonion_db

-  Are you able to duplicate the problem on a fresh Security Onion installation?
-  Check the `Known Issues <https://github.com/Security-Onion-Solutions/security-onion/issues>`__ to see if this is a known issue that we are working on.
-  If all else fails, please send an email to our `security-onion mailing list <MailingLists>`__.
-  Need training or commercial support?
   https://www.securityonionsolutions.com

.. toctree::
   :maxdepth: 2

   faq
   DirectoryStructure
   Tools
   Passwords
   Support
   MailingLists
   TeamMembers
