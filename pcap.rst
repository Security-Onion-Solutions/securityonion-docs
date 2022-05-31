.. _pcap:

PCAP
====

:ref:`soc` gives you access to our PCAP interface. This interface allows you to access your full packet capture that was recorded by :ref:`stenographer`. 

In most cases, you'll pivot to PCAP from a particular event in :ref:`alerts`, :ref:`dashboards`, or :ref:`hunt` by choosing the PCAP action on the action menu. 

.. image:: images/soc-events-table.png
  :target: _images/soc-events-table.png

Alternatively, you can go directly to the PCAP interface and then put in your search criteria to search for a particular stream. 

.. image:: images/pcap-add-job.png
  :target: _images/pcap-add-job.png

Security Onion will then locate the stream and render a high level overview of the packets.

.. image:: images/pcap.png
  :target: _images/pcap.png

If there are many packets in the stream, you can use the ``LOAD MORE`` button, ``Rows per page`` setting, and arrows to navigate through the list of packets. 

You can drill into individual rows to see the actual payload data. There are buttons at the top of the table that control what data is displayed in the individual rows. By disabling ``Show all packet data`` and ``HEX``, we can get an ASCII transcript.

.. image:: images/pcap-transcript.png
  :target: _images/pcap-transcript.png

You can select text with your mouse and then use the context menu to send that selected text to :ref:`cyberchef`, Google, or other destinations defined in the actions list.

.. image:: images/pcap-select-pivot.png
  :target: _images/pcap-select-pivot.png

You can send all of the visible packet data to :ref:`cyberchef` by clicking the CyberChef icon on the right side of the table header. Please note that this only sends packet data that is currently being displayed, so if you are looking at a large stream you may need to use the ``LOAD MORE`` button to display all packets in the stream.

.. image:: images/pcap-cyberchef.png
  :target: _images/pcap-cyberchef.png

Finally, you can download the full pcap file by clicking the download button on the far right side of the table header. If you are using an :ref:`analyst-vm`, then the pcap will automatically open in :ref:`networkminer`. Alternatively, you could open the pcap in :ref:`wireshark`.

.. image:: images/pcap-download.png
  :target: _images/pcap-download.png

Once you've viewed one or more PCAPs, you will see them listed on the main PCAP page.

.. image:: images/pcap-jobs.png
  :target: _images/pcap-jobs.png

When you are done with a PCAP, you may want to delete it using the ``X`` button on the far right. This deletes the cached PCAP file saved at ``/nsm/soc/jobs/``.
