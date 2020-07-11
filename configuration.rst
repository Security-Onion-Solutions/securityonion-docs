.. _configuration:

Configuration
=============

Now that you've installed Security Onion, it's time to configure it! Security Onion is designed for many different use cases. Here are just a few examples.

.. tip::

  If this is your first time using Security Onion and you just want to try it out, we recommend the Evaluation option as it's the quickest and easiest way to get started.

Evaluation
----------

The Evaluation option allows you to quickly and easily evaluate Security Onion. It works well for classroom or small lab environments. Evaluation is **not** designed for production usage. Choose ``EVAL``, follow the prompts, and then proceed to the :ref:`post-installation` section.

Production Server - Standalone
------------------------------

Standalone is similar to Evaluation in that it only requires a single box, but Standalone is more ready for production usage. 

Choose ``STANDALONE``, follow the prompts, and then proceed to the :ref:`post-installation` section.

Production Server - Distributed Deployment
------------------------------------------

If deploying a distributed environment, you’ll need to perform the remaining steps on the manager node, as well as all forward and search nodes, but make sure you install and configure the manager node first. For best performance, the manager node should be dedicated to just being a server for the other nodes (the manager node should have no sniffing interfaces of its own). Please note that all nodes will need to be able to connect to the manager node on ports ``22``, ``4505``, and ``4506``.

Build the manager by following the prompts. Save the ``soremote`` password so that you can join nodes to the grid.

Build search nodes and join them to the manager node using the ``soremote`` password.

Build forward nodes and join them to the manager node using the ``soremote`` password.

Proceed to the :ref:`post-installation` section.

Sending Logs to Separate SIEM
-----------------------------

You can install Security Onion and then configure it to send logs to a separate SIEM.

For more information, please see the :ref:`syslog-output` section.
