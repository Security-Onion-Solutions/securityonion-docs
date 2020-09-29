.. _alerts:

Alerts
======

:ref:`soc` gives you access to our new Alerts interface. This interface allows you to quickly get an overview of the alerts that Security Onion is generating and quickly drill down into details, pivot to :ref:`pcap` or :ref:`hunt`, and escalate alerts to :ref:`hive`.

Toggles
-------

The top of the page has toggles for ``Acknowledged`` and ``Escalated``. Enabling the ``Acknowledged`` toggle will only show alerts that have previously been acknowledged by an analyst. Enabling the ``Escalated`` toggle will only show alerts that have previously been escalated by an analyst.

.. image:: 
  :target: 


Query Bar
---------
The query bar defaults to ``Group By Name, Module`` which groups the alerts by ``rule.name`` and ``event.module``. You can click the dropdown box to select other queries which will group by other fields.

.. image:: 
  :target: 

Time Picker
-----------

By default, Alerts searches the last 24 hours. If you want to search a different time frame, you can change it in the upper right corner of the screen. You can use the default relative time or click the clock icon to change to absolute time.

.. image:: 
  :target: 

Data Table
----------

The remainder of the page is a data table that starts in the grouped view and can be switched to the default view. The data table has some basic functionality regardless of which view you are looking at. Clicking the table headers allows you to sort ascending or descending. Clicking the bell icon acknowledges an alert. That alert can then be seen by select the ``Acknowledged`` toggle at the top of the page.

Clicking a value in the table brings up a menu of actions for that value. The plus and minus magnifying glass icons to the left allow you to include or exclude (respectively) those values in your query. If present, the down arrow icon allows you to drill into that value (more on that in the next section). The fourth icon allows to add that particular field as a groupby in the query. The fourth icon starts a new search for the value in :ref:`hunt`. The ``G`` and ``VT`` on the right end of the actions menu look up the value at Google and VirusTotal (respectively).

You can adjust the ``Rows per page`` setting in the bottom right and use the left and right arrow icons to page through the table.

Grouped View
------------

By default, alerts are grouped by whatever criteria is selected in the query bar. Clicking a field value and then clicking the down arrow icon allows you to drilldown into that value which switches to the detailed view.

.. image:: 
  :target: 

Detailed View
-------------

If you click a value in the grouped view and then click the down arrow icon on the quick bar, it will drill down to the detailed view. This is a data table that contains all search results and allows you to then drill into individual search results as necessary. Clicking the table headers allows you to sort ascending or descending. Starting from the left side of each row, there is an arrow which will expand the result to show all of its fields. To the right of that arrow is the ``Timestamp`` field. Next, a few standard fields are shown: ``source.ip``, ``source.port``, ``destination.ip``, ``destination.port``, ``log.id.uid`` (Zeek unique identifier), ``network.community_id`` (Community ID), and ``event.dataset``. Depending on what kind of data you're looking at, there may be some additional data-specific fields as well. 

.. image:: 
  :target: 

When you click the down arrow to expand a row in the Events table, it will show all of the individual fields from that event. Field names are shown on the left and field values on the right. When looking at the field names, there is an icon to the left that will add that field to the ``groupby`` section of your query. You can click on values on the right to bring up the action menu to refine your search or pivot to other pages. 

.. image:: 
  :target: 
