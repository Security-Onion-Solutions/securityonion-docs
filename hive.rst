.. _hive:

TheHive
=======

.. warning::

	Starting in Security Onion 2.3.100, we are transitioning from TheHive to :ref:`cases`. Existing installations with TheHive enabled will still be able to use TheHive for a very short time. However, new installations will not be able to enable TheHive. We will stop including TheHive and Cortex container images starting in Security Onion 2.3.120, currently scheduled for release in March 2022. From that point forward, users running the current version of Security Onion will no longer be able to natively run TheHive on the platform and our support for TheHive on Security Onion will end. Users wishing to continue using TheHive on Security Onion should plan to migrate to an external instance of TheHive. For now, users will still be able to escalate events from Security Onion Console to external instances of TheHive version 3.

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
  
Clicking the escalate button will escalate the data from the row as it is displayed. This means that if you're looking at an aggregated view, you will get limited details in the resulting escalated case. If you want more details to be included in the case, then first drill into the aggregation and escalate one of the individual items in that aggregation.
  
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
