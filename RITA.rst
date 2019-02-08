RITA
====

From: https://github.com/activecm/rita

    RITA is an open source framework for network traffic analysis.

    The framework ingests Bro Logs, and currently supports the following
    analysis features:

    | Beaconing: Search for signs of beaconing behavior in and out of
      your network
    | DNS Tunneling Search for signs of DNS based covert channels
    | Blacklisted: Query blacklists to search for suspicious domains and
      hosts
    | URL Length Analysis: Search for lengthy URLs indicative of malware
    | Scanning: Search for signs of port scans in your network

We can add RITA to Security Onion to enhance its current capabilities
and leverage the great work from the folks at `Active
Countermeasures <https://activecountermeasures.com/>`__. They've done a
fantastic job of allowing RITA to be easy to integrate with Security
Onion.

Warning
-------

Please keep in mind we do not officially support RITA, so installation
is at your own risk.

Additionally, RITA currently only supports use of Bro logs in TSV
format. If you ware running the latest version of Security Onion, you
will need to switch from JSON to TSV format by following the steps here:

`<Bro#tsv>`__

Installation
------------

To install RITA on Security Onion:

| Download the install script:
| ``wget https://raw.githubusercontent.com/activecm/rita/master/install.sh``

| Make the installer executable:
| ``chmod +x install.sh``

| Run the installer:
| ``sudo ./install.sh``

| Start MongoDB:
| ``sudo service mongod start``

Usage
-----

| You can then import logs with:
| ``rita import /nsm/bro/logs dataset1``

| Then have RITA analyze the imported data:
| ``rita analyze``

| To see the most visited URLs:
| ``rita show-most-visited-urls dataset1``

| To see long connections, type:
| ``rita show-long-connections dataset1``

| To see beacons, type:
| ``rita show-beacons dataset1``

| Finally, you can issue an HTML report (viewable in browser) by typing:
| ``rita html-report``

| See other available commands with:
| ``rita --help``

Configuration
-------------

If you don't want to specify your the path for your Bro logs, you'll
want to change the value for ``ImportDirectory`` in
``/etc/rita/config.yaml`` to ``/nsm/bro/logs``.

| For additional information, see:
| https://github.com/activecm/rita
