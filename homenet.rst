.. _homenet:

Homenet
=======

The homenet variable defines the networks that are considered home networks (those networks that you are monitoring and defending). It is used for :ref:`suricata` and for :ref:`zeek` as well. The default value is RFC1918 private address space:

.. image:: images/19_setup_homenet.png
  :target: _images/19_setup_homenet.png

Configuration
-------------

You can configure Suricata's HOME_NET value by going to :ref:`administration` --> Configuration --> suricata --> config --> vars --> address-groups --> HOME_NET.

You can configure Zeek's HOME_NET value by going to :ref:`administration` --> Configuration --> zeek --> config --> networks --> HOME_NET.
