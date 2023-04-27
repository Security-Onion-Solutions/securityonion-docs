.. _desktop:

Security Onion Desktop
======================

Full-time analysts may want to use a dedicated Security Onion desktop. This allows you to investigate pcaps, malware, and other potentially malicious artifacts without impacting your Security Onion deployment or your usual desktop environment.

.. image:: images/desktop.png
  :target: _images/desktop.png

.. note::

  Security Onion Desktop currently only supports Rocky Linux 9, so you'll either need to use our Security Onion ISO image (recommended) or a manual installation of Rocky Linux 9.
  
Security Onion Desktop consists of a full GNOME desktop environment including Chromium web browser, :ref:`networkminer`, :ref:`wireshark`, and other analyst tools.
 
**Installation**

There are a few different ways to install Security Onion Desktop:

- Our Security Onion ISO image includes a boot menu option for Desktop installs that will partition your disk appropriately and immediately perform a Desktop installation.

- In our normal Setup wizard, you can choose ``OTHER`` and then choose ``ANALYST``.

- The ``so-analyst-install`` command is totally independent of the standard setup process, so you can run it before or after setup or not run setup at all if all you really want is the Analyst desktop itself.

**Joining to Grid**

You can optionally join your Desktop installation to your grid. This allows it to pull updates from the grid and automatically trust the grid's HTTPS certificate. It also updates the manager's firewall to allow the Desktop installation to connect. Please note that Desktop installations won't actually display on the :ref:`grid` page.

If you choose not to join your Desktop installation to your grid, then you may need to run :ref:`so-allow` on the manager node and choose the ``analyst`` option to allow the traffic through the host-based :ref:`firewall`.

**Disabling**

The analyst desktop is controlled via :ref:`salt` pillar. If you need to disable the Desktop desktop environment, find the ``workstation`` setting in your :ref:`salt` pillar and change ``enabled: true`` to ``enabled: false``:

::

	workstation:
	  gui:
	    enabled: false

.. toctree::
   :maxdepth: 2
   
   networkminer
   wireshark
