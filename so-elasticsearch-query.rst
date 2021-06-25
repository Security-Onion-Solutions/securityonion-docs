.. _so-elasticsearch-query:

so-elasticsearch-query
======================

Starting in Security Onion 2.3.60, so-elasticsearch-query submits a cURL request to the local Security Onion Elasticsearch host.

Usage: ./so-elasticsearch-query <PATH> [ARGS,...]

Where:
   PATH represents the elastic function being requested.
   ARGS is used to specify additional, optional curl parameters.

Examples:

::
   so-elasticsearch-query /

   so-elasticsearch-query '*:so-*/_search' -d '{"query": {"match_all": {}},"size": 1}' | jq
