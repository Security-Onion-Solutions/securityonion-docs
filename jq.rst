.. _jq:

jq
==

From https://stedolan.github.io/jq/:

    jq is like sed for JSON data - you can use it to slice and filter and map and transform structured data with the same ease that sed, awk, grep and friends let you play with text.
    
Usage
-----

We configure :ref:`zeek` to write logs in JSON format. If you want to parse those logs from the command line, then you can use ``jq``.  Here's a basic example:

::

   jq '.' /nsm/zeek/logs/current/conn.log
   
This command will parse all of the records in ``/nsm/zeek/logs/current/conn.log``.  For each of the records, it will then output every field and its value.

More Information
----------------

For more information about ``jq``, please see https://stedolan.github.io/jq/.
