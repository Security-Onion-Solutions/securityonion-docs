.. _removing-a-node:

Removing a Node
===============

There may come a time when you need to remove a node from your distributed deployment. To do this, log into your manager and list all salt keys:

::

   sudo salt-key

Then remove the sensor by deleting its key from salt (replacing ``sensor_key_name`` with the actual name):

::

   sudo salt-key -d sensor_key_name

Remove search node
------------------

If you are removing a search node, you will want to remove it from cross cluster search. In :ref:`kibana`, navigate to ``Dev Tools`` and paste the following text into the window (modifying ``nodename`` to match the name of your node):

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
