.. _pcap:

PCAP
====

:ref:`soc` gives you access to our new PCAP interface. This interface allows you to access your full packet capture. You can pivot to PCAP from :ref:`hunt` or from :ref:`kibana`. Alernatively, you can go directly to the PCAP interface and then put in your search criteria to search for a particular stream. 

.. image:: https://user-images.githubusercontent.com/1659467/87230100-5a346b80-c37b-11ea-8c72-71c1c2234261.png
  :target: https://user-images.githubusercontent.com/1659467/87230100-5a346b80-c37b-11ea-8c72-71c1c2234261.png

Once :ref:`soc` has located the stream, it will show a high level overview of the packets.

.. image:: https://user-images.githubusercontent.com/1659467/87229786-25bfb000-c379-11ea-8121-890bca6b889f.png
  :target: https://user-images.githubusercontent.com/1659467/87229786-25bfb000-c379-11ea-8121-890bca6b889f.png

If there are many packets in the stream, you can use the ``LOAD MORE`` button, ``Rows per page`` setting, and arrows to navigate through the list of packets. 

You can drill into individual rows to see the actual payload data. There are buttons at the top of the table that control what data is displayed in the individual rows. By enabling ``Show all packet data`` and disabling ``HEX``, we can get an ASCII transcript.

.. image:: https://user-images.githubusercontent.com/1659467/87229921-391f4b00-c37a-11ea-834c-8454cb047a03.png
  :target: https://user-images.githubusercontent.com/1659467/87229921-391f4b00-c37a-11ea-834c-8454cb047a03.png

Finally, you can also download the pcap by clicking the button on the right side of the table header.
