Description
===========

At Security Onion Conference 2016, Eric Conrad shared some IDS rules for
detecting unusual ICMP echo requests/replies and identifying C2 channels
that may utilize ICMP tunneling for covert communication.

Usage
=====

We can add the rules to ``/etc/nsm/rules/local.rules`` and the variables
to ``snort.conf`` and/or ``suricata.yaml`` so that we can gain better
insight into ICMP echoes or replies over a certain size, containing
particularly suspicious content, etc.

Presentation
============

| You can find Eric's presentation here:
| http://www.ericconrad.com/2016/09/c2-phone-home-leveraging-securityonion.html

Download
========

| You can download the rules here:
| https://drive.google.com/file/d/0ByeHgv6rpa3gUDNuMUdobFBCNkk
