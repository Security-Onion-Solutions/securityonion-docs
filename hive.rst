.. _hive:

TheHive
=======

From https://thehive-project.org/:

    A scalable, open source and free Security Incident Response Platform, tightly integrated with MISP (Malware Information Sharing Platform), designed to make life easier for SOCs, CSIRTs, CERTs and any information security practitioner dealing with security incidents that need to be investigated and acted upon swiftly.
    
Usage
-----

.. image:: https://user-images.githubusercontent.com/1659467/94850514-07f06d00-03f5-11eb-8071-6e45d82feec7.png
  :target: https://user-images.githubusercontent.com/1659467/94850514-07f06d00-03f5-11eb-8071-6e45d82feec7.png

As you are working in :ref:`alerts`, :ref:`hunt`, or :ref:`kibana`, you may find alerts or logs that are interesting enough to send to TheHive and create a case. Other analysts can collaborate with you as you work to close that case.

In :ref:`alerts` and :ref:`hunt`, you can use the blue triangle with an exclamation point to escalate to TheHive.

.. image:: https://user-images.githubusercontent.com/1659467/95380455-c9572880-08b4-11eb-8821-cee23b97d85e.png
  :target: https://user-images.githubusercontent.com/1659467/95380455-c9572880-08b4-11eb-8821-cee23b97d85e.png
  
In Kibana you will see a scripted field named ``Push to TheHive`` with a value of ``Click to create a case in TheHive``. This will use the API to add this new event to :ref:`hive`.

.. image:: https://user-images.githubusercontent.com/1659467/95380261-7da47f00-08b4-11eb-954a-613d1291ecb0.png
  :target: https://user-images.githubusercontent.com/1659467/95380261-7da47f00-08b4-11eb-954a-613d1291ecb0.png

Configuration
-------------

TheHive reads its configuration from ``/opt/so/conf/thehive/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

Diagnostic Logging
------------------

TheHive logging can be found at ``/opt/so/log/thehive/``.

More Information
----------------

.. seealso::

    For more information about TheHive, please see https://thehive-project.org/.
