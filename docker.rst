.. _docker:

Docker
======

From https://www.docker.com/what-docker:

    Docker is the world’s leading software container platform. Developers use Docker to eliminate “works on my machine” problems when collaborating on code with co-workers. Operators use Docker to run and manage apps side-by-side in isolated containers to get better compute density. Enterprises use Docker to build agile software delivery pipelines to ship new features faster, more securely and with confidence for both Linux, Windows Server, and Linux-on-mainframe apps.

Download
--------

| Our Docker images are stored on Docker Hub:
| https://hub.docker.com/u/securityonion/

If you download our Security Onion ISO image, the Docker engine and these Docker images are baked right into the ISO image.

If you instead use another ISO image, our installer will download Docker images as necessary.

Security
--------

| To prevent tampering, our Docker images are signed using Docker Notary:
| https://docs.docker.com/notary/getting_started/

Any time we push an image to Docker Hub, we explicitly set ``--disable-content-trust=false`` to sign the image using Docker Notary.

Any time we download an image from Docker Hub, we also explicitly set ``--disable-content-trust=false`` to verify that signature using Docker Notary.

Elastic
-------

To maintain a high level of stability, reliability, and support, our Elastic Docker images are based on the Docker images provided by Elastic.co. Their Docker images are built on CentOS 7:
https://www.elastic.co/blog/docker-base-centos7

Registry
--------

The manager node runs a Docker registry. From https://docs.docker.com/registry/recipes/mirror/:

    If you have multiple instances of Docker running in your environment (e.g., multiple physical or virtual machines, all running the Docker daemon), each time one of them requires an image that it doesn’t have it will go out to the internet and fetch it from the public Docker registry. By running a local registry mirror, you can keep most of the redundant image fetch traffic on your local network.

Networking and Bridging
-----------------------

By default, Docker configures its bridge with an IP of ``172.17.0.1``.

https://docs.docker.com/engine/userguide/networking/#default-networks

For many folks this is fine, but what if we actually use the the ``172.17.0.0/16`` range within our internal network(s)?  This results in a **conflict** when trying to assign IP addresses to interfaces and trying to route outside of the host. 

It is currently possible to change this at install time. Once you change this default docker network you **MUST** configure all nodes in the grid to use this range:

| During setup choose change docker network range.  
| Enter your desired address range. You do not need the /24 at the end.  

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

VMware Tools
------------

If you have VMware Tools installed and you suspend and then resume, the Docker interfaces will no longer have IP addresses and the Elastic stack will no longer be able to communicate. One workaround is to remove ``/etc/vmware-tools/scripts/vmware/network`` to prevent VMware suspend/resume from modifying your network configuration.

Dependencies
------------

TheHive / Cortex
~~~~~~~~~~~~~~~~
| ``so-thehive`` - REQ - TheHive Web App
| ``so-thehive-cortex`` - OPT - Cortex Web App
| ``so-thehive-es`` - REQ - TheHive & Cortex state data

Fleet
~~~~~
| ``so-fleet`` - REQ - Fleet Web App
| ``so-mysql`` - REQ - Fleet state data
| ``so-redis`` - REQ - Required for live querying

Playbook
~~~~~~~~
| ``so-playbook`` - REQ - Playbook Web App
| ``so-navigator`` - OPT - Navigator Web App
| ``so-soctopus`` - REQ - Automation

SOCtopus
~~~~~~~~
| ``so-soctopus`` - REQ - SOCtopus App
| ``so-elasticsearch`` - OPT - Automation

Suricata
~~~~~~~~
| ``so-suricata`` - REQ - Suricata app

Kibana
~~~~~~
| ``so-kibana`` - REQ - Kibana Web App
| ``so-elasticsearch`` - REQ -

Zeek
~~~~
| ``so-bro`` - REQ - Zeek app
