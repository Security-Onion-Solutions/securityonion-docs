.. _proxmox:

Proxmox
=======

Proxmox Virtual Environment is a virtualization platform similar to :ref:`vmware` or :ref:`virtualbox`. You can read more about Proxmox VE at https://www.proxmox.com/en/proxmox-ve. If you would like to run Security Onion in a Proxmox VM, then here are some additional things you need to be aware of.

CPU
---

Proxmox defaults to a VM CPU which may not include all of the features of your host CPU. You may need to change this to ``host`` to pass through the host CPU type.

Display
-------

If you plan to use :ref:`networkminer` or other Mono-based applications in a Proxmox VM, then you may need to set the VM Display to ``VMware compatible (vmware)``.

NIC
---

If you're going to install Security Onion in Proxmox and sniff live network traffic, you may need to do some additional configuration in Proxmox itself. You can either passthrough a physical NIC to the VM or you can use a virtual NIC.

Passthrough Physical NIC
~~~~~~~~~~~~~~~~~~~~~~~~

The first option is to sniff traffic from a physical NIC that has been passed through to the VM. For more information about Proxmox passthrough, please see:

https://www.servethehome.com/how-to-pass-through-pcie-nics-with-proxmox-ve-on-intel-and-amd/

https://pve.proxmox.com/wiki/PCI_Passthrough

https://pve.proxmox.com/wiki/PCI(e)_Passthrough

Once the physical NIC is passed through to the Security Onion VM, then Security Onion should be able to correctly configure the NIC for sniffing.

Virtual NIC
~~~~~~~~~~~

The second option is to sniff traffic from a Proxmox virtual NIC. For more details, please see the discussion at https://github.com/Security-Onion-Solutions/securityonion/discussions/8245.

Keep in mind you may need to manually disable NIC offloading features on any Proxmox NIC used for sniffing (the physical interface and any related bridge interface). One way to do this is to add a post-up command to each sniffing interface in /etc/network/interfaces on the Proxmox host. 

For example, if you have a Proxmox physical interface called ``enp2s0`` with a bridge interface called ``vmbr1``, then you might log into Proxmox and edit /etc/network/interfaces by adding the following to the ``enp2s0`` section:

::

  post-up for i in rx tx sg tso ufo gso gro lro; do ethtool -K enp2s0 $i off; done

and the following to the ``vmbr1`` section:

::

  post-up for i in rx tx sg tso ufo gso gro lro; do ethtool -K vmbr1 $i off; done

For more information about NIC offloading, please see https://blog.securityonion.net/2011/10/when-is-full-packet-capture-not-full.html.

If you are running Proxmox 9 or higher, then you may also need to set ``mtu 9000`` for the Proxmox physical sniffing interface and its corresponding bridge interface.

Once your Security Onion VM is receiving traffic as expecte, if :ref:`grid` reports Capture Loss but no Zeek Loss and you are confident that the loss is not occuring in your tap or span port, then it may be related to the Proxmox host physical interface. Certain NICs like the Intel X710 may have pre-set channels and you can check with the ``ethtool -l`` command. For more information, please see the ``ethtool`` man page at https://man7.org/linux/man-pages/man8/ethtool.8.html.

If this is the case for your host physical interface, then you can add an additional post-up command to run ``ethtool -L`` with the ``combined 1`` option. For example, if you have a physical interface called ``enp3s0f1np1``, then the corresponding section of /etc/network/interfaces would look like this:

::

  post-up ethtool -L enp3s0f1np1 combined 1; for i in rx tx sg tso ufo gso gro lro; do ethtool -K enp3s0f1np1 $i off; done

