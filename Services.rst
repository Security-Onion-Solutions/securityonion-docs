Services
========

Services are controlled by the use of Security Onion scripts
(``so-<noun>-<verb>``) which act as wrappers to other lower-level
scripts. These scripts are detailed below:

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

List of controlled services:

::

    ls /usr/sbin/so-sensor-*

The following examples are for Bro, but you could substitute whatever
sensor service you're trying to control.

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
