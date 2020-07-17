.. _bpf:

BPF
===

BPF stands for Berkeley Packet Filter. From https://en.wikipedia.org/wiki/Berkeley_Packet_Filter:

   BPF supports filtering packets, allowing a userspace process to supply a filter program that specifies which packets it wants to receive. For example, a tcpdump process may want to receive only packets that initiate a TCP connection. BPF returns only packets that pass the filter that the process supplies. This avoids copying unwanted packets from the operating system kernel to the process, greatly improving performance.

Configuration
-------------

Global BPF
~~~~~~~~~~

You can specify your BPF in the static pillar on your manager node (``/opt/so/saltstack/local/pillar/static.sls``), and by default, it will apply to all interfaces in your entire deployment.

If you have separate sensors reporting to that manager node, they will pull down the relevant BPF as part of the Salt update that runs every 15min and then restart Suricata/Steno/Zeek so that the BPF change will take effect.

Node-Specific BPF
~~~~~~~~~~~~~~~~~

If you don’t want your sensors to inherit BPF from the manager node, you can edit the minion sls file, which will override any global BPF settings set from the static pillar. (``/opt/so/saltstack/local/pillar/minions/$Hostname.sls``)

Simple Example
~~~~~~~~~~~~~~

Suppose you want :ref:`stenographer` to not record full packet capture for port 443:

::

    steno:
     bpf:
      - not port 443

Quoting
~~~~~~~

YAML rules apply and so if the bpf's first character is a reserved YAML character such as ``[] {} > | * & ! % # ` @ ,``, then you will need to enclose the entire line in double quotes. For example:

::

    steno:
     bpf:
      - "!(port 443)"
      
Multiple Conditions
~~~~~~~~~~~~~~~~~~~

If your BPF contains multiple conditions you can put them on multiple lines and join them with ``&&`` but make sure the final condition has no ``&&`` at the end. For example:

::

    nids:
     bpf:
      - not host 192.168.1.2 &&
      - not host 192.168.1.3 &&
      - not host 192.168.1.4

VLAN
~~~~
From Seth Hall regarding VLAN tags:

::

    (not (host 192.168.53.254 or host 192.168.53.60 or host 192.168.53.69 or host 192.168.53.234)) or (vlan and (not (host 192.168.53.254 or host 192.168.53.60 or host 192.168.53.69 or host 192.168.53.234)))

This amazingly works if you are only using it to restrict the traffic passing through the filter. The basic template is…

::

    <your filter> and (vlan and <your filter>)

Once the ``vlan`` tag is included in the filter, all subsequent expressions to the right are shifted by four bytes so you need to duplicate the filter on both sides of the vlan keyword. There are edge cases where this will no longer work and probably edge cases where a few undesired packets will make it though, but it should work in the example case that you've given.

Also, I'm assuming that any tools you are running will support vlan tags and no tags simultaneously.

Troubleshooting BPF using tcpdump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you need to troubleshoot BPF, you can use ``tcpdump`` as shown in the following articles.

http://taosecurity.blogspot.com/2004/09/understanding-tcpdumps-d-option-have.html

http://taosecurity.blogspot.com/2004/12/understanding-tcpdumps-d-option-part-2.html

http://taosecurity.blogspot.com/2008/12/bpf-for-ip-or-vlan-traffic.html

More Information
----------------

.. seealso::

   | For more information about BPF, please see:
   | https://en.wikipedia.org/wiki/Berkeley_Packet_Filter
   | http://biot.com/capstats/bpf.html
