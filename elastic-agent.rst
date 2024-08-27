.. _elastic-agent:

Elastic Agent
=============

From https://www.elastic.co/elastic-agent:

    With Elastic Agent you can collect all forms of data from anywhere with a single unified agent per host. One thing to install, configure, and scale.
      
Each Security Onion node uses the Elastic Agent to transport logs to :ref:`elasticsearch`. You can also deploy the Elastic Agent to your endpoints to transport logs to your Security Onion deployment.

Deployment
----------

.. note::

   In order to receive logs from the Elastic Agent, Security Onion must be running :ref:`logstash`. Evaluation Mode and Import Mode do not run :ref:`logstash`, so you'll need Standalone or a full Distributed Deployment. In a Distributed Deployment, forward nodes do not run :ref:`logstash`, so you'll need to configure agents to send to your manager or receiver nodes. For more information, please see the :ref:`architecture` section.

To deploy an Elastic agent to an endpoint, go to the :ref:`soc` :ref:`downloads` page and download the proper Elastic agent for the operating system of that endpoint. Don't forget to allow the agent to connect through the firewall by going to :ref:`administration` --> Configuration --> firewall --> hostgroups.

.. image:: images/config-item-firewall.png
  :target: _images/config-item-firewall.png

Once there, select the ``elastic_agent_endpoint`` option.

.. note::

    Check out our Elastic Agent video at https://youtu.be/cGmQMsFuAvw!

Linux
~~~~~

If deploying the Elastic Agent to a Linux host, make the file executable and then execute using sudo:

::

    chmod +x ./so-elastic-agent_linux_amd64
    sudo ./so-elastic-agent_linux_amd64

MacOS
~~~~~

If deploying the Elastic Agent to macOS, you will need to take a few steps. First, remove the quarantine attribute. Then, make the file executable. Finally, execute the file using sudo:

::

    xattr -d com.apple.quarantine ./so-elastic-agent_darwin_amd64
    chmod +x ./so-elastic-agent_darwin_amd64
    sudo ./so-elastic-agent_darwin_amd64

After the installer has completed, review the Elastic docs for your version of macOS and approve the required settings (system extension and full drive access) as shown at https://www.elastic.co/guide/en/security/current/elastic-endpoint-deploy-reqs.html.

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

You can read more about integrations in the :ref:`elastic-fleet` section and at https://docs.elastic.co/integrations.

Reinstalling
------------

If for some reason you need to uninstall and reinstall the Elastic Agent on one of your Security Onion grid members, you can do so as follows:

::

        sudo elastic-agent uninstall
        sudo salt-call state.apply elasticfleet.install_agent_grid

More Information
----------------

.. note::

    For more information about the Elastic Agent, please see https://www.elastic.co/guide/en/fleet/current/fleet-overview.html.
