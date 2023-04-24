.. _analyst-vm:

Analyst VM
==========

Full-time analysts may want to create a dedicated Analyst VM. This allows you to investigate pcaps and other potentially malicious artifacts without impacting your Security Onion deployment or your workstation.

.. image:: images/analyst-vm.png
  :target: _images/analyst-vm.png

.. note::

  The Analyst desktop currently only supports CentOS, so you'll either need to use our Security Onion ISO image (recommended) or a manual installation of CentOS 7.
  
**Installation**

There are a few different ways to install the Analyst desktop:

- Our Security Onion ISO image includes a new boot menu option for Analyst installs that will partition your disk appropriately and immediately perform an Analyst installation.

- In our normal Setup wizard, you can choose ``OTHER`` and then choose ``ANALYST``.

- The ``so-analyst-install`` script will install a full GNOME desktop environment including Chromium web browser, :ref:`networkminer`, :ref:`wireshark`, and other analyst tools. ``so-analyst-install`` is totally independent of the standard setup process, so you can run it before or after setup or not run setup at all if all you really want is the Analyst VM itself.

**Joining to Grid**

You can optionally join your Analyst installation to your grid. This allows it to pull updates from the grid and automatically trust the grid's HTTPS certificate. It also updates the manager's firewall to allow the Analyst installation to connect. Please note that Analyst installations won't actually display on the :ref:`grid` page.

If you choose not to join your Analyst installation to your grid, then you may need to run :ref:`so-allow` on the manager node and choose the ``analyst`` option to allow the traffic through the host-based :ref:`firewall`.

**Disabling**

The analyst desktop is controlled via :ref:`salt` pillar. If you need to disable the Analyst desktop environment, find the ``workstation`` setting in your :ref:`salt` pillar and change ``enabled: true`` to ``enabled: false``:

::

	workstation:
	  gui:
	    enabled: false

.. toctree::
   :maxdepth: 2
   
   networkminer
   wireshark
