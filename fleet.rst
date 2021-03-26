.. _fleet:

Fleet
=====

From https://fleetdm.com/:

    Ask questions about your servers, containers, and laptops running Linux, Windows, and macOS. Quickly deploy osquery and scale your fleet to 50,000+ devices on top of a stable core technology.
    
Usage
-----

If you selected to enable Fleet during the setup, you can now login to Fleet using the email address and password that you entered during the installer. You can edit the password or add a new Fleet user within Fleet itself.

.. image:: images/fleet.png
  :target: _images/fleet.png

Custom :ref:`osquery` packages were generated for you during setup and you can find them under Downloads in :ref:`soc`. Before you install a package on an endpoint, use :ref:`so-allow` on your manager node to configure the firewall to allow inbound osquery connections.

Configuration
-------------

Fleet configuration can be found in ``/opt/so/conf/fleet/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

Diagnostic Logging
------------------

Fleet logs can be found in ``/opt/so/log/fleet/``.

More Information
----------------

.. seealso::

    For more information about osquery, please see the :ref:`osquery` section.

    For more information about Fleet, please see https://fleetdm.com/.
