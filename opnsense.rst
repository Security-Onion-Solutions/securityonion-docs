.. _opnsense:

OPNsense
========

OPNsense is a free and open firewall that can be found at https://opnsense.org/. You can integrate your OPNsense firewall with your Security Onion grid system to utilize it as a makeshift sensor, allowing management of Suricata rules through :ref:`detections`. This is particularly useful for organizations that find it challenging to install network taps on their egress connections.

Prerequisites
-------------

- **Security Onion Manager Access**: Access to the manager of your grid.
- **Administrative Rights**: Ability to modify settings in the OPNsense GUI.
- **SSH Access**: You must have SSH access to your OPNsense firewall.

Configuring Detections
----------------------

The :ref:`detections` module can now manage :ref:`nids` rules for external Suricata instances. Please refer to the :ref:`nids` section for detailed instructions on how to set this up.

Trust the Grid CA
-----------------

To establish a secure connection between your OPNsense firewall and the grid manager, your firewall will need to trust the grid's Certificate Authority (CA) certificate.

**Steps:**

1. **Copy the Grid CA Certificate:**

   - SSH into your grid manager.
   - Run the command ``cat /etc/pki/ca.crt`` to display the CA certificate.
   - Copy the entire output of that command.

2. **Import the CA Certificate into OPNsense:**

   - Log into the OPNsense GUI.
   - Navigate to **System** → **Trust** → **Authorities**.
   - Click the **+** button to add a new certificate authority.
   - Set **Method** to **Import an existing Certificate Authority**.
   - **Descriptive Name**: Enter a name like "Security Onion CA".
   - **Certificate Data**: Paste the copied CA certificate content.
   - Click **Save**.

Setting Up the Suricata Rules Repository
----------------------------------------

Since OPNsense doesn't allow enabling third-party repositories through the GUI, you'll need to modify the configuration manually.

**Steps:**

1. **Remove Existing Rule Repositories:**

   - SSH into your OPNsense firewall and run the following:

     .. code-block:: shell

        sudo rm -rf /usr/local/opnsense/scripts/suricata/metadata/rules/*

2. **Create a New Repository File:**

   - Create and edit the ``onion.xml`` file:

     .. code-block:: shell

        sudo vi /usr/local/opnsense/scripts/suricata/metadata/rules/onion.xml

   - Paste the following content into the file, replacing ``YOURMANAGER`` with the hostname or IP address of your grid manager:

     .. code-block:: xml

        <?xml version="1.0"?>
        <ruleset documentation_url="http://docs.opnsense.org/">
            <location url="https://YOURMANAGER:7789/" prefix="SecurityOnion"/>
            <files>
                <file description="SecurityOnion rules">all.rules</file>
                <file description="SecurityOnion" url="inline::all.rules">all.rules</file>
            </files>
        </ruleset>

   - Save and exit the editor.

3. **Refresh Rule Sets in OPNsense:**

   - Navigate to **Services** → **Intrusion Detection** → **Administration** → **Download** in the OPNsense GUI.
   - You should see **Security Onion** listed as a ruleset.
   - Select **Security Onion** and click **Download & Update Rules**.
   - Once updated, the rules will appear under the **Rules** tab.

Scheduling Rule Updates
-----------------------

To keep your Suricata rules up to date, schedule regular updates.

**Steps:**

1. Navigate to **Services** → **Intrusion Detection** → **Administration** → **Schedule**.
2. Click the **+** button to add a new schedule.
3. **Configure the Schedule:**

   - **Description**: Enter a name like "Suricata Rule Update".
   - **Cron Expression**: Set the frequency to every 15 minutes.
   - **Type**: Choose **Update and reload intrusion detection rules**.

4. Click **Save**.

OPNsense will now automatically download and reload the rules every 15 minutes.

.. note::

   When OPNsense downloads rules from Security Onion, it can only enable and disable rules. Threshold settings are ignored.

Enable NetFlow
--------------

To collect network flow data similar to Zeek's connection logs, configure NetFlow on OPNsense to send data to your grid.

**Steps:**

1. **Prepare Your Grid to Receive NetFlow Data:**

   - Refer to the :ref:`netflow` section to set up your grid for receiving NetFlow data.

2. **Configure NetFlow on OPNsense:**

   - Navigate to **Reporting** → **NetFlow** in the OPNsense GUI.
   - Under **Capture**, select the internal interfaces you wish to monitor.
   - Also, select your **WAN** interface to monitor external traffic.
   - Under **Destinations**, add a new destination:

     - **Hostname/IP Address**: Enter the IP address of the grid node configured to accept NetFlow data.
     - **Port**: Enter the port number you set up on the grid node.
     - **Format**: Choose the appropriate NetFlow version (e.g., NetFlow v5 or v9).

   - Click **Apply** to save the settings.

Sending Firewall Logs to the Grid
---------------------------------

Centralize your logging by sending OPNsense firewall logs to your grid.

**Steps:**

1. Navigate to **System** → **Settings** → **Logging** in the OPNsense GUI.
2. Click on the **Remote Logging** tab.
3. Click the **+** button to add a new remote logging destination.
4. **Configure Remote Logging:**

   - **Transport**: Select **TCP**.
   - **Application Levels**: Leave at default to send all logs or specify as needed.
   - **Facilities**: Leave at default to include all facilities or specify as needed.
   - **Hostname/IP Address**: Enter the IP address of the grid system where you set up the logging input.
   - **Port**: Enter the port number configured on the grid system.
   - **Format**: Choose the appropriate format (e.g., Syslog).

5. Click **Save** to apply the settings.
