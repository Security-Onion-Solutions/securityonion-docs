jq
==

From https://stedolan.github.io/jq/:

    jq is like sed for JSON data - you can use it to slice and filter and map and transform structured data with the same ease that sed, awk, grep and friends let you play with text.
    
Usage
-----

If you have `<Bro>`_ configured to write logs in json format and you want to parse those logs from the command line, then you can use ``jq``:

::

   jq '.' /nsm/bro/logs/current/conn.log
   
This command will parse ``/nsm/bro/logs/current/conn.log`` and then output every field of every line.

More Information
----------------

| For more information about jq, please see:
| https://stedolan.github.io/jq/
