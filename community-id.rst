.. _community-id:

Community ID
============

From https://github.com/corelight/community-id-spec:
    
    When processing flow data from a variety of monitoring applications (such as Zeek and Suricata), 
    it's often desirable to pivot quickly from one dataset to another. While the required flow tuple 
    information is usually present in the datasets, the details of such "joins" can be tedious, 
    particular in corner cases. This spec describes "Community ID" flow hashing, standardizing the 
    production of a string identifier representing a given network flow, to reduce the pivot to a 
    simple string comparison.
    
Security Onion enables the built-in Community ID support in both :ref:`zeek` and :ref:`suricata`. 

For logs that don’t naturally include Community ID, we use the Elasticsearch Community ID processor:
https://www.elastic.co/guide/en/elasticsearch/reference/current/community-id-processor.html

:ref:`dashboards` includes a Community ID dashboard that will show all logs with that value.

More Information
----------------

.. note::

    | For more information about Community ID, please see:
    | https://github.com/corelight/community-id-spec
