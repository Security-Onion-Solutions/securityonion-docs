.. _strelka:

Strelka
=======

From https://github.com/target/strelka:

    Strelka is a real-time file scanning system used for threat hunting, threat detection, and incident response. Based on the design established by Lockheed Martin's Laika BOSS and similar projects (see: related projects), Strelka's purpose is to perform file extraction and metadata collection at huge scale.

Depending on what options you choose in Setup, it may ask if you want to use :ref:`zeek` or :ref:`suricata` for metadata. Whichever engine you choose for metadata will then extract files from network traffic. Strelka then analyzes those files and they end up in ``/nsm/strelka/processed/``.

Alerts
------
Strelka scans files using YARA rules. If it detects a match, then it will generate an alert that can be found in :ref:`alerts`, :ref:`hunt`, or :ref:`kibana`. Here are some screenshots from :ref:`alerts` that show Strelka detecting Poison Ivy RAT:

.. image:: images/strelka-alert-1.png
  :target: _images/strelka-alert-1.png

.. image:: images/strelka-alert-2.png
  :target: _images/strelka-alert-2.png

.. image:: images/strelka-alert-3.png
  :target: _images/strelka-alert-3.png

.. image:: images/strelka-alert-4.png
  :target: _images/strelka-alert-4.png

Logs
----
Even if Strelka doesn't detect a YARA match, it will still log metadata about the file. You can find Strelka logs in :ref:`hunt` and :ref:`kibana`. Here's an example of Strelka logs in :ref:`hunt`:

.. image:: images/strelka.png
  :target: _images/strelka.png

Configuration
-------------
Strelka reads its configuration from ``/opt/so/conf/strelka/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

More Information
----------------

.. seealso::

    For more information about Strelka, please see https://github.com/target/strelka.
