Introduction
============

The following are posts from Martin Holste, the author of ELSA,
extracted from the Security Onion and Security Onion Testing mailing
lists, that provide insight and working examples of the power of ELSA's
query capabilities.

| Also see the ELSA documentation:
| https://github.com/mcholste/elsa/wiki/Documentation

12/11/12 - [security-onion-testing]
===================================

In any case, be sure to check out the documentation for [subsearches]
(https://github.com/mcholste/_elsa/wiki/Documentation#Subsearches) as
that's where you get the really powerful queries from.

The queries from today were like this (note that you can always replace
``groupby`` with using the ``Report On`` menu button):

Show NIDS alerts containing ``current events`` or ``trojan``:

::

       sig_msg:current_events or sig_msg:trojan groupby:sig_msg

Choose ``ET POLICY Proxy Judge Discovery/Evasion (prxjdg.cgi)`` from the
signature list, which executes:

::

       sig_msg:"ET POLICY Proxy Judge Discovery/Evasion (prxjdg.cgi)"

Get a sense for the distribution of the alert over different IP's by
pivoting on dstip (or look at the field summary at the top and notice
that there is just one unique entry for srcip)

::

       sig_msg:"ET POLICY Proxy Judge Discovery/Evasion (prxjdg.cgi)" groupby:dstip

Notice that there's just one entry for srcip and drill down on it

::

       10.0.1.1 class:snort groupby:sig_msg

Find some other alerts but nothing concrete, mine for data in URL's (via
Bro)

::

       10.0.1.1 class:bro_http groupby:site

see the Polish site and drill-down

::

       site:www.aksarat.pl

Click ``Info`` and choose the ``getPcap`` plugin to see the content of
the request

As a follow-up, look at the URI structure and see if other sites are
being used for this checkin

::

    uri:check.rsp groupby:site

Get a feel for how often the check-in occurs

::

       uri:check.rsp groupby:hour

Change granularity to per-minute

::

       uri:check.rsp groupby:minute limit:1000

Be alerted in the future by clicking ``Results...`` and choosing
``Create alert`` so anytime ``uri:check.rsp`` shows up you get an email.

1/12/13 - [security-onion]
==========================

Once you start looking at connections in ELSA with ``geoip``, you can
also use the ``whois`` plugin in the same way to see a description of
the destination network. So, from Brad's dashboard, you could run this
query in the ELSA query box:

::

       icmp or udp or tcp class=BRO_CONN groupby:BRO_CONN.dstip | whois

Then, you can do some post-search filters to remove any well-known hosts
like this:

::

       icmp or udp or tcp class=BRO_CONN groupby:BRO_CONN.dstip | whois | filter(descr,google)

Or maybe you want to see TCP traffic not to port 80/443:

::

       tcp class=BRO_CONN groupby:BRO_CONN.dstip -dstport:80 -dstport:443 | whois

Or, find only things destined for a high port with a certain byte count:

::

       +tcp class=BRO_CONN groupby:BRO_CONN.dstip +dstport>=1000 +bytes_in>1000000 | whois

1/22/13 - [security-onion] Is it possible to launch ELSA from command line?
===========================================================================

You can use the command-line version of ELSA by navigating to
``/opt/elsa/contrib/securityonion/contrib`` and using the ``cli.sh``
script:

::

    sh cli.sh "example.com" 

The output is in JSON, so you might want to install jq and pipe the
results into it:

::

    sh cli.sh "example.com" | jq '.'

4/16/2013 - `ELSA <ELSA>`__ What is the best way to query for a list of all internal RFC1918 hosts sending / receiving traffic outside the US?
==============================================================================================================================================

Great question!

If you're using a firewall to create the flow records:

::

    host:<my firewall> class:firewall_connection_end srcip>=10.0.0.0 srcip<=10.255.255.255 srcip>=192.168.0.0 srcip<=192.168.255.255 srcip>=172.16.0.0 srcip<=172.16.255.255 groupby:dstip | geoip | filter(cc,us)

You will probably want to run a prior search for just

::

     srcip>=10.0.0.0 srcip<=10.255.255.255 srcip>=192.168.0.0 srcip<=192.168.255.255 srcip>=172.16.0.0 srcip<=172.16.255.255

Then save that as a saved search and give it the name rfc1918. Then, you
can reduce the above query to this:

::

    host:<my firewall> class:firewall_connection_end $rfc1918 groupby:dstip | geoip | filter(cc,us)

If you leave off the ``host:<my firewall>`` term, then it will still
work but only search temp indexes.

For data extrusion, one of my favorites is to do something similar, but
with HTTP POST's:

::

    +method:post $rfc1918 groupby:dstip | geoip | filter(cc,us)

Or Java user agents:

::

    +user_agent:java $rfc1918 groupby:dstip | geoip | filter(cc,us)
