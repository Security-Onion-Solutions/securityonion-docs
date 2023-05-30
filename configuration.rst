.. _configuration:

Configuration
=============

Now that you've installed Security Onion, it's time to configure it!

.. image:: images/04_setup_init.png
  :target: _images/04_setup_init.png

Security Onion is designed for many different use cases. Here are just a few examples!
 
.. tip::

  If this is your first time using Security Onion and you just want to try it out, we recommend the Import option as it's the quickest and easiest way to get started.

Import
------

One of the easiest ways to get started with Security Onion is using it to forensically analyze pcap and log files. Just install Security Onion in ``Import`` mode and then run :ref:`so-import-pcap` to import pcap files or :ref:`so-import-evtx` to import Windows event logs in EVTX format.

Evaluation
----------

``Evaluation Mode`` is ideal for classroom or small lab environments.  Evaluation is **not** designed for production usage. Choose ``EVAL``, follow the prompts (see screenshots below), and then proceed to the :ref:`post-installation` section.

Production Server - Standalone
------------------------------

Standalone is similar to Evaluation in that it only requires a single box, but Standalone is more ready for production usage. Choose ``STANDALONE``, follow the prompts, and then proceed to the :ref:`post-installation` section.

Production Server - Distributed Deployment
------------------------------------------

If deploying a distributed environment, install and configure the manager node first and then join the other nodes to it. For best performance, the manager node should be dedicated to just being a manager for the other nodes (the manager node should have no sniffing interfaces of its own). 

Build the manager by running Setup, selecting the ``DISTRIBUTED`` install submenu, and choosing the ``New Deployment`` option. You can choose either ``MANAGER`` or ``MANAGERSEARCH``. If you choose ``MANAGER``, then you must join one or more search nodes (this is optional if you choose ``MANAGERSEARCH``) and you will want to do this before you start joining other node types.

Build nodes by running Setup, selecting the ``DISTRIBUTED`` install submenu, choosing ``Existing Deployment``, and selecting the appropriate option. Please note that all nodes will need to be able to connect to the manager node on several ports and the manager will need to connect to search nodes and heavy nodes. You'll need to make sure that any network firewalls have firewall rules to allow this traffic as defined in the :ref:`firewall` section. In addition to network firewalls, you'll need to make sure the manager's host-based firewall allows the connections. You can do this in two ways. The first option is going to :ref:`administration` --> Configuration --> firewall --> hostgroups, selecting the appropriate node type, and adding the IP address. The second option is to wait until the node tries to join and it will prompt you to run a specific command on the manager. When the node initialization completes, it will prompt you to go to :ref:`administration` --> Grid Members, find the node in the Pending Members list, click the ``Review`` button, and then click the ``Accept`` button.

Proceed to the :ref:`post-installation` section.
