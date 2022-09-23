.. _bpf:

BPF
===

BPF stands for Berkeley Packet Filter. From https://en.wikipedia.org/wiki/Berkeley_Packet_Filter:

   BPF supports filtering packets, allowing a userspace process to supply a filter program that specifies which packets it wants to receive. For example, a tcpdump process may want to receive only packets that initiate a TCP connection. BPF returns only packets that pass the filter that the process supplies. This avoids copying unwanted packets from the operating system kernel to the process, greatly improving performance.

Configuration
-------------

You can modify your BPF configuration by going to :ref:`administration` --> Configuration --> bpf. You can apply BPF configuration to :ref:`stenographer`, :ref:`suricata`, or :ref:`zeek`.

Quoting
~~~~~~~

YAML rules apply and so if you want to use a reserved YAML character such as ``[] {} > | * & ! % # ` @ ,``, then you may need to enclose the entire line in double quotes. For example:

::

        "!(port 443)"
      
Multiple Conditions
~~~~~~~~~~~~~~~~~~~

If your BPF contains multiple conditions you can put them on multiple lines and join them with a logical AND (``&&``) or logical OR (``||``) but make sure the final condition has nothing at the end. 

Here's an example of joining conditions with a logical AND:

::

        not host 192.168.1.2 &&
        not host 192.168.1.3 &&
        not host 192.168.1.4
      
Here's an example of joining conditions with a logical OR:

::

        host 192.168.1.2 ||
        host 192.168.1.3 ||
        host 192.168.1.4

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

   | Please note that :ref:`zeek` and :ref:`stenographer` should correctly analyze traffic on a VLAN but won't log the actual VLAN tags due to the way that :ref:`af-packet` works:
   | https://github.com/J-Gras/zeek-af_packet-plugin/issues/9
   | https://github.com/google/stenographer/issues/211
   
Troubleshooting BPF using tcpdump
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| If you need to troubleshoot BPF, you can use ``tcpdump`` as shown in the following articles:
| https://taosecurity.blogspot.com/2004/09/understanding-tcpdumps-d-option-have.html
| https://taosecurity.blogspot.com/2004/12/understanding-tcpdumps-d-option-part-2.html
| https://taosecurity.blogspot.com/2008/12/bpf-for-ip-or-vlan-traffic.html

More Information
----------------

.. seealso::

   Check out our BPF video at https://youtu.be/uamNOjtUi4Y!

   | For more information about BPF, please see:
   | https://en.wikipedia.org/wiki/Berkeley_Packet_Filter
   | https://biot.com/capstats/bpf.html
