Services
========

Services are controlled by the use of Security Onion scripts (``so-<noun>-<verb>``) which act as wrappers to other lower-level scripts. You can see a list of all of these scripts with the following command:

::

   ls /usr/sbin/so-*

These scripts are detailed below.

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

The three main categories of services are server, sensor, and elastic.

Server services
---------------

Check status of sguild (Sguil server):

::

    sudo so-sguild-status

Start sguild:

::

    sudo so-sguild-start

Stop sguild:

::

    sudo so-sguild-stop

Restart sguild:

::

    sudo so-sguild-restart

Sensor services
---------------

Sensor services are controlled with ``so-sensor-*``.

The following examples are for Bro, but you could substitute whatever sensor service you're trying to control (nids, pcap, etc.).

Check status of Bro:

::

    sudo so-bro-status

Start Bro:

::

    sudo so-bro-start

Stop Bro:

::

    sudo so-bro-stop

Restart Bro:

::

    sudo so-bro-restart

Elastic services
----------------

Elastic services are controlled with ``so-elastic-*``.

Check status of the Elastic stack:

::

    sudo so-elastic-status

Start the Elastic stack:

::

    sudo so-elastic-start

Stop the Elastic stack:

::

    sudo so-elastic-stop

Restart the Elastic stack:

::

    sudo so-elastic-restart
