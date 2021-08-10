.. _url-base:

Changing Web Access URL
=====================

If you need to change the URL for web access to Security Onion (for example, from IP to FQDN), do the following:

* Change the value for ``url_base`` in ``/opt/so/saltstack/local/pillar/global.sls`` (on the manager, if a distributed deployment).

* Run ``sudo salt-call state.highstate`` on all nodes (can first run on the manager, then ``sudo salt \* state.highstate`` from the manager for the remaining nodes).
