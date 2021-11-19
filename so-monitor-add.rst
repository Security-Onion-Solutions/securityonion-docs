.. _so-monitor-add:

so-monitor-add
==============

If you've already run through Setup but later find that you need to add a new monitor (sniffing) interface, you can run ``so-monitor-add``. This will allow you to add network interfaces to ``bond0`` so that their traffic is monitored.

.. warning::

  Cloud images sniff directly from network interfaces rather than using ``bond0`` so this utility won't work in those environments.
