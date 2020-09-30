.. _fleet:

Fleet
=====

From https://www.kolide.com/fleet/:

    Expand osquery capabilities from a single machine to your entire fleet. Query dynamic sets of hosts, and watch the data stream in for immediate analysis and investigation. Export results for a closer look in your favorite tools.
    
Usage
-----

If you selected to enable Fleet during the setup, you can now login to Fleet using the email address and password that you entered during the installer. You can edit the password or add a new Fleet user within Fleet itself.

.. image:: https://user-images.githubusercontent.com/1659467/87230293-fe6ae200-c37c-11ea-8de2-3138202107ca.png
    :target: https://user-images.githubusercontent.com/1659467/87230293-fe6ae200-c37c-11ea-8de2-3138202107ca.png

Custom :ref:`osquery` packages were generated for you during setup and you can find them under Downloads in :ref:`soc`. Before you install a package on an endpoint, use ``sudo so-allow`` on your manager node to configure the SO firewall to allow inbound osquery connections.

Configuration
-------------

Fleet configuration can be found in ``/opt/so/conf/fleet/``.

Diagnostic Logging
------------------

Fleet logs can be found in ``/opt/so/log/fleet/``.

More Information
----------------

.. seealso::

    For more information about osquery, please see the :ref:`osquery` section.

    For more information about Fleet, please see https://www.kolide.com/fleet/.
