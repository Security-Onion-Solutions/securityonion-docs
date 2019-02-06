GA now available
================

| Our Elastic Stack integration has reached General Availability! We
  highly recommend performing a fresh installation rather than trying to
  upgrade pre-release installations!
| https://blog.securityonion.net/2018/04/security-onion-elastic-stack-general.html

Warning
=======

Our Elastic integration is still considered experimental and so the
usual warnings and disclaimers apply:

Experimental Setup is BLEEDING EDGE and TOTALLY UNSUPPORTED!

-  If this breaks your system, you get to keep both pieces!
-  This is a work in progress and is in constant flux.
-  Do NOT run this on a system that you care about!
-  Do NOT run this on a system that has data that you care about!
-  This should only be run on a TEST box with TEST data!
-  Experimental Setup may result in nausea, vomiting, or a burning
   sensation.

NOT Officially Supported
========================

Performing an in-place upgrade from previous Alpha/Beta/RC releases to
the current Release Candidate is NOT officially supported. If you're
currently running RC3, here are the steps you can try to update to RC4.
If you encounter any issues, please perform a fresh installation of the
current Release Candidate.

Distributed Deployments
=======================

If you're updating a distributed deployment, please perform the
following steps on the master server before upgrading any nodes. Any
nodes running Logstash/Elasticsearch (Ex. Storage/Heavy) will need to
have these steps performed as well.

Prepare to Update
=================

First, delete Logstash templates before updating:

::

    curl -XDELETE localhost:9200/_template/logstash*

Back up Logstash config:

::

    sudo mv /etc/logstash/conf.d /etc/logstash/conf.d.prerc4

Update
======

Next, update to new packages and images:

::

    sudo soup

Clean Up
========

Remove all so-crossclustercheck references:

::

    sudo rm -f /etc/cron.d/crossclustercheck
    sudo rm -f /etc/logrotate.d/crossclustercheck
    sudo rm -f /etc/nsm/crossclustertab

If you have mapping conflicts in Kibana, then delete old indices (this
will delete all logstash data in Elasticsearch):

::

    curl -XDELETE localhost:9200/logstash-*

Elasticsearch heap size
=======================

Elasticsearch heap size is no longer controlled in
``/etc/nsm/securityonion.conf``. It is now controlled in the standard
``/etc/elasticsearch/jvm.options`` file. The default of 25% of RAM up to
25GB should be a sane default for most deployments. If you need to
modify this default, you can modify ``-Xms`` and ``-Xmx`` in
``/etc/elasticsearch/jvm.options`` but make sure they are set to the
same value. Then restart Elasticsearch:

::

    sudo so-elasticsearch-restart

To avoid confusion, you can remove the old ``ELASTICSEARCH_HEAP`` option
from your ``/etc/nsm/securityonion.conf`` as follows:

::

    sudo sed -i '/ELASTICSEARCH_HEAP=/d' /etc/nsm/securityonion.conf

Logstash heap size
==================

Logstash heap size is no longer controlled in
``/etc/nsm/securityonion.conf``. It is now controlled in the standard
``/etc/logstash/jvm.options`` file. The default of 25% of RAM up to 4GB
should be a sane default for most deployments. If you need to modify
this default, you can modify ``-Xms`` and ``-Xmx`` in
``/etc/logstash/jvm.options`` but make sure they are set to the same
value. Then restart Logstash:

::

    sudo so-logstash-restart

To avoid confusion, you can remove the old ``LOGSTASH_HEAP`` option from
your ``/etc/nsm/securityonion.conf`` as follows:

::

    sudo sed -i '/LOGSTASH_HEAP=/d' /etc/nsm/securityonion.conf

Logstash Failures
=================

If you updated without first running the
``sudo mv /etc/logstash/conf.d /etc/logstash/conf.d.prerc4`` command at
the top of this page, then you may get Logstash failures that look like
this:

::

    An unexpected error occurred! {:error=>#<NoMethodError: undefined method `tr'

Since ``/etc/logstash/conf.d`` wasn't renamed, Logstash now has a broken
configuration. Try resolving as follows:

::

    sudo mv /etc/logstash/conf.d /etc/logstash/conf.d.broken
    sudo so-elastic-configure

Updating \_cluster/settings
Once all nodes have been updated using the steps above, log into Kibana on the master server. If Kibana shows an error with index patterns, you may need to run the following on the master server:
===================================================================================================================================================================================================

::

    so-elastic-configure-kibana

Once logged into Kibana, click Dev Tools, paste the following, and then
click the green triangle to send the request:

::

    GET _cluster/settings

The output pane on the right will then display ``_cluster/settings``
which will list the master server and any remote nodes.

If any of your hostnames have capital letters, you may see duplicate
entries for them. For example, suppose that your hostname is
``SecurityOnion``. You would have previously had an entry in
``_cluster/settings`` for ``SecurityOnion``. Our new standard is to
lowercase these settings so you'll now have a new entry for
``securityonion``. You'll need to remove the old ``SecurityOnion``
entry. Paste the following into Dev Tools and replace "SecurityOnion"
with the actual node name you'd like to remove:

::

    PUT _cluster/settings
    {
    "persistent": {
    "search": {
    "remote": {
    "SecurityOnion": {
    "seeds": null}}}}}

Also, any remote nodes (heavy nodes or storage nodes) will need to be
updated with a new option called ``skip_unavailable`` (this replaces our
old ``so-crossclustercheck`` workaround). So for each remote node, paste
the following and replace ``remotenode1`` with the name of the node
you're updating:

::

    PUT _cluster/settings
    {
    "persistent": {
    "search.remote.remotenode1.skip_unavailable": true}}

When finished, ``GET _cluster/settings`` should show one entry for the
master server and one entry for each remote node. Remote nodes should
show ``"skip_unavailable": "true"`` and all entries should be lowercase.
