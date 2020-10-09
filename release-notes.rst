.. _release-notes:

Release Notes
=============

Before downloading, please review the notes for this release.

Security Onion is now generally available and is at version 2.3!

Known Issues
------------

- It is still possible to update your grid from any release candidate to 2.3 but if this is a true production deployment, we recommend a fresh image and install.
- Please be patient as we update our documentation. We have made a concerted effort to update as much as possible but some things still may be incorrect or ommited. If you have questions or feedback, please start a discussion at https://securityonion.net/discuss.
- Once you update your grid to 2.3, any new nodes that join the grid must be 2.3 so if you try to join an older node it will fail. For best results, use the latest 2.3 ISO (or 2.3 installer from github) when joining to an 2.3 grid.
- Shipping Windows Eventlogs with Osquery will fail intermittently with utf8 errors logged in the Application log. This is scheduled to be fixed in Osquery 4.5.
- When running soup to upgrade from older versions to 2.3, there is a Salt error that may occur during the final highstate. This error is related to the patch_os_schedule and can be ignored as it should not occur again in subsequent highstates.
- When Search Nodes are upgraded from older versions to 2.3, there is a chance of a race condition where certificates are missing. This will show errors in the manager log to the remote node. To fix this run the following on the search node that is having the issue:

  - Stop elasticsearch - ``sudo so-elasticsearch-stop``
  - Run the SSL state - ``sudo salt-call state.apply ssl``
  - Restart elasticsearch - ``sudo so-elasticsearch-restart``

2.3.0 Changes
-------------

- New "Alerts" queue for reviewing all alerts for acknowledgement or escalation. You can then send the alerts to The Hive in a new case  
- The Hive no longer recieves alerts directly. We made this change due to user feedback and our own internal testing. The Hive would just get too cluttered with alerts making it impossible to effectively manage the events. Alerts allows you to slice and dice the alerts like you can in Hunt  
- ISO install now works for UEFI as well as Secure Boot    
- Airgap grids can now be updated using the latest ISO. Please read this documentation carefully    
- Suricata is now at 5.0.4     
- Zeek is at 3.0.11    
- Google Stenographer has been updated to the latest version     
- soup will now attempt to clean up old dockers to free up space    
- Users can now customize Hunt actions via the hunt.actions.json file  
- You can now modify the queries you want to display in the dropdown via hunt.queries.json  
- The eventfields that get displayed based on the serach can now be cutomized via hunt.eventfields.json.
- Alerts have similar json files where you can customize how you want to see things and start with alerts.function.json  
- Read more about customizing SOC here  



2.2.0 Changes
-------------

- Setup now includes an option for airgap installations
- Playbook now works properly when installed in airgap mode
- Added so-analyst script to create an analyst workstation with GNOME desktop, Chromium browser, Wireshark, and NetworkMiner
- Upgraded Zeek to version 3.0.10 to address a recent security issue
- Upgraded Docker to latest version
- Re-worked IDSTools to make it easier to modify
- Added so-* tools to the default path so you can now tab complete
- so-status can now be run from a manager node to get the status of a remote node. Run salt <target> so.status
- Salt now prevents states from running on a node that it shouldn't so you can't, for example, accidentally apply the elasticsearch state on a forward node
- Added logic to check for Salt mine corruption and recover automatically
- Collapsed Hunt filter icons and action links into a new quick action bar that will appear when a field value is clicked; actions include:

  - Filtering the hunt query
  - Pivot to PCAP
  - Create an alert in TheHive
  - Google search for the value
  - Analyze the value on VirusTotal.com
- Fixed minor bugs in Hunt user interface relating to most-recently used queries, tooltips, and more
- ``so-user-add`` now automatically adds users to Fleet and TheHive (in addition to SOC)
- Introduced ``so-user-disable`` and ``so-user-enable`` commands which allows administrators to lock out users that are no longer permitted to use Security Onion
- Added icon to SOC Users list representing their active or locked out status
- Removed User delete action from SOC interface in favor of disabling users for audit purposes
- Prune old PCAP job data from sensors once the results are streamed back to the manager node
- Hunt filtering to a specific value will search across all fields instead of only the field that was originally clicked
- Limiting PCAP jobs to extract at most 2GB from a sensor to avoid users accidentally requesting unreasonably large PCAP via the web interface
- ``so-test`` is back - run it to easily replay PCAPs and verify that all the components are working as expected
- New Elasticsearch subfield (``.security``) based on the new community-driven analyzer from @neu5ron - https://github.com/neu5ron/es_stk
- Playbook now uses the new .security subfield for case-insensitive wildcard searches


