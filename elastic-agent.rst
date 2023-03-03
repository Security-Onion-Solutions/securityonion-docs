.. _elastic-agent:

Elastic Agent
=============

From https://www.elastic.co/elastic-agent:

    With Elastic Agent you can collect all forms of data from anywhere with a single unified agent per host. One thing to install, configure, and scale.
      
Each Security Onion node uses the Elastic Agent to transport logs to :ref:`elasticsearch`. You can also deploy the Elastic Agent to your endpoints to transport logs to your Security Onion deployment.

Deployment
----------

To deploy an Elastic agent to an endpoint, go to the :ref:`soc` :ref:`downloads` page and download the proper Elastic agent for the operating system of that endpoint. Don't forget to allow the agent to connect through the firewall by going to :ref:`administration` --> Configuration --> firewall.

Logs
----

Once the agent starts sending logs, you should be able to find them in :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana`.

More Information
----------------

.. note::

    For more information about the Elastic Agent, please see https://www.elastic.co/guide/en/fleet/current/fleet-overview.html.
