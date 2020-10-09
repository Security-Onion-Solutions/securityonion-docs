.. _services:

Services
========

You can control individual services with the ``so-<noun>-<verb>`` scripts. You can see a list of all of these scripts with the following command:

::

   ls /usr/sbin/so-*-*

The following examples are for Zeek, but you could substitute whatever service you're trying to control (logstash, pcap, etc.).

Start Zeek:

::

    sudo so-zeek-start

Stop Zeek:

::

    sudo so-zeek-stop

Restart Zeek:

::

    sudo so-zeek-restart
    

