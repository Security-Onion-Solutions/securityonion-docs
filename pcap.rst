.. _pcap:

PCAP
====

:ref:`soc` includes a PCAP interface which allows you to access your full packet capture that was written to disk by :ref:`stenographer` or :ref:`suricata`. 

You can access PCAP in two different ways. The first and most common option is to pivot to PCAP from a particular event in :ref:`alerts`, :ref:`dashboards`, or :ref:`hunt` by choosing the PCAP action on the action menu.

.. image:: images/soc-events-table.png
  :target: _images/soc-events-table.png

The second and less common option is to go directly to the PCAP interface, click the blue + button, and then put in your search criteria to search for a particular stream.

.. image:: images/73_jobs_add.png
  :target: _images/73_jobs_add.png

Regardless of which of these two options you choose, Security Onion should then locate the stream and render a high level overview of the packets.

.. image:: images/62_pcap.png
  :target: _images/62_pcap.png

If there are many packets in the stream, you can use the ``LOAD MORE`` button, ``Rows per page`` setting, and arrows to navigate through the list of packets. 

You can drill into individual rows to see the actual payload data. There are buttons at the top of the table that control what data is displayed in the individual rows. If you disable the ``Show all packet data`` and ``HEX`` buttons, then you get an ASCII transcript.

.. image:: images/65_pcap_details.png
  :target: _images/65_pcap_details.png

You can select text with your mouse and then use the context menu to send that selected text to :ref:`cyberchef`, Google, or other destinations defined in the actions list.

There are two buttons on the right side of the table header. The first will send all visible packet data to :ref:`cyberchef`. Please note that this only sends packet data that is currently being displayed, so if you are looking at a large stream you may need to use the ``LOAD MORE`` button to display all packets in the stream. The second button on the far right allows you to download the full pcap file. You can then open the pcap file using :ref:`networkminer`, :ref:`wireshark`, or any other standard libpcap tool. You should typically avoid doing pcap analysis on your normal desktop environment, so you may want to consider opening the pcap file in a :ref:`desktop` instance.

Once you've viewed one or more PCAPs, you will see them listed on the main PCAP page.

.. image:: images/72_jobs.png
  :target: _images/72_jobs.png

When you are done with a PCAP, you may want to delete it using the ``X`` button on the far right. This deletes the cached PCAP file saved at ``/nsm/soc/jobs/``.

Troubleshooting
---------------

If you have trouble retrieving PCAP, here are some things to check:

- Verify that full packet capture is enabled via either :ref:`stenographer` or :ref:`suricata`.
- Check to see if you have any :ref:`bpf` configuration that may cause :ref:`stenographer` or :ref:`suricata` to ignore the traffic.
- Check :ref:`grid` and verify that all services are running properly.
- Check :ref:`influxdb` and verify that PCAP Retention is long enough to include the stream you're looking for.
- Make sure that there is plenty of free space on ``/nsm`` to carve the stream and write the output to disk.
