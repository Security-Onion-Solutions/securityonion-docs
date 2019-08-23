Setup
=====

After installing Security Onion, double-click the ``Setup`` icon on the desktop (or run ``sudo sosetup`` from a terminal) to configure your system.  In most cases, you'll run Setup to do network configuration, reboot, and then run Setup again for service configuration.

sosetup-minimal
---------------

``sosetup-minimal`` configures Security Onion to run using minimal resources.  It will run Setup and then do the following:

-  stop and disable elastalert
-  stop and disable freqserver
-  stop and disable domainstats
-  set Elasticsearch to a 400MB heap size
-  set Logstash to ``LOGSTASH_MINIMAL`` mode and set a 200MB heap size

Automating Setup
----------------

You can automate the Setup process using ``sosetup.conf``.

Starting from scratch
---------------------

There are a few example files in ``/usr/share/securityonion/``.  Copy one of these example files to your home directory:

::

    cp /usr/share/securityonion/sosetup.conf ~

Edit your new ``sosetup.conf`` using ``nano`` or your favorite text editor:

::

    nano ~/sosetup.conf

Then run Setup with the ``-f`` switch and the path to this file:

::

    sudo sosetup -f ~/sosetup.conf

sosetup -w
----------

``sosetup`` also supports a ``-w`` switch that allows you to answer the standard Setup questions and have it write out your custom ``sosetup.conf``.  For example:

::

    # Configure sosetup to write out a new configuration file called sosetup.conf
    sosetup -w ~/sosetup.conf

    # Answer all questions in Setup

    # Run sosetup with the new configuration file
    sudo sosetup -f ~/sosetup.conf
