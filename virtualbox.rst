.. _virtualbox:

VirtualBox
==========

In this section, we'll cover installing Security Onion on VirtualBox. You can download a copy of VirtualBox for Windows, Mac OS X, or Linux at https://www.virtualbox.org. 

Creating VM
-----------

- Launch VirtualBox and click the ``New`` button.
- Provide a name for the virtual machine (``Security Onion 2.4`` for example) and then select the ISO image. It should automatically set type to ``Linux`` and version to ``Oracle Linux 9.x``. Click the checkbox for ``Skip Unattended Installation`` and then click the ``Next`` button.
- Specify RAM and Processors as needed per the :ref:`hardware` section and then click the ``Next`` button.
- Specify virtual hard disk size as needed per the :ref:`hardware` section and then click the ``Next`` button.
- Confirm options and then click the ``Finish`` button.
- Virtualbox should have automatically enabled a network adapter attached to the NAT network. Depending on what kind of installation you are doing, you may want an additional network interface for sniffing from a TAP or SPAN port. If so, click the ``Settings`` button, click ``Network``, and then go to ``Adapter 2``. Enable the adapter, configure the network it should attach to, and then you will most likely want to go to Advanced and set Promiscuous Mode to either ``Allow VMs`` or ``Allow All``. Click the ``OK`` button.
- Click the ``Start`` button to start the VM.
- Follow the installation steps for your desired installation type in the :ref:`installation` section.

Guest Additions
---------------

If you want to install VirtualBox Guest Additions, please see https://www.virtualbox.org/manual/ch04.html.
