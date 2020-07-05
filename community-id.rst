Community ID
============

From https://github.com/corelight/community-id-spec:

  ::
    
      When processing flow data from a variety of monitoring applications (such as Zeek and Suricata), 
      it's often desirable to pivot quickly from one dataset to another. While the required flow tuple 
      information is usually present in the datasets, the details of such "joins" can be tedious, 
      particular in corner cases. This spec describes "Community ID" flow hashing, standardizing the 
      production of a string identifier representing a given network flow, to reduce the pivot to a 
      simple string comparison.
    
We enable the default Community ID support in both Zeek and Suricata. For tools that don't natively support it, 
we sponsored the development of an Elasticsearch Ingest Processor to automaticaly generate Community ID values:

https://github.com/Security-Onion-Solutions/elasticsearch-ingest-community-id
