Endgame
=======

Starting in Security Onion 2.3.90, we can ingest Endgame data by following the steps below.

.. note::

 Please keep in mind that we currently use the ``*:endgame-*`` index pattern for Endgame data. This means the data will not be visible using the native Security Onion dashboards/index pattern in Kibana. However, Endgame data will be natively viewable and aggregatable using Hunt and Elastic Security.

Configuration
-------------

**During Security Onion Setup**

To configure Endgame ingestion during setup, ensure the ``ENDGAMEHOST`` variable is set to the IP address of the Endgame SMP that you want to send data from:

::

 sudo ENDGAMEHOST=192.168.1.100 ./so-setup-network

This will open the Security Onion host-based firewall for access from the SMP to Security Onion on TCP port 3765.

------

**Post-Installation Setup**

To configure Endgame ingestion on an existing Security Onion installation, perform the following steps.

Add the SMP to the firewall exceptions for the Security Onion node:

::

 sudo so-firewall includehost endgame $smpip

Add the following to the ``soc`` pillar entry the manager's sls file in ``/opt/so/saltstack/local/pillar/minions`` to configure the pivot from SOC to Endgame (based on ``agent.id``):

::
 
  soc:
    endgamehost: $smpip
    
------

**Configure Event Streaming in Endgame SMP**

Once one of the two requirements above have been completed, the following must be configured in the Endgame web console:

Select ``Administration -> Streaming -> Event Streaming -> Add``. **Requires Admin user role**

Ensure ``Logstash`` is selected under the ``Destination`` options.

Next, copy the contents of ``/etc/ssl/certs/intca.crt`` (on the Security Onion manager node) to the ``Certificate`` section.

*Endgame will attempt to verify the X.509 certificate attributes match the destination server, so you will also need to ensure the SMP can resolve the hostname of the Security Onion node (to match the certificate).*  **This may require a hosts file entry on the SMP**.

Ensure the SMP is pointed to ``https://$securityonion:3765`` and save the configuration. 

Navigate to ``Administration -> Policy -> YOUR POLICY -> Settings -> Elastic Streaming`` and enable ``Event Streaming`` if not already enabled.

Once events are batched and published from the Endgame SMP, you can search for them in :ref:`dashboards` or :ref:`hunt` using a query like ``event.module:endgame``.

----------

Example Endgame Data
--------------------

.. image:: https://user-images.githubusercontent.com/16829864/142234485-31778c15-e534-4747-882f-b82aafd14589.png
 :target: https://user-images.githubusercontent.com/16829864/142234485-31778c15-e534-4747-882f-b82aafd14589.png


Pivot to Endgame Console
------------------------

If Endgame support is enabled, a default `Endgame` pivot will be populated within SOC, based on the ``agent.id`` field:

.. image:: https://user-images.githubusercontent.com/16829864/142237432-4657a104-1a98-47fd-98e2-0c800c025740.png
 :target: https://user-images.githubusercontent.com/16829864/142237432-4657a104-1a98-47fd-98e2-0c800c025740.png
 
.. image:: https://user-images.githubusercontent.com/16829864/142236568-5a19f356-b197-4bb4-99ee-8a74313bed11.png
 :target: https://user-images.githubusercontent.com/16829864/142236568-5a19f356-b197-4bb4-99ee-8a74313bed11.png
