.. _removing-a-node:

Removing a Node
===============

There may come a time when you need to remove a node from your distributed deployment. To do this, you'll need to remove the node's configuration from a few different components.

Salt
----

You can remove a node from salt by going to :ref:`administration` --> Configuration --> Grid Members. Find the Grid Member you would like to remove, click the REVIEW button, and then click the DELETE button.

SOC
---

To remove the node from the SOC Grid page, make sure the node is powered off and then restart SOC:

::

   sudo so-soc-restart
