.. _analyst-vm:

Analyst VM
==========

Full-time analysts may want to create a dedicated Analyst VM. This allows you to investigate pcaps and other potentially malicious artifacts without fear of impacting your Security Onion deployment or your workstation.

Starting in Security Onion 2.2, the ``so-analyst`` script will install a full GNOME desktop environment including Chromium web browser, :ref:`wireshark`, :ref:`networkminer`, and other analyst tools. 

.. note::

 ``so-analyst`` currently downloads packages from the Internet, so you will need to ensure that networking is configured before running ``so-analyst``.

If you installed using our Security Onion 2.2 (or higher) ISO image:

::

 sudo ~/SecurityOnion/setup/so-analyst
 
Otherwise, if you installed standard CentOS/Ubuntu and then cloned our github repo, then you can run ``so-analyst`` from your git clone directory like this:

::

 sudo ~/securityonion/setup/so-analyst

To connect from the Analyst VM to your manager node, you will need to run :ref:`so-allow` on the manager node and choose the ``analyst`` option to allow the traffic through the host-based :ref:`firewall`.

.. toctree::
   :maxdepth: 2
   
   networkminer
   wireshark
