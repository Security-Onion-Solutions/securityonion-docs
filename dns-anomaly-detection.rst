.. _dns-anomaly-detection:

DNS Anomaly Detection
=====================

Dr. Johannes Ullrich of the SANS Internet Storm Center posted a great DNS Anomaly Detection script based on the query logs coming from his DNS server. We can do the same thing with :ref:`zeek`'s dns.log (where :ref:`zeek` captures all the DNS queries it sees on the network).

.. note::

    Please note that the following script is only intended for standalone machines and will not work properly on distributed deployments. Another option which might work better is :ref:`elastalert` and its ``new_term`` rule.

Thanks to ``senatorhotchkiss`` on our mailing list for updating the original script to replace ``bro-cut`` with ``jq``:

::

    #!/bin/bash

    ZEEK_LOGS="/nsm/zeek/logs"
    TODAY=`date +%Y-%m-%d`
    YESTERDAY=`date -d yesterday +%Y-%m-%d`
    OLD_DIRS=`ls $ZEEK_LOGS | grep "20*-*" | egrep -v "current|stats|$TODAY|$YESTERDAY"`
    TMPDIR=/tmp
    OLDLOG=$TMPDIR/oldlog
    NEWLOG=$TMPDIR/newlog
    SUSPECTS=$TMPDIR/suspects

    for DIR in $OLD_DIRS; do zcat $ZEEK_LOGS/$DIR/dns* | jq '{"id.resp_p"},{"query"}' ; done  | grep -v "^5353" | awk '{print $2}' | sort | uniq -c | sort -k2 > $OLDLOG
    zcat $ZEEK_LOGS/$YESTERDAY/dns* | jq '{"id.resp_p"},{"query"}' | grep -v "^5353" | awk '{print $2}' | sort | uniq -c | sort -k2 > $NEWLOG
    join -1 2 -2 2  -a 2 $OLDLOG $NEWLOG | egrep -v '.* [0-9]+ [0-9]+$' | sort -nr -k2 | head -50 > $SUSPECTS

    echo
    echo "===================================="
    echo "Top 50 First Time Seen DNS queries:"
    echo "===================================="
    cat $SUSPECTS


