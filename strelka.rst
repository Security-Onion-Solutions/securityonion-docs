.. _strelka:

Strelka
=======

From https://github.com/target/strelka:

    Strelka is a real-time file scanning system used for threat hunting, threat detection, and incident response. Based on the design established by Lockheed Martin's Laika BOSS and similar projects (see: related projects), Strelka's purpose is to perform file extraction and metadata collection at huge scale.

:ref:`zeek` extracts files from network traffic to ``/nsm/zeek/extracted/complete/``. Strelka then analyzes those files and they end up in ``/nsm/strelka/processed/``.

Configuration
-------------
Strelka configuration can be found at ``/opt/so/conf/strelka/``.

More Information
----------------

.. seealso::

    For more information about Strelka, please see https://github.com/target/strelka.