2.1.0 Changes
-------------

- Fixed an issue where the console was timing out and making it appear that the installer was hung
- Introduced Import node type ideal for running so-import-pcap to import pcap files and view the resulting logs in Hunt or Kibana
- Moved static.sls to global.sls to align the name with the functionality
- Traffic between nodes in a distributed deployment is now fully encrypted
- Playbook

  - Elastalert now runs active Plays every 3 minutes
  - Changed default rule-update config to only import Windows rules from the Sigma Community repo
  - Lots of bug fixes & stability improvements
- Ingest Node parsing updates for Osquery and Winlogbeat - implemented single pipeline for Windows eventlogs & sysmon logs
- Upgraded Osquery to 4.4 and re-enabled auto-updates
- Upgraded to Salt 3001.1
- Upgraded Wazuh to 3.13.1
- Hunt interface now shows the timezone being used for the selected date range
- Fixed Cortex initialization so that TheHive integration and initial user set is correctly configured
- Improved management of TheHive/Cortex credentials
- SOC now allows for arbitrary, time-bounded PCAP job creation, with optional filtering by host and port

2.0.3 Changes
-------------

- Resolved an issue with large drives and the ISO install  
- Modified ISO installation to use Logical Volume Management (LVM) for disk partitioning
- Updated Elastic Stack components to version 7.8.1
- Updated Zeek to version 3.0.8

2.0.2 Changes
-------------

- | Sensoroni fails on 2.0.1 ISO EVAL installation #1089
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1089
  
2.0.1 Changes
-------------

- | Security Fix: variables.txt from ISO install stays on disk for 10 days
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1067
  
- | Security Fix: Remove user values from static.sls
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1068
  
- | Fix distributed deployment sensor interval issue allowing PCAP
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1059
  
- | Support for passwords that start with special characters
  | https://github.com/Security-Onion-Solutions/securityonion/issues/1058
  
- Minor soup updates

2.0.0 Changes
-------------

- This version requires a fresh install, but there is good news - we have brought back :ref:`soup`! From now on, you should be able to run :ref:`soup` on the manager to upgrade your environment to RC2 and beyond!
- Re-branded 2.0 to give it a fresh look
- All documentation has moved to our docs site
- soup is alive! Note: This tool only updates Security Onion components. Please use the built-in OS update process to keep the OS and other components up to date
- so-import-pcap is back! See the docs here
- Fixed issue with so-features-enable
- Users can now pivot to PCAP from Suricata alerts
- ISO install now prompts users to create an admin/sudo user instead of using a default account name
- The web email & password set during setup is now used to create the initial accounts for TheHive, Cortex, and Fleet
- Fixed issue with disk cleanup
- Changed the default permissions for /opt/so to keep non-priviledged users from accessing salt and related files
- Locked down access to certain SSL keys
- Suricata logs now compress after they roll over
- Users can now easily customize shard counts per index
- Improved Elastic ingest parsers including Windows event logs and Sysmon logs shipped with WinLogbeat and Osquery (ECS)
- Elastic nodes are now "hot" by default, making it easier to add a warm node later
- so-allow now runs at the end of an install so users can enable access right away
- Alert severities across Wazuh, Suricata and Playbook (Sigma) have been standardized and copied to event.severity:

  - 1-Low / 2-Medium / 3-High / 4-Critical
  
- Initial implementation of alerting queues:

  - Low & Medium alerts are accessible through Kibana & Hunt
  - High & Critical alerts are accessible through Kibana, Hunt and sent to TheHive for immediate analysis
  
- ATT&CK Navigator is now a statically-hosted site in the nginx container
- Playbook

  - All Sigma rules in the community repo (500+) are now imported and kept up to date
  - Initial implementation of automated testing when a Play's detection logic has been edited (i.e., Unit Testing)
  - Updated UI Theme
  - Once authenticated through SOC, users can now access Playbook with analyst permissions without login
  
- Kolide Launcher has been updated to include the ability to pass arbitrary flags - new functionality sponsored by SOS
- Fixed issue with Wazuh authd registration service port not being correctly exposed
- Added option for exposure of Elasticsearch REST API (port 9200) to so-allow for easier external querying/integration with other tools
- Added option to so-allow for external Strelka file uploads (e.g., via strelka-fileshot)
- Added default YARA rules for Strelka -- default rules are maintained by Florian Roth and pulled from https://github.com/Neo23x0/signature-base
- Added the ability to use custom Zeek scripts
- Renamed "master server" to "manager node"
- Improved unification of Zeek and Strelka file data
