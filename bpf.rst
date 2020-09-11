.. _bpf:

BPF
===

BPF stands for Berkeley Packet Filter. From https://en.wikipedia.org/wiki/Berkeley_Packet_Filter:

   BPF supports filtering packets, allowing a userspace process to supply a filter program that specifies which packets it wants to receive. For example, a tcpdump process may want to receive only packets that initiate a TCP connection. BPF returns only packets that pass the filter that the process supplies. This avoids copying unwanted packets from the operating system kernel to the process, greatly improving performance.

Configuration
-------------

Global BPF
~~~~~~~~~~

You can specify your BPF in the global pillar on your manager node (``/opt/so/saltstack/local/pillar/global.sls``), and by default, it will apply to all interfaces in your entire deployment. If there is no BPF configuration already in the file, you can append it to the bottom of the file.

If you have separate sensors reporting to that manager node, they will pull down the relevant BPF as part of the Salt update that runs every 15 minutes and then restart Suricata/Steno/Zeek so that the BPF change will take effect.

Node-Specific BPF
~~~~~~~~~~~~~~~~~

If you don’t want your sensors to inherit BPF from the manager node, you can edit the minion sls file (``/opt/so/saltstack/local/pillar/minions/$Hostname.sls``), which will override any global BPF settings set from the global pillar.

Simple Example
~~~~~~~~~~~~~~

Suppose you want :ref:`stenographer` to not record full packet capture for port 443:

::

    steno:
     bpf:
      - not port 443

Quoting
~~~~~~~

YAML rules apply and so if you want to use a reserved YAML character such as ``[] {} > | * & ! % # ` @ ,``, then you may need to enclose the entire line in double quotes. For example:

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

If you have traffic that has VLAN tags, you can craft a BPF as follows:

::

    <your filter> or (vlan and <your filter>)

Notice that you must include your filter on both sides of the vlan tag.

For example:

::

    (not (host 192.168.1.2 or host 192.168.1.3 or host 192.168.1.4)) or (vlan and (not (host 192.168.1.2 or host 192.168.1.3 or host 192.168.1.4)))

.. warning::

   Please note that :ref:`zeek` and :ref:`stenographer` currently do not see VLAN tags due to the way that :ref:`af-packet` works:
   
   https://github.com/J-Gras/zeek-af_packet-plugin/issues/9
   
   https://github.com/google/stenographer/issues/211
   
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
