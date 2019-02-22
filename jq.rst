jq
==

From https://stedolan.github.io/jq/:

    jq is like sed for JSON data - you can use it to slice and filter and map and transform structured data with the same ease that sed, awk, grep and friends let you play with text.
    
Usage
-----

If you have Bro configured to write logs in json format, then you can use jq to parse those json logs.  For example:

::

   jq '.' /nsm/bro/logs/current/conn.log
   
This command will parse ``/nsm/bro/logs/current/conn.log`` and then output every field of every line.

More Information
----------------

| For more information about jq, please see:
| https://stedolan.github.io/jq/
