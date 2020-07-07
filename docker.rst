.. _docker:

Docker
======

From https://www.docker.com/what-docker:

    Docker is the world’s leading software container platform.
    Developers use Docker to eliminate “works on my machine” problems
    when collaborating on code with co-workers. Operators use Docker to
    run and manage apps side-by-side in isolated containers to get
    better compute density. Enterprises use Docker to build agile
    software delivery pipelines to ship new features faster, more
    securely and with confidence for both Linux, Windows Server, and
    Linux-on-mainframe apps.

Images
------

To maintain a high level of stability, reliability, and support, our Elastic Docker images are based on the Docker images provided by Elastic.co. Their Docker images are built on CentOS 7:
https://www.elastic.co/blog/docker-base-centos7

Registry
--------

From https://docs.docker.com/registry/recipes/mirror/:

    If you have multiple instances of Docker running in your environment
    (e.g., multiple physical or virtual machines, all running the Docker
    daemon), each time one of them requires an image that it doesn’t
    have it will go out to the internet and fetch it from the public
    Docker registry. By running a local registry mirror, you can keep
    most of the redundant image fetch traffic on your local network.

We can leverage the Docker registry (as a `pull-through cache <https://docs.docker.com/registry/recipes/mirror/>`__) with our Security Onion Docker images. As mentioned above, this will allow us to cut down on external requests and bandwidth, cache the images on a local server, and only pull new images when they are available.

We can easily configure our Security Onion management server and sensor by running the following script on each machine (watch out for line-wrapping) :

::

   wget https://raw.githubusercontent.com/weslambert/securityonion-docker-registry/master/so-docker-registry
   sudo bash so-docker-registry

The above script:

-  Sets up a Docker container named ``docker-registry`` on the management server - this container exposes port 5000 for 127.0.0.1 (only locally).
-  Configures the management server to use the ``docker-registry`` container as its proxy to pull images (``registry-mirror`` in ``/etc/default/docker``).
-  Configures a sensor to use to ``docker-registry`` on the management server as a proxy to pull images -- this is done through the addition of a local port forward (5000) through the existing autossh tunnel (``/root/.ssh/securityonion_ssh.conf``), and setting the ``registry-mirror`` value for the docker client on the sensor (``/etc/default/docker``)
-  Restarts Security Onion Docker containers so the latest images are cached on the management server and pulled to the sensor.

After the script has completed (after running on both machines), the newest images from the ``securityonionsolutions`` repo should be locally cached on the management server, and already pulled to the sensor.

We can check this by running the following from the management server (or sensor):

::

   curl localhost:5000/v2/_catalog

From here on, whenever ``soup`` checks for new images, it will pull them from the management server instead of Docker Hub.

Sneakernet Updates
------------------

If we need to perform offline updates of Docker images, we can do so by cloning the ``security-onion-docker-airgap`` script(s) at https://github.com/weslambert/securityonion-docker-airgap:

::

   git clone https://github.com/weslambert/securityonion-docker-airgap
   cd securityonion-docker-airgap

The script(s) should be run first on a machine with internet access -- Docker images will be downloaded and saved to a single ``images.tar`` file.

::

   sudo ./so-elastic-airgap

Choose the ``Save`` option.

From there, the ``securityonion-docker-airgap`` directory (including the ``images.tar`` file) should be copied to the destination machine.

Once there, change into the ``securityonion-docker-airgap`` directory:

::

   cd securityonion-docker-airgap

Run the ``so-elastic-airgap`` script, and choose the ``Load`` option.

The Docker images should now be loaded. We can verify this by running:

::

   sudo docker images

Networking
----------

Bridge
------

By default, Docker configures it's bridge with an IP of ``172.17.0.1``.

https://docs.docker.com/engine/userguide/networking/#default-networks

For many folks this is fine, but what if we actually use the the ``172.17.0.0/16`` range within our internal network(s)?  This results in a **conflict** when trying to assign IP addresses to interfaces and trying to route outside of the host.

A simple solution to this is to do the following:

| Create the following file - ``/etc/docker/daemon.json``.
| Inside of the file, place the following:

::

    {
      "bip": "your_docker_bridge_ip/netmask"
    }   

Restart Docker:

::

   sudo service docker restart

Running ``netstat -rn`` should show that the range for the ``docker0`` bridge has changed.

| For more information/options, see:
| https://docs.docker.com/engine/userguide/networking/default_network/custom-docker0/

Containers
----------

Our Docker containers all belong to a common Docker bridge network, called ``so-elastic-net``. Each container is also aliased, so that communication can occur between the different docker containers using said alias. For example, communication to the ``so-elasticsearch`` container would occur through an alias of ``elasticsearch``.

You may come across interfaces in ``ifconfig`` with the format ``veth*``. These are the external interfaces for each of the Docker containers. These interfaces correspond to internal Docker container interfaces (within the Docker container itself).

To identify which external interface belongs to which container, we can do something like the following:

From the host, type:

::

   sudo docker exec so-elasticsearch cat /sys/class/net/eth0/iflink

This should provide you with a value with which you can grep the host ``net`` class ``ifindex(es)``:

| **Example:**
| ``grep 25 /sys/class/net/veth*/ifindex | cut -d'/' -f5``

You should then receive some output similar to the following:

``vethc5ff027``

where ``vethc5ff027`` is the external interface of ``eth0`` within the ``so-elasticsearch`` container.

Download
--------

| Our Docker images are stored on Docker Hub:
| https://hub.docker.com/u/securityonionsolutions/

If you download our Security Onion ISO image, the Docker engine and these Docker images are baked right into the ISO image.

If you instead use another ISO image, our installer will download Docker images as necessary.

Security
--------

| To prevent tampering, our Docker images are signed using Docker Notary:
| https://docs.docker.com/notary/getting_started/

Any time we push an image to Docker Hub, we explicitly set ``--disable-content-trust=false`` to sign the image using Docker Notary.

Any time we download an image from Docker Hub, we also explicitly set ``--disable-content-trust=false`` to verify that signature using Docker Notary.

VMware Tools
------------

If you have VMware Tools installed and you suspend and then resume, the Docker interfaces will no longer have IP addresses and the Elastic stack will no longer be able to communicate. One workaround is to remove ``/etc/vmware-tools/scripts/vmware/network`` to prevent VMware suspend/resume from modifying your network configuration.

Dependencies
------------

TheHive / Cortex
~~~~~~~~~~~~~~~~
so-thehive - REQ - TheHive Web App
so-thehive-cortex - OPT - Cortex Web App
so-thehive-es - REQ - TheHive & Cortex state data

Fleet
~~~~~
so-fleet - REQ - Fleet Web App
so-mysql - REQ - Fleet state data
so-redis - REQ - Required for live querying

Playbook
~~~~~~~~
so-playbook - REQ - Playbook Web App
so-navigator - OPT - Navigator Web App
so-soctopus - REQ - Automation

SOCtopus
~~~~~~~~
so-soctopus - REQ - SOCtopus App
so-elasticsearch - OPT - Automation

Suricata
~~~~~~~~
so-suricata - REQ - Suricata app

Kibana
~~~~~~
so-kibana - REQ - Kibana Web App
so-elasticsearch - REQ -

Zeek
~~~~
so-bro - REQ - Zeek app
