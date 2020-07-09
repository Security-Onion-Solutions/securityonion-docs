.. _fleet:

Fleet
=====

From https://www.kolide.com/fleet/:

    Expand osquery capabilities from a single machine to your entire fleet. Query dynamic sets of hosts, and watch the data stream in for immediate analysis and investigation. Export results for a closer look in your favorite tools.
    
Usage
-----

If you selected to install Fleet during the setup, you can now login to Fleet using the email & password that you entered during the installer. You can edit the password or add a new Fleet user within Fleet itself.

Osquery packages were generated during setup and you can find them under Downloads in the :ref:`soc`. They are customized specifically for your Security Onion install. Before you install a package on an endpoint, use ``sudo so-allow`` on your management server to configure the SO firewall to allow inbound osquery connections.

More Information
----------------

For more information about osquery, please see the osquery section.

For more information about Fleet, please see https://www.kolide.com/fleet/.
