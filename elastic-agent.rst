.. _elastic-agent:

Elastic Agent
=============

From https://www.elastic.co/elastic-agent:

    With Elastic Agent you can collect all forms of data from anywhere with a single unified agent per host. One thing to install, configure, and scale.
      
Each Security Onion node uses the Elastic Agent to transport logs to :ref:`elasticsearch`. You can also deploy the Elastic Agent to your endpoints to transport logs to your Security Onion deployment.

Deployment
----------

To deploy an Elastic agent to an endpoint, go to the :ref:`soc` :ref:`downloads` page and download the proper Elastic agent for the operating system of that endpoint. Don't forget to allow the agent to connect through the firewall by going to :ref:`administration` --> Configuration --> firewall.

.. note::

   In order to receive logs from the Elastic Agent, Security Onion must be running :ref:`logstash`. Evaluation Mode and Import Mode do not run :ref:`logstash`, so you'll need Standalone or a full Distributed Deployment. In a Distributed Deployment, forward nodes do not run :ref:`logstash`, so you'll need to configure agents to send to your manager or receiver nodes. For more information, please see the :ref:`architecture` section.

Logs
----

Once the agent starts sending logs, you should be able to find them in :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana`.

Management
----------

You can manage your agents using :ref:`elastic-fleet`.

Live Queries
------------

You can query your agents in realtime using :ref:`osquery-manager`.

Integrations
------------

You can read more about integrations at :ref:`elastic-fleet` and https://docs.elastic.co/integrations.

More Information
----------------

.. note::

    For more information about the Elastic Agent, please see https://www.elastic.co/guide/en/fleet/current/fleet-overview.html.
