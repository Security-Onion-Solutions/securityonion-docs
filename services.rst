.. _services:

Services
========

All Services
------------

You can control all services with the ``so-<verb>`` scripts as follows.

Check status of all services:

::

    sudo so-status

Start all services:

::

    sudo so-start

Stop all services:

::

    sudo so-stop

Restart all services:

::

    sudo so-restart
    
Individual Services
-------------------

You can control individual services with the ``so-<noun>-<verb>`` scripts. You can see a list of all of these scripts with the following command:

::

   ls /usr/sbin/so-*-*

The following examples are for Zeek, but you could substitute whatever sensor service you're trying to control (logstash, pcap, etc.).

Check status of Zeek:

::

    sudo so-zeek-status

Start Zeek:

::

    sudo so-zeek-start

Stop Zeek:

::

    sudo so-zeek-stop

Restart Zeek:

::

    sudo so-zeek-restart
    

