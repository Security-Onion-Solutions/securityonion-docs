Automating Setup
================

You can automate the Setup process using ``sosetup.conf``.  There are a few example files in ``/usr/share/securityonion/``.

Starting from scratch
---------------------

Copy one of the example files from ``/usr/share/securityonion/`` to your home directory:

::

    cp /usr/share/securityonion/sosetup.conf ~

Edit your new ``sosetup.conf`` using ``nano`` or your favorite text editor:

::

    nano ~/sosetup.conf

Run Setup with the -f switch and the path to this file:

::

    sudo sosetup -f ~/sosetup.conf

Using ``sosetup -w``
--------------------

``sosetup`` also supports a ``-w`` switch that allows you to answer the standard Setup questions and have it write out your custom ``sosetup.conf``.  For example:

::

    # Configure sosetup to write out a new configuration file called sosetup.conf
    sosetup -w ~/sosetup.conf

    # Answer all questions in Setup

    # Run sosetup with the new configuration file
    sudo sosetup -f ~/sosetup.conf
