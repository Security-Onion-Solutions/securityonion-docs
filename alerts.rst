.. _alerts:

Alerts
======

:ref:`soc` gives you access to our new Alerts interface. This interface gives you an overview of the alerts that Security Onion is generating and allows you to quickly drill down into details, pivot to :ref:`hunt` or :ref:`pcap`, and escalate alerts to :ref:`hive`.

.. image:: https://user-images.githubusercontent.com/1659467/94826485-5aba2c80-03d5-11eb-8ad8-1a36c18a742e.png
  :target: https://user-images.githubusercontent.com/1659467/94826485-5aba2c80-03d5-11eb-8ad8-1a36c18a742e.png
  
Toggles
-------

The top of the page has toggles for ``Acknowledged`` and ``Escalated``:

.. image:: https://user-images.githubusercontent.com/1659467/94587683-ed7d8e80-0250-11eb-951d-282ba76932f7.png
  :target: https://user-images.githubusercontent.com/1659467/94587683-ed7d8e80-0250-11eb-951d-282ba76932f7.png

- Enabling the ``Acknowledged`` toggle will only show alerts that have previously been acknowledged by an analyst. 

- Enabling the ``Escalated`` toggle will only show alerts that have previously been escalated by an analyst to :ref:`hive`.

Query Bar
---------
The query bar defaults to ``Group By Name, Module`` which groups the alerts by ``rule.name`` and ``event.module``. If you want to send your current Alerts query to :ref:`hunt`, you can click the crosshair icon to the right of the query bar.

.. image:: https://user-images.githubusercontent.com/1659467/94826741-a076f500-03d5-11eb-82f9-413a0ba79797.png
  :target: https://user-images.githubusercontent.com/1659467/94826741-a076f500-03d5-11eb-82f9-413a0ba79797.png

Under the query bar, you'll notice colored bubbles that represent the individual components of the query and the fields to group by. If you want to remove part of the query, you can click its corresponding bubble to remove it and run a new search.

You can click the dropdown box to select other queries which will group by other fields.

.. image:: https://user-images.githubusercontent.com/1659467/94826842-bc7a9680-03d5-11eb-829b-4940403859f5.png
  :target: https://user-images.githubusercontent.com/1659467/94826842-bc7a9680-03d5-11eb-829b-4940403859f5.png
  
Time Picker
-----------

By default, Alerts searches the last 24 hours. If you want to search a different time frame, you can change it in the upper right corner of the screen.

.. image:: https://user-images.githubusercontent.com/1659467/94587826-20c01d80-0251-11eb-8fa3-2e73a0763981.png
  :target: https://user-images.githubusercontent.com/1659467/94587826-20c01d80-0251-11eb-8fa3-2e73a0763981.png

Data Table
----------

The remainder of the page is a data table that starts in the grouped view and can be switched to the detailed view. Both views have some functionality in common:

- Clicking the table headers allows you to sort ascending or descending. 

- Clicking the bell icon acknowledges an alert. That alert can then be seen by selecting the ``Acknowledged`` toggle at the top of the page. In the ``Acknowledged`` view, clicking the bell icon removes the acknowledgement.

- Clicking the exclamation icon escalates the alert to :ref:`hive` and creates a case. The case can then be seen in :ref:`hive` interface.

- Clicking a value in the table brings up a menu of actions for that value. The plus and minus magnifying glass icons to the left allow you to include or exclude (respectively) those values in your query. If present, the down arrow icon allows you to drill into that value (more on that in the next section). The groupby icon allows to add that particular field as a groupby in the query. The crosshair icon starts a new search for the value in :ref:`hunt`. The ``G`` and ``VT`` on the right end of the actions menu look up the value at Google and VirusTotal (respectively).

- You can adjust the ``Rows per page`` setting in the bottom right and use the left and right arrow icons to page through the table.

Grouped View
~~~~~~~~~~~~

By default, alerts are grouped by whatever criteria is selected in the query bar. Clicking a field value and then clicking the down arrow icon allows you to drilldown into that value which switches to the detailed view.

.. image:: https://user-images.githubusercontent.com/1659467/94826933-d87e3800-03d5-11eb-99a7-388658bfdf36.png
  :target: https://user-images.githubusercontent.com/1659467/94826933-d87e3800-03d5-11eb-99a7-388658bfdf36.png

Detailed View
~~~~~~~~~~~~~

If you click a value in the grouped view and then click the down arrow icon on the quick bar, it will drill down to the detailed view. This shows all search results and allows you to then drill into individual search results as necessary. Clicking the table headers allows you to sort ascending or descending. Starting from the left side of each row, there is an arrow which will expand the result to show all of its fields. To the right of that arrow is the ``Timestamp`` field. Next, a few standard fields are shown: ``source.ip``, ``source.port``, ``destination.ip``, ``destination.port``, ``log.id.uid`` (Zeek unique identifier), ``network.community_id`` (Community ID), and ``event.dataset``. Depending on what kind of data you're looking at, there may be some additional data-specific fields as well. 

.. image:: https://user-images.githubusercontent.com/1659467/94827102-0bc0c700-03d6-11eb-9957-001568c442cd.png
  :target: https://user-images.githubusercontent.com/1659467/94827102-0bc0c700-03d6-11eb-9957-001568c442cd.png

When you click the down arrow to expand a row in the Events table, it will show all of the individual fields from that event. Field names are shown on the left and field values on the right. When looking at the field names, there is an icon to the left that will add that field to the ``groupby`` section of your query. You can click on values on the right to bring up the action menu to refine your search or pivot to other pages. 

.. image:: https://user-images.githubusercontent.com/1659467/94827209-28f59580-03d6-11eb-88fd-16f1cc2be788.png
  :target: https://user-images.githubusercontent.com/1659467/94827209-28f59580-03d6-11eb-88fd-16f1cc2be788.png
