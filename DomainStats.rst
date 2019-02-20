DomainStats
===========

| DomainStats is based on Mark Baggett's domain\_stats.py, found at
  https://github.com/MarkBaggett/domain_stats.
| Thanks to Justin Henderson for all his work with the DomainStats
  docker image!

From https://github.com/SMAPPER/docker_domain_stats:

    This docker image runs domain\_stats.py. This is a python service
    that is designed to perform mass domain analysis. It can do things
    such as find the creation\_date of a domain and identify if a domain
    is a member of the Alexa/Cisco Umbrella top 1 million sites.

    It was developed to be used in conjunction with a SIEM and is in
    production environments. Specifically, it has been used in
    conjunction with the Elastic Stack, such as queried by Logstash,
    with large success.

Configuration
-------------

Internet Access
~~~~~~~~~~~~~~~

DomainStats does whois lookups so it needs to connect outbound on port
43 to whois servers on the Internet. If this traffic is not allowed
through your firewall, then whois lookups will hang causing DomainStats
to hang. This results in the logstash pipeline backing up and Kibana
showing no data. In the current release, Setup will automatically
disable DomainStats if whois lookups fail.

Enabling DomainStats
~~~~~~~~~~~~~~~~~~~~

| DomainStats is disabled by default when running ``Production Mode``
  with ``Best Practices``.
| You can enable it by doing the following:

::

    sudo sed -i 's/DOMAIN_STATS_ENABLED="no"/DOMAIN_STATS_ENABLED="yes"/' /etc/nsm/securityonion.conf
    sudo so-elastic-start
    sudo so-logstash-restart

Updating Top-1m file
~~~~~~~~~~~~~~~~~~~~

From https://github.com/SMAPPER/docker_domain_stats#updating-top-1m-file:

    The docker image does not currently automatically update the
    top-1m.csv. The below example shows how to download a new top 1
    million site list and have a domain_stats container use it. This
    could be scheduled as a cron job on your host to keep a current
    Alexa/Cisco Umbrella top-1m.csv in use.

(Slightly modified for Security Onion)

::

    #/etc/cron.d/domainstats   
    #
    #crontab entry to grab new Top 1m CSV for DomainStats Docker image   
    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/localbin:/sbin:/bin/usr/sbin:/usr/bin
    1 07 * * *   root ( wget -q http://s3.amazonaws.com/alexa-static/top-1m.csv.zip -O /tmp/top-1m.csv.zip && unzip -o 
    /tmp/top-1m.csv.zip -d /tmp && docker cp /tmp/top-1m.csv so-domainstats:/opt/domain_stats/top-1m.csv && docker restart 
    so-domainstats && rm -f /tmp/top-1m.csv* ) > /dev/null 2>&1

| For information how to modify configuration for DomainStats, consult the following:
| https://github.com/SMAPPER/docker_domain_stats

DomainStats logs can be found in ``/var/log/domain_stats/``.

Kibana
------

| You can find DomainStats data by going to the Domain Stats dashboard in Kibana:
| |domain1-dns|

.. |domain1-dns| image:: https://user-images.githubusercontent.com/1659467/30856291-e5c2d8e0-a285-11e7-9230-36c190329be7.PNG
