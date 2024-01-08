.. _post-installation:

After Installation
==================

Services
--------

You can check the :ref:`grid` page to see if all services are running correctly.

.. image:: images/39_grid.png
  :target: _images/39_grid.png

.. note::

  Please note that new nodes start off showing a red Fault and may take a few minutes to fully initialize before they show a green OK.

You can also verify services are running from the command line with the :ref:`so-status` command:

::

	sudo so-status
	
Adjust firewall rules
---------------------

Depending on what kind of installation you did, the Setup wizard may have already walked you through adding firewall rules to allow your analyst IP address(es). If you need to make other adjustments to firewall rules, you can do so by going to :ref:`administration` --> Configuration --> firewall --> hostgroups.

.. image:: images/config-item-firewall.png
  :target: _images/config-item-firewall.png

SSH
---

You should be able to do most administration from :ref:`soc` but if you need access to the command line then we recommend using :ref:`ssh` rather than the :ref:`console`.

Data Retention
--------------

-  Review the :ref:`elasticsearch` section to see if you need to change any of the default index retention settings.

Other
-----

-  Full-time analysts may want to connect using a dedicated :ref:`desktop`.

-  Any IDS/NSM system needs to be tuned for the network it’s monitoring. Please see the :ref:`tuning` section. 

-  Configure the OS to use your preferred :ref:`ntp` server.
