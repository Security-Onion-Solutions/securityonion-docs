.. _help:

Help
====

Having problems? Try the suggestions below.

-  Have you run :ref:`soup` to ensure that you're on the latest version?
-  Check the :ref:`faq`.
-  Search the :ref:`community-support` forum.
-  Search the documentation and support forums of the tools contained within Security Onion: :ref:`tools`
-  Check log files in ``/opt/so/log/`` or other locations for any errors or possible clues:

   -  Setup ``/root/sosetup.log``
   -  Suricata ``/opt/so/log/suricata/suricata.log``
   -  Zeek ``/nsm/zeek/logs/current/``
   -  Elasticsearch ``/opt/so/log/elasticsearch/<hostname>.log``
   -  Kibana ``/opt/so/log/kibana/kibana.log``
   -  Logstash ``/opt/so/log/logstash/logstash.log``
   -  Elastalert ``/opt/so/log/elastalert/elastalert_stderr.log``

-  Are you able to duplicate the problem on a fresh Security Onion installation?
-  Check the `Known Issues <https://github.com/Security-Onion-Solutions/securityonion/issues>`__ to see if this is a known issue that we are working on.
-  If all else fails, please feel free to reach out for :ref:`support`.

.. toctree::
   :maxdepth: 2

   faq
   directory
   tools
   support
   community-support
   help-wanted
