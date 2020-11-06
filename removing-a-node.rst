.. _removing-a-node:

Removing a Node
===============

There may come a time when you need to remove a node from your distributed deployment. To do this, log into your manager and list all :ref:`salt` keys:

::

   sudo salt-key

Then remove the node by deleting its key from :ref:`salt` (replacing ``nodename`` with the actual node name):

::

   sudo salt-key -d nodename

Remove search node
------------------

If you are removing a search node, you will want to remove it from cross cluster search. In :ref:`kibana`, navigate to ``Dev Tools`` and paste the following text into the window (replacing ``nodename`` with the actual node name):

::

    PUT _cluster/settings
    {
      "persistent": {
        "search": {
          "remote": {
            "nodename": {
              "skip_unavailable": null,
              "seeds":null
            }
          }
        }
      }  
    }

Click the play button to send the request to :ref:`elasticsearch`.
