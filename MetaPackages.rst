Metapackages
============

Security Onion consists of over 50 packages in a Launchpad PPA. You can install these packages individually or you can install one or more metapackages (groups of packages) depending on what functionality you need.

-  | securityonion-client (about 525MB)
   | Sguil client, Wireshark, NetworkMiner, etc.
   
   ::
   
      sudo apt install securityonion-client

-  | securityonion-sensor (about 135MB)
   | Snort, Suricata, Bro, netsniff-ng, Sguil agents, etc.
   
   ::
   
      sudo apt install securityonion-sensor

-  | securityonion-server (about 265MB)
   | Sguil server, Squert, CapMe, etc.
   
   ::
   
      sudo apt install securityonion-server

-  | securityonion-elastic (about 5MB)
   | Scripts and configuration files for the Elastic Stack (Elasticsearch, Logstash, and Kibana) and its associated log pipeline including syslog-ng. This package includes ``so-elastic-download`` which downloads the Docker images for the Elastic stack. You'll probably want to install syslog-ng-core explicitly to replace rsyslog.
   
   ::
   
      sudo apt install securityonion-elastic syslog-ng-core

-  | securityonion-all (about 930MB)
   | all of the above plus syslog-ng
   
   ::
   
      sudo apt install securityonion-all

-  | securityonion-iso
   | all of the above plus bridge-utils, byobu, foremost, pinguybuilder, securityonion-desktop-gnome, securityonion-onionsalt, securityonion-samples-bro, securityonion-samples-markofu, securityonion-samples-mta, securityonion-samples-shellshock, xfsprogs
   
   ::
   
      sudo apt install securityonion-iso
