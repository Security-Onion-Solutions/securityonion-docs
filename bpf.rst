.. _bpf:

BPF
===

| BPF stands for Berkeley Packet Filter:
| https://en.wikipedia.org/wiki/Berkeley_Packet_Filter
| http://biot.com/capstats/bpf.html

Configuration
-------------

Global BPF
~~~~~~~~~~

You can specify your BPF in the static pillar on your manager node (``/opt/so/saltstack/local/pillar/static.sls``), and by default, it will apply to all interfaces in your entire deployment.

If you have separate sensors reporting to that manager node, they will pull down the relevant BPF as part of the Salt update that runs every 15min and then restart Suricata/Steno/Zeek so that the BPF change will take effect.

Node-Specific BPF
~~~~~~~~~~~~~~~~~

If you don’t want your sensors to inherit BPF from the manager node, you can edit the minion sls file, which will override any global BPF settings set from the static pillar. (``/opt/so/saltstack/local/pillar/minions/$Hostname.sls``)

Pillar BPF Syntax
~~~~~~~~~~~~~~~~~

::

   steno:
     bpf:
      - not port 80 &&
      - not port 443 &&
      - not port 134

   zeek:
     bpf:
      - not port 443

   nids:
     bpf:
      - not port 443


BPF Examples
~~~~~~~~~~~~

Exclude traffic to/from a host:

::

   !(host xxx.xxx.xxx.xxx)
   
   
Exclude traffic from a source host to a destination port:

::

    !(src host xxx.xxx.xxx.xxx && dst port 161)
    
Combine multiple BPFs together using ``&&``, but note that the last entry has no final ``&&``:
::

    #Nothing from src host to dst port
    !(src host xxx.xxx.xxx.xxx && dst port 161) &&

    #Nothing from src host to dst host and dst port
    !(src host xxx.xxx.xxx.xxx && dst host xxx.xxx.xxx.xxx && dst port 80) &&

    #Nothing to or from:
    !(host xxx.xxx.xxx.xxx) &&

    #Last entry has no final &&
    !(host xxx.xxx.xxx.xxx)

VLAN
~~~~
From Seth Hall regarding VLAN tags:

::

    (not (host 192.168.53.254 or host 192.168.53.60 or host 192.168.53.69 or host 192.168.53.234)) or (vlan and (not (host 192.168.53.254 or host 192.168.53.60 or host 192.168.53.69 or host 192.168.53.234)))

This amazingly works if you are only using it to restrict the traffic passing through the filter. The basic template is…

::

    <your filter> and (vlan and <your filter>)

Once the ``vlan`` tag is included in the filter, all subsequent
expressions to the right are shifted by four bytes so you need to
duplicate the filter on both sides of the vlan keyword. There are edge
cases where this will no longer work and probably edge cases where a few
undesired packets will make it though, but it should work in the example
case that you've given.

Also, I'm assuming that any tools you are running will support vlan tags and no tags simultaneously.

Troubleshooting BPF using tcpdump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you need to troubleshoot BPF, you can use ``tcpdump`` as shown in the following articles.

http://taosecurity.blogspot.com/2004/09/understanding-tcpdumps-d-option-have.html

http://taosecurity.blogspot.com/2004/12/understanding-tcpdumps-d-option-part-2.html

http://taosecurity.blogspot.com/2008/12/bpf-for-ip-or-vlan-traffic.html
