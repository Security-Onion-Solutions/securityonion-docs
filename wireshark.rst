.. _wireshark:

Wireshark
=========

From https://www.wireshark.org/:

    Wireshark is the world’s foremost and widely-used network protocol analyzer. It lets you see what’s happening on your network at a microscopic level and is the de facto (and often de jure) standard across many commercial and non-profit enterprises, government agencies, and educational institutions. Wireshark development thrives thanks to the volunteer contributions of networking experts around the globe and is the continuation of a project started by Gerald Combs in 1998.
    
Usage
-----
Wireshark is a part of our :ref:`analyst-vm` installation.

Screenshot
----------

.. image:: images/wireshark.png
  :target: _images/wireshark.png

Example
-------

Suppose you are looking at an interesting HTTP file download in :ref:`PCAP` and want to extract the file. Click the PCAP download button and then open the pcap file with Wireshark.

.. image:: images/wireshark-png-0.png
  :target: _images/wireshark-png-0.png

To extract files from HTTP traffic, click File - Export Objects - HTTP.

.. image:: images/wireshark-png-1.png
  :target: _images/wireshark-png-1.png

Select the file(s) to save.

.. image:: images/wireshark-png-2.png
  :target: _images/wireshark-png-2.png

Specify where to save them.

.. image:: images/wireshark-png-3.png
  :target: _images/wireshark-png-3.png

Review the extracted file(s).

.. image:: images/wireshark-png-4.png
  :target: _images/wireshark-png-4.png

More Information
----------------

.. seealso::

    For more information about Wireshark, please see https://www.wireshark.org/.
