.. _so-elasticsearch-query:

so-elasticsearch-query
======================

You can use ``so-elasticsearch-query`` to submit a cURL request to the local Security Onion Elasticsearch host from the command line.

Usage
-----

::

   so-elasticsearch-query <PATH> [ARGS,...]

Where:

- PATH represents the elastic function being requested.
- ARGS is used to specify additional, optional curl parameters.

Examples
--------

::

   sudo so-elasticsearch-query /
   
::

   sudo so-elasticsearch-query '*:so-*/_search' -d '{"query": {"match_all": {}},"size": 1}' | jq
