.. _configuration:

Configuration
=============

Now that you've installed Security Onion, it's time to configure it!

.. note::

  Setup uses keyboard navigation and you can use arrow keys to move around. Certain screens may provide a list and ask you to select one or more items from that list. You can use the space bar to select items and the Enter key to proceed to the next screen.

.. warning::

  If you use DHCP and your IP address changes, this can cause problems. If you want to use DHCP, make sure that you have a DHCP reservation so that your IP address does not change. Otherwise, use a static IP address to be safe.
  
Security Onion is designed for many different use cases. Here are just a few examples!
 
.. tip::

  If this is your first time using Security Onion and you just want to try it out, we recommend the Import option as it's the quickest and easiest way to get started.

Import
------

One of the easiest ways to get started with Security Onion is using it to forensically analyze one or more pcap files. Just install Security Onion in ``Import`` mode and then run `so-import-pcap <so-import-pcap>`__ giving it the full path to one or more pcap files. For more information, please see the `so-import-pcap <so-import-pcap>`__ section.

Evaluation
----------

``Evaluation Mode`` is ideal for classroom or small lab environments.  Evaluation is **not** designed for production usage. Choose ``EVAL``, follow the prompts (see screenshots below), and then proceed to the :ref:`post-installation` section.

Production Server - Standalone
------------------------------

Standalone is similar to Evaluation in that it only requires a single box, but Standalone is more ready for production usage. Choose ``STANDALONE``, follow the prompts, and then proceed to the :ref:`post-installation` section.

Production Server - Distributed Deployment
------------------------------------------

If deploying a distributed environment, install and configure the manager node first and then join the other nodes to it. For best performance, the manager node should be dedicated to just being a manager for the other nodes (the manager node should have no sniffing interfaces of its own). 

Please note that all nodes will need to be able to connect to the manager node on several ports and the manager will need to connect to search nodes and heavy nodes. You'll need to make sure that any network firewalls have firewall rules to allow this traffic as defined in the :ref:`firewall` section.

Build the manager by following the prompts. Save the ``soremote`` password so that you can join nodes to the manager.

Build search nodes and join them to the manager node using the ``soremote`` password.

Build forward nodes and join them to the manager node using the ``soremote`` password.

Proceed to the :ref:`post-installation` section.
