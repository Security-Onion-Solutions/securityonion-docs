.. _proxy:

Proxy Configuration
===================

If you need to force your Internet traffic through a proxy server, you can put your proxy server settings in ``/etc/environment`` like this:

::

    export http_proxy=http://server:port
    export https_proxy=https://server:port
    export ftp_proxy=https://server:port
    export no_proxy="localhost,127.0.0.1"

Docker
------

To configure Docker proxy settings, perform the following steps:

::

   sudo -i
   mkdir /etc/systemd/system/docker.service.d
   cat <<EOT >> /etc/systemd/system/docker.service.d/proxy.conf 
   [Service]
   Environment="HTTP_PROXY=http://proxy.someplace.com:8080/" "HTTPS_PROXY=http://proxy.someplace.com:8080/" "NO_PROXY=127.0.0.1,localhost,.someplace.com"
   EOT
   systemctl daemon-reload && systemctl restart docker && exit
   sudo soup

sudo
----

If you're going to run something using sudo, remember to use the ``-i`` option to force it to process the environment variables. For example:

::

    sudo -i rule-update

Alternatively, see the ``env_keep`` option under the ``sudo caveat`` section of https://help.ubuntu.com/community/EnvironmentVariables.
