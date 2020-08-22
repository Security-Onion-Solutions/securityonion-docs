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
:ref:`elastalert` and :ref:`suricata` rules are stored in ``/opt/so/rules/``.

/opt/so/saltstack/local
-----------------------
Custom :ref:`salt` settings can be added to ``/opt/so/saltstack/local/``.

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

/nsm/wazuh
-------------
All :ref:`wazuh` files are stored in ``/nsm/wazuh/``. For convenience, we have placed symlinks for Wazuh config at ``/opt/so/conf/wazuh`` (linked to `/nsm/wazuh/etc`) and Wazuh rules at ``/opt/so/rules/hids`` (``local_rules.xml`` links to ``/nsm/wazuh/etc/rules/local_rules.xml`` and ``ruleset`` links to ``/nsm/wazuh/ruleset``).
