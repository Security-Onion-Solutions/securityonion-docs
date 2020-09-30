.. _hive:

TheHive
=======

From https://thehive-project.org/:

    A scalable, open source and free Security Incident Response Platform, tightly integrated with MISP (Malware Information Sharing Platform), designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.
    
Usage
-----

.. image:: https://user-images.githubusercontent.com/1659467/87230310-2d815380-c37d-11ea-9af8-a89a43afe0ef.png
    :target: https://user-images.githubusercontent.com/1659467/87230310-2d815380-c37d-11ea-9af8-a89a43afe0ef.png

As you are working in :ref:`alerts`, :ref:`hunt`, or :ref:`kibana`, you may find alerts or logs that are interesting enough to send to TheHive and create a case. Other analysts can collaborate with you as you work to close that case.

In Kibana you will see a scripted field named ``TheHive`` with a value of ``Add2Hive``. This will use the API to add this new event to :ref:`hive`.

.. image:: https://github.com/Security-Onion-Solutions/securityonion/wiki/images/kibana_hive.png
    :target: https://github.com/Security-Onion-Solutions/securityonion/wiki/images/kibana_hive.png

Configuration
-------------

TheHive reads its configuration from ``/opt/so/conf/thehive/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

Diagnostic Logging
------------------

TheHive logging can be found at ``/opt/so/log/thehive/``.

Severity
--------

Currently, alerts sent to TheHive are hardcoded to severity 2. We are working on an :ref:`elastalert` tweak to set the correct severity.

More Information
----------------

.. seealso::

    For more information about TheHive, please see https://thehive-project.org/.
