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
   
Cross Cluster Search
--------------------

If you are removing a search node, you will want to remove it from cross cluster search. To do so, you'll need to update that search node's settings in ``_cluster/settings`` and make sure that any settings are set to ``null``. So you might want to start by doing the following query via :ref:`so-elasticsearch-query`:

::

   sudo so-elasticsearch-query _cluster/settings
   
Then based on that output, update ``_cluster/settings`` by sending that node section back but with all settings set to ``null``. You could use :ref:`so-elasticsearch-query` again or use :ref:`kibana`'s ``Dev Tools`` and paste something like the following text into the window (replacing ``nodename`` with the actual node name and adding any other settings as necessary):

::

    PUT _cluster/settings
    {
      "persistent": {
        "cluster": {
          "remote": {
            "nodename": {
              "skip_unavailable": null,
              "seeds":null
            }
          }
        }
      }  
    }


.. note::

   | For more information, please see:
   | https://www.elastic.co/guide/en/elasticsearch/reference/current/modules-remote-clusters.html#configure-remote-clusters-dynamic
