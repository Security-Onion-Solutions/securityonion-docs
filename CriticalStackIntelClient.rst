Critcal Stack Intel Client
==========================

Many analysts may wish to integrate intel feeds into their existing
network security monitoring infrastructure. While still considered
experimental, analysts can install and utilize the Critical Stack Intel
Client with in Security Onion to do so, allowing them receive and act
upon intel feeds as desired. The process for installing and configuring
the client is rather straightforward, and can be completed in minutes.

Install and Configure
---------------------

| For installation steps, please see:
| http://taosecurity.blogspot.com/2015/01/try-critical-stack-intel-client.html

Profit
------

Once the client is correctly installed and configured , Bro should
create ``intel.log`` in ``/nsm/bro/logs``, and you should be able to see
logs via the Intel dashboard within Kibana.

**Please note**: Depending on the type of traffic seen by Security
Onion, it may take a while for information to be available, or for
``intel.log`` to be created, as this is only done once an indicator has
been recognized.

Also note that, by default, the Critical Stack client polls hourly to
update (locally) feeds to which you are subscribed. Requests are limited
to a certain amount per hour, so it is recommended to use a different
API key per server. Upstream, the content of the feeds themselves are
updated at an interval defined by the the feed author/origin.

| For more information, please see Richard Bejtlich's TaoSecurity blog
  or the Critical Stack Intel Marketplace:
| http://taosecurity.blogspot.com/2015/01/try-critical-stack-intel-client.html
| https://intel.criticalstack.com/
