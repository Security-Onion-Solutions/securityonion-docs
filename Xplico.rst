Description
===========

From http://www.xplico.org/about:

    | The goal of Xplico is extract from an internet traffic capture the
      applications data contained.
    | For example, from a pcap file Xplico extracts each email (POP,
      IMAP, and SMTP protocols), all HTTP contents, each VoIP call
      (SIP), FTP, TFTP, and so on. Xplico isn’t a network protocol
      analyzer. Xplico is an open source Network Forensic Analysis Tool
      (NFAT).

EOL
===

Our Xplico package will reach EOL (End Of Life) on June 5, 2018. After
that date, we will no longer provide updates or support of any kind for
Xplico. To remove Xplico from your system, please see the steps at the
bottom of this page.

Enabling
========

Xplico is disabled by default by modern versions of Setup. This is
controlled by the ``XPLICO_ENABLED`` setting in
``/etc/nsm/securityonion.conf``.

Logging In
==========

From http://wiki.xplico.org/doku.php?id=interface:

    | The default username and password are:
    | username: xplico
    | password: xplico

    | The default admin username and password are:
    | username: admin
    | password: xplico

More Information
================

| For more information, please see:
| http://www.xplico.org/

Removing
========

If you don't use Xplico, you can remove it as follows.

Ensure that Xplico is disabled in ``/etc/nsm/securityonion.conf``:

::

    sudo sed -i 's|XPLICO_ENABLED=yes|XPLICO_ENABLED=no|g' /etc/nsm/securityonion.conf

Install all updates to ensure you're running the latest version of the
``securityonion-iso`` metapackage:

::

    sudo soup

Remove Xplico and its dependencies:

::

    sudo apt purge lame libgeoip-dev libjson-c-dev libmp3lame0 librecode0 php5-sqlite python3-httplib2 python3-psycopg2 recode securityonion-ndpi sqlite3 xplico

Remove Xplico shortcuts:

::

    sudo rm /home/*/Desktop/securityonion-xplico*
