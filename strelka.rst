.. _strelka:

Strelka
=======

From https://github.com/target/strelka:

    Strelka is a real-time file scanning system used for threat hunting, threat detection, and incident response. Based on the design established by Lockheed Martin's Laika BOSS and similar projects (see: related projects), Strelka's purpose is to perform file extraction and metadata collection at huge scale.

:ref:`zeek` extracts files from network traffic to ``/nsm/zeek/extracted/complete/``. Strelka then analyzes those files and they end up in ``/nsm/strelka/processed/``.

You can find Strelka logs in :ref:`hunt` and :ref:`kibana`. Here's an example of Strelka logs in :ref:`hunt`:

.. image:: https://user-images.githubusercontent.com/1659467/95659529-b11f1d80-0aef-11eb-91d3-f700d6ee5314.png
  :target: https://user-images.githubusercontent.com/1659467/95659529-b11f1d80-0aef-11eb-91d3-f700d6ee5314.png

Configuration
-------------
Strelka reads its configuration from ``/opt/so/conf/strelka/``. However, please keep in mind that if you make any changes to this directory they may be overwritten since the configuration is managed with :ref:`salt`.

More Information
----------------

.. seealso::

    For more information about Strelka, please see https://github.com/target/strelka.
