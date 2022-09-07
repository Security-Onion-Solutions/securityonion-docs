.. _directory:

Directory Structure
===================

/opt/so/conf
------------
Applications read their configuration from ``/opt/so/conf/``. However, please keep in mind that most config files are managed with :ref:`salt`, so if you manually modify those config files, your changes may be overwritten at the next Salt update.

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
