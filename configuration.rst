.. _configuration:

Configuration
=============

Now that you've installed Security Onion, it's time to configure it! Security Onion is designed for many different use cases. Here are just a few examples.

.. tip::

  If this is your first time using Security Onion and you just want to try it out, we recommend the Evaluation option as it's the quickest and easiest way to get started.

.. note::

  If you install directly in a console (rather than an SSH session), the console may timeout causing the install to appear to hang. If this happens, simply press an arrow key on your keyboard to wake the console up.
  
.. warning::

  If you use DHCP and your IP address changes, this can cause problems. If you want to use DHCP, make sure that you have a DHCP reservation so that your IP address does not change. Otherwise, use a static IP address to be safe.
  
Evaluation
----------

The Evaluation option allows you to quickly and easily evaluate Security Onion. It works well for classroom or small lab environments. Evaluation is **not** designed for production usage. Choose ``EVAL``, follow the prompts (see screenshots below), and then proceed to the :ref:`post-installation` section.

Production Server - Standalone
------------------------------

Standalone is similar to Evaluation in that it only requires a single box, but Standalone is more ready for production usage. 

Choose ``STANDALONE``, follow the prompts, and then proceed to the :ref:`post-installation` section.

Production Server - Distributed Deployment
------------------------------------------

If deploying a distributed environment, install and configure the manager node first and then join the other nodes to it. For best performance, the manager node should be dedicated to just being a manager for the other nodes (the manager node should have no sniffing interfaces of its own). Please note that all nodes will need to be able to connect to the manager node on ports ``22``, ``4505``, and ``4506``.

Build the manager by following the prompts. Save the ``soremote`` password so that you can join nodes to the manager.

Build search nodes and join them to the manager node using the ``soremote`` password.

Build forward nodes and join them to the manager node using the ``soremote`` password.

Proceed to the :ref:`post-installation` section.

Screenshots
-----------

The following screenshots are from an ``EVAL`` installation with all services enabled. Your screens may be different depending on what options you choose.

.. image:: https://user-images.githubusercontent.com/1659467/87330029-f5f1e300-c505-11ea-8a8d-2a5cbf0eeeed.png

.. image:: https://user-images.githubusercontent.com/1659467/90795908-a5c42880-e2dc-11ea-87d6-6252c9866d6b.png

.. image:: https://user-images.githubusercontent.com/1659467/87334336-7b789180-c50c-11ea-94e0-0c5aded8799d.png

.. image:: https://user-images.githubusercontent.com/1659467/87334404-9519d900-c50c-11ea-89e7-80a5b70fc683.png

.. image:: https://user-images.githubusercontent.com/1659467/87334452-a8c53f80-c50c-11ea-9661-602ae7047183.png

.. image:: https://user-images.githubusercontent.com/1659467/87334531-ca262b80-c50c-11ea-98b6-440ee2bcdbe1.png

.. image:: https://user-images.githubusercontent.com/1659467/87334570-dca06500-c50c-11ea-9760-a8a75a26664a.png

.. image:: https://user-images.githubusercontent.com/1659467/87334614-ef1a9e80-c50c-11ea-9eb8-5feff68b8e26.png

.. image:: https://user-images.githubusercontent.com/1659467/87334660-ff327e00-c50c-11ea-917b-6a3891ec003b.png

.. image:: https://user-images.githubusercontent.com/1659467/87334698-12454e00-c50d-11ea-9fc0-6364cedb8232.png

.. image:: https://user-images.githubusercontent.com/1659467/87334750-2426f100-c50d-11ea-97c0-ab11180f78f8.png

.. image:: https://user-images.githubusercontent.com/1659467/87334796-36a12a80-c50d-11ea-9160-4b3b4c27e531.png

.. image:: https://user-images.githubusercontent.com/1659467/87334827-4751a080-c50d-11ea-8703-e914e876d536.png

.. image:: https://user-images.githubusercontent.com/1659467/87334864-57698000-c50d-11ea-8eaf-11ecaed403b8.png

.. image:: https://user-images.githubusercontent.com/1659467/87334902-68b28c80-c50d-11ea-8682-b59a5302c587.png

.. image:: https://user-images.githubusercontent.com/1659467/87335033-a0213900-c50d-11ea-8eca-73ae73ba5f5c.png

