.. _proxy:

Proxy
=====

Setup will ask if you want to connect through a proxy server and, if so, it will automatically configure the system for you. Otherwise, if you need to configure manually, please continue reading.

There is no way to set a global proxy on Linux, but several tools will route their traffic through a proxy if the following lines are added to ``/etc/environment``:

::

    http_proxy=<proxy_url>
    https_proxy=<proxy_url>
    ftp_proxy=<proxy_url>
    no_proxy="localhost, 127.0.0.1, <management_ip>, <hostname>"
    
Where:
    ``<proxy_url>`` is the url of the proxy server. (For example, ``http://10.0.0.2:3128`` or ``https://user:password@your.proxy.url``)
    
    ``<management_ip>`` is the IP address of the Security Onion box.
    
    ``<hostname>`` is the hostname of the Security Onion box.
   
.. note::
    You may also need to include the IP address and hostname of the manager in the ``no_proxy`` variable above if configuring the proxy on a forward node.
   
In addition to the above, Security Onion also makes use of pillar values in the file ``/opt/so/saltstack/local/pillar/minions/<HOSTNAME>_<ROLE>.sls`` on managers. Edit that file as below, following the same substitutions from above:

::

    ...
    manager:
        ...
        proxy: '<proxy_url>'
        no_proxy: 'localhost, 127.0.0.1, <management_ip>, <hostname>'
        ...
   

.. note:: 
    The above snippet is truncated, ellipses ( ``...`` ) should be treated as one or more lines in the file.


To configure Docker proxy settings, please see https://docs.docker.com/network/proxy/.


To configure git to use a proxy for all users, add the following to ``/etc/gitconfig``:

::

    [http]
      proxy = <proxy_url>

sudo
----

If you're going to run something using sudo, remember to use the ``-i`` option to force it to process the environment variables. For example:

::

    sudo -i so-rule-update

.. warning::
    Using ``sudo su -`` will ignore ``/etc/environment``, instead use ``sudo su`` if you need to operate as root.
