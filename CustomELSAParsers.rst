How do I write custom ELSA parsers?
===================================

https://github.com/mcholste/elsa/wiki/Documentation#AddingParsers

http://www.balabit.com/sites/default/files/documents/syslog-ng-ose-3.3-guides/en/syslog-ng-ose-v3.3-guide-admin-en/html/reference_patterndb_schemes.html

Where do I put my custom ELSA parsers?
======================================

Create a new subdirectory in ``/etc/elsa/patterns.d/``, add your parsers
to the new subdirectory, and then use ``pdbtool`` to merge the entire
``/etc/elsa/patterns.d/`` directory into
``/opt/elsa/node/conf/patterndb.xml``. For example:

::

    # Create a new subdirectory in /etc/elsa/patterns.d/
    sudo mkdir /etc/elsa/patterns.d/local/

    # Add new parser
    sudo nano /etc/elsa/patterns.d/local/my_new_log_parser

    # Test new parser
    pdbtool test /etc/elsa/patterns.d/local/my_new_log_parser

    # Backup existing patterndb.xml
    sudo cp /opt/elsa/node/conf/patterndb.xml /opt/elsa/node/conf/patterndb.xml.bak

    # Merge all patterns into new patterndb.xml
    sudo pdbtool merge -p /opt/elsa/node/conf/patterndb.xml --recursive -D /etc/elsa/patterns.d/

    # Restart syslog-ng
    sudo service syslog-ng restart

Palo Alto default log format parser
-----------------------------------

https://groups.google.com/forum/#!topic/enterprise-log-search-and-archive/SJwOY7N2A60
