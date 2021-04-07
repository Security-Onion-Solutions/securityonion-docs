.. _proxy:

Proxy Configuration
===================

Starting in Security Onion 2.3.40, Setup will ask if you want to connect through a proxy server and, if so, it will automatically configure the system for you. Otherwise, if you need to configure manually, please continue reading.

If you need to force your Internet traffic through a proxy server, you can put your proxy server settings in ``/etc/environment`` like this:

::

    export http_proxy=http://server:port
    export https_proxy=https://server:port
    export ftp_proxy=https://server:port
    export no_proxy="localhost,127.0.0.1"

You may also need to include the actual IP address of the Security Onion box itself in the ``no_proxy`` variable above.

Docker
------

To configure Docker proxy settings, please see https://docs.docker.com/network/proxy/.

sudo
----

If you're going to run something using sudo, remember to use the ``-i`` option to force it to process the environment variables. For example:

::

    sudo -i so-rule-update

.. warning::
    Using ``sudo su -`` will ignore ``/etc/environment``, instead use ``sudo su`` if you need to operate as root.
