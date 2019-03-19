Proxy Configuration
===================

If you need to force your Internet traffic through a proxy server, you can put your proxy server settings in ``/etc/environment`` like this:

::

    export http_proxy=http://server:port
    export https_proxy=https://server:port
    export ftp_proxy=https://server:port
    export PERL_LWP_ENV_PROXY=https://server:port
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

***For older versions of Security Onion on the Elastic Stack, if the above did not work, you may want to try the following:***

Modify ``/etc/default/docker`` and add the appropriate proxy information, like so:

::

    export http_proxy="http://server:port/"
    export https_proxy="https://server:port/"

Then restart Docker with:

::

    sudo so-elastic-stop 
    sudo service docker restart
    sudo so-elastic-start

sudo
----

If you're going to run something using sudo, remember to use the ``-i`` option to force it to process the environment variables. For example:

::

    sudo -i rule-update

Alternatively, see the ``env_keep`` option under the ``sudo caveat`` section of https://help.ubuntu.com/community/EnvironmentVariables.

PulledPork
----------

As of `PulledPork 0.7.2 <https://blog.securityonion.net/2017/01/pulledpork-rule-update-and-several.html>`__,
you may need to pass the ``-W`` option to Pulledpork:

::

    -W Where you want to work around the issue where some implementations of LWP do not work with pulledpork's proxy configuration.

If you find that you need this option, you can add the following to ``/etc/nsm/securityonion.conf``:

::

    PULLEDPORK_OPTIONS="-W"

For older versions of PulledPork and certain proxies (Bluecoat in particular), you may need to change from ``https`` to ``http`` in ``/etc/nsm/pulledpork/pulledpork.conf``. For more information, please see:
 
`PulledPork Issue 154 <https://code.google.com/archive/p/pulledpork/issues/154>`__

https://groups.google.com/d/topic/security-onion/NQ-dLLPxR6A/discussion

https://groups.google.com/d/topic/security-onion-testing/piRYj-7Ar8M/discussion
