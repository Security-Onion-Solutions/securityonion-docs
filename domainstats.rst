.. _domainstats:

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

DomainStats does whois lookups so it needs to connect outbound on port 43 to whois servers on the Internet. If this traffic is not allowed through your firewall, then whois lookups will hang causing DomainStats to hang. This results in the log pipeline backing up and Kibana showing no data. In the current release, Setup will automatically disable DomainStats if whois lookups fail. Because of this, DomainStats is currently disabled by default.
