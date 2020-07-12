.. _hive:

TheHive
=======

From https://thehive-project.org/:

    A scalable, open source and free Security Incident Response Platform, tightly integrated with MISP (Malware Information Sharing Platform), designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.
    
Credentials
-----------

| Username: hiveadmin  
| Password: hivechangeme  

Usage
-----

.. image:: https://user-images.githubusercontent.com/1659467/87230310-2d815380-c37d-11ea-9af8-a89a43afe0ef.png

:ref:`soc` provides a link to TheHive. TheHive should display the highest level of alerts. You can then triage those alerts and turn them into cases if necessary. Other analysts can collaborate with you as you work to close those cases. As you are working through a case and need more context, you can pivot to Kibana or Hunt as necessary.

In Kibana you will see a scripted field named ``TheHive`` with a value of ``Add2Hive``. This will use the API to add this new event to :ref:`hive`.

.. image:: https://github.com/Security-Onion-Solutions/securityonion/wiki/images/kibana_hive.png

Configuration
-------------
TheHive configuration can be found in ``/opt/so/conf/thehive/``.

Logging
-------
TheHive logging can be found at ``/opt/so/log/thehive/``.

More Information
----------------

.. seealso::

    For more information about TheHive, please see https://thehive-project.org/.
