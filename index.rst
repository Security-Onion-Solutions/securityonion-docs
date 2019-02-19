Security Onion Documentation
=======================================

Welcome to the Security Onion Documentation!

Formats
-------

This documentation is published online at https://securityonion.net/docs.  If you are viewing an offline version of this documentation but have Internet access, you might want to switch to the online version at https://securityonion.net/docs to see the latest version.

| This documentation is also available in PDF format:
| https://readthedocs.org/projects/securityonion/downloads/pdf/latest/

Contributing
------------
| If you notice any documentation is missing or incorrect, please feel free to submit a pull request (PR) to the following repo:
| https://github.com/Security-Onion-Solutions/securityonion-docs

We will review the PR and merge if appropriate.

Naming Convention
-----------------
Our goal is to allow you to easily guess and type the URL of the documentation you want to go to.

| For example, if you want to read more about Suricata, you can type the following into your browser: 
| https://securityonion.net/docs/suricata

To achieve this goal, new documentation pages should use the following naming convention:

- all lowercase
- ``.rst`` file extension
- ideally, the name of the page should be one simple word (for example: ``suricata.rst``)
- try to avoid symbols such as hyphens and underscores
- if symbols are required, hyphens are preferred to underscores


.. toctree::
   :maxdepth: 2
   :caption: Getting Started

   about
   IntroductionToSecurityOnion
   Use-Cases
   Hardware
   Release-Notes
   Installation
   QuickISOImage
   InstallingOnUbuntu
   ProductionDeployment
   PostInstallation
   TimeZones
   Services
   IntroductionWalkthrough
   VMWare-Walkthrough
   Videos
   Elastic-Architecture
   Cheat-Sheet
   Conference

.. _updateupgrade:

.. toctree::
   :maxdepth: 2
   :caption: Update/Upgrade

   Upgrade
   HWE
   Upgrading-from-14.04-to-16.04
   MySQL-Upgrade-Errors
   EOL

.. _analysttools:

.. toctree::
   :maxdepth: 2
   :caption: Analyst Tools

   Kibana
   CapMe
   CyberChef
   Squert
   Sguil
   networkminer

.. _networkvisibility:

.. toctree::
   :maxdepth: 2
   :caption: Network Visibility

   NIDS
   Snort
   Suricata
   Bro
   netsniff-ng

.. _hostvisibility:

.. toctree::
   :maxdepth: 2
   :caption: Host Visibility

   Beats
   Wazuh
   Sysmon
   Autoruns
   Syslog

.. _elasticstack:

.. toctree::
   :maxdepth: 2
   :caption: Elastic Stack

   Elastic
   Elasticsearch
   Logstash
   Kibana
   ElastAlert
   Curator
   FreqServer
   DomainStats
   Docker
   Redis
   Data-Fields
   Alert-Data-Fields
   Bro-Fields
   Elastalert-Fields
   Beats
   ELSA-to-Elastic
   Re‐Indexing

.. _customizing:

.. toctree::
   :maxdepth: 2
   :caption: Customizing for your network

   NetworkConfiguration
   Proxy
   Firewall
   Email
   ChangingIPAddress
   NTP

.. _tuning:

.. toctree::
   :maxdepth: 2
   :caption: Tuning

   ManagingAlerts
   Rules
   AddingLocalRules
   DisablingProcesses
   BPF
   PF_RING
   AF-PACKET
   MySQLTuning
   NewDisk
   High-Performance-Tuning
   Trimming-PCAPs

.. _tricksandtips:

.. toctree::
   :maxdepth: 2
   :caption: Tricks and Tips

   Airgapped-Networks
   Analyst-VM
   Automating-Setup
   Best-Practices
   CloudClient
   ConnectingtoSguil
   Desktop
   DNSAnomalyDetection
   ICMP-Anomaly-Detection
   MetaPackages
   Pcaps
   RemovingASensor
   Salt
   SensorStopsSeeingTraffic
   SSH

.. _integrations:

.. toctree::
   :maxdepth: 2
   :caption: Integrations

   Alienvault-OTX
   CriticalStackIntelClient
   Etherpad
   FIR
   GRR
   MISP
   DeployingNtopng
   RITA
   strelka
   ThirdPartyIntegration

.. _help:

.. toctree::
   :maxdepth: 2
   :caption: Help

   Support
   Help
   FAQ
   Passwords
   MailingLists
   TeamMembers
   Secure-Boot
   Security
   TroubleBooting

.. _other:

.. toctree::
   :maxdepth: 2
   :caption: Other

   DirectoryStructure
   Tools
   so-import-pcap
