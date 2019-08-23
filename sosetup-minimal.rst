sosetup-minimal
===============

``sosetup-minimal`` is a wrapper around our traditional ``sosetup`` script that configures the box to run using minimal resources.

It will run Setup and then do the following:

-  stop and disable elastalert
-  stop and disable freqserver
-  stop and disable domainstats
-  set Elasticsearch to a 400MB heap size
-  set Logstash to ``LOGSTASH_MINIMAL`` mode and set a 200MB heap size

Requirements:

-  You must have at least 4GB RAM.
