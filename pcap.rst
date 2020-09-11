.. _pcap:

PCAP
====

:ref:`soc` gives you access to our new PCAP interface. This interface allows you to access your full packet capture. You can pivot to PCAP from :ref:`hunt` or from :ref:`kibana`. Alternatively, you can go directly to the PCAP interface and then put in your search criteria to search for a particular stream. 

.. image:: https://user-images.githubusercontent.com/1659467/92967744-cb5dd100-f447-11ea-9621-4c477d6a7e3a.png
  :target: https://user-images.githubusercontent.com/1659467/92967744-cb5dd100-f447-11ea-9621-4c477d6a7e3a.png

Once :ref:`soc` has located the stream, it will show a high level overview of the packets.

.. image:: https://user-images.githubusercontent.com/1659467/92967522-6a35fd80-f447-11ea-8fbd-27c0bd952704.png
  :target: https://user-images.githubusercontent.com/1659467/92967522-6a35fd80-f447-11ea-8fbd-27c0bd952704.png

If there are many packets in the stream, you can use the ``LOAD MORE`` button, ``Rows per page`` setting, and arrows to navigate through the list of packets. 

You can drill into individual rows to see the actual payload data. There are buttons at the top of the table that control what data is displayed in the individual rows. By disabling ``Show all packet data`` and ``HEX``, we can get an ASCII transcript.

.. image:: https://user-images.githubusercontent.com/1659467/92967656-a49f9a80-f447-11ea-9923-e0beaf39487d.png
  :target: https://user-images.githubusercontent.com/1659467/92967656-a49f9a80-f447-11ea-9923-e0beaf39487d.png

Finally, you can also download the pcap by clicking the button on the right side of the table header.
