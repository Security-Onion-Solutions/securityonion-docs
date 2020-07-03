Help
====

Having problems? Try the suggestions below.

-  Are you running the `latest version of Security Onion <Upgrade>`__?
-  Check the `FAQ <FAQ>`__.
-  Search the `Security Onion Mailing List <MailingLists>`__.
-  Search the documentation and mailing lists of the tools contained within Security Onion: `Tools <Tools>`__
-  Check log files in ``/var/log/nsm/`` or other locations for any errors or possible clues:

   -  Setup ``/var/log/nsm/sosetup.log``
   -  Suricata ``/var/log/nsm/{ HOSTNAME-INTERFACE }/suricata.log``
   -  Zeek ``/nsm/bro/logs/current``
   -  Elasticsearch ``/var/log/elasticsearch/<hostname>.log``
   -  Kibana ``/var/log/kibana/kibana.log``
   -  Logstash ``/var/log/logstash/logstash.log``
   -  Elastalert ``/var/log/elastalert/elastalert_stderr.log``

-  Are you able to duplicate the problem on a fresh Security Onion installation?
-  Check the `Known Issues <https://github.com/Security-Onion-Solutions/security-onion/issues>`__ to see if this is a known issue that we are working on.
-  If all else fails, please send an email to our `security-onion mailing list <MailingLists>`__.
-  Need training or commercial support?
   https://www.securityonionsolutions.com

.. toctree::
   :maxdepth: 2

   faq
   directory
   tools
   support
   mailing-lists
   help-wanted
