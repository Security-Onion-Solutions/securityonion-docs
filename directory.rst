.. _directory:

Directory Structure
===================

/opt/so/conf
------------
Configuration files are stored in ``/opt/so/conf/``.

/opt/so/log
-----------
Debug logs are stored in ``/opt/so/log/``.

/opt/so/rules
-------------
ElastAlert and NIDS rules are stored in ``/opt/so/rules/``.

/opt/so/saltstack/local
-----------------------
Custom salt settings can be added to ``/opt/so/saltstack/local/``.

/opt/so/wazuh
-------------
Wazuh configuration and rules are stored in ``/opt/so/wazuh/``.

/nsm
----
The vast majority of data is stored in ``/nsm/``.

/nsm/zeek
---------
:ref:`zeek` writes its protocol logs to ``/nsm/zeek/``.

/nsm/elasticsearch
------------------
:ref:`elasticsearch` stores its data in ``/nsm/elasticsearch/``.

/nsm/pcap
---------
:ref:`stenographer` stores full packet capture in ``/nsm/pcap/``.
