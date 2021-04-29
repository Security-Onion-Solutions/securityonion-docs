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
    
Security Onion enables the native Community ID support in both :ref:`zeek` and :ref:`suricata`. 

We sponsored the development of Community ID support in :ref:`osquery`:

https://dactiv.llc/blog/correlate-osquery-network-connections/

For tools that don't natively support Community ID, we sponsored the development of an :ref:`elasticsearch` Ingest Processor to automatically generate Community ID values:

https://github.com/Security-Onion-Solutions/elasticsearch-ingest-community-id

More Information
----------------

.. seealso::

    | For more information about Community ID, please see:
    | https://github.com/corelight/community-id-spec
