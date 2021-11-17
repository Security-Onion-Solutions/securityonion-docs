Endgame
==============

Starting in Secrity Onion 2.3.90, we can ingest Endgame data, following the steps below.

Please keep in mind, we currently use the ``*:endgame-*`` index pattern for Endgame data, therefore 
the data will not be visible using the native Security Onion dashboards/index pattern in Kibana. However, Endgame 
data will be natively viewable and aggregatable using Hunt and Elastic Security.

Configuration
------------

**Before Setup**

To configure Endgame ingestion during setup, ensure the ``ENDGAMEHOST`` variable is set to the IP address of the Endgame SMP form which you intended to send data:

``sudo ENDGAMEHOST=192.168.1.100 ./so-setup-network``

This will open the Security Onion host-based firewall for access from the SMP to Security Onion on TCP port 3765.


**After Setup**

To configure Endgame ingestion after setup, perform the following steps:

Add the SMP to the firewall exceptions for the Security Onion node:

``sudo so-firewall includehost endgame $smpip``

Add the following to the ``soc`` pillar entry the manager's sls file in ``/opt/so/saltstack/local/pillar/minions`` to configure the pivot from SOC to Endgame (based on ``agent.id``):

::
 
  soc:
    endgamehost: $yoursmp
    


**Configure Event Streaming**

Next, copy the contents of ``/etc/ssl/certs/intca.crt`` (on the Security Onion manager node) to the certificate section in the configuration for event streamining within the SMP web console.

You will also need to ensure the SMP can resolve the hostname of the Security Onion node (to match the certificate).  **This may require a hosts file entry on the SMP**.

Ensure the SMP is pointed to ``https://$securityonion:3765`` and save the configuration. Once events are batched and published from the Endgame SMP, they will be accessible in Hunt, using:

``event.module:endgame``

**Example Endgame Data**

.. image:: https://user-images.githubusercontent.com/16829864/142234485-31778c15-e534-4747-882f-b82aafd14589.png
 :target: https://user-images.githubusercontent.com/16829864/142234485-31778c15-e534-4747-882f-b82aafd14589.png
