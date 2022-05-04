.. _hunt:

Hunt
====

:ref:`soc` gives you access to our Hunt interface. This interface allows you to hunt through all of the data in :ref:`elasticsearch` and is highly tuned for stacking, pivoting, data expansion, and data reduction.

.. image:: images/hunt.png
  :target: _images/hunt.png

There is an Options drop-down menu that allows you to set options such as Auto Hunt, Exclude case data, Automatic Refresh Interval, and Time Zone.

Auto Hunt
---------

The Auto Hunt option defaults to enabled:

.. image:: https://user-images.githubusercontent.com/1659467/94722720-af05d380-0325-11eb-9139-ce49c3a549cf.png
  :target: https://user-images.githubusercontent.com/1659467/94722720-af05d380-0325-11eb-9139-ce49c3a549cf.png

When enabled, Hunt will automatically submit your query any time you change filters, groupings, or date ranges.

Exclude case data
-----------------

Hunt excludes :ref:`cases` data by default:

.. image:: images/soc-exclude-case-data.png
  :target: _images/soc-exclude-case-data.png

If you disable this option, then you can use Hunt to query your :ref:`cases` data.

Automatic Refresh Interval
--------------------------

The Automatic Refresh Interval setting will automatically refresh your query at the time interval you select:

.. image:: images/soc-automatic-refresh-interval.png
  :target: _images/soc-automatic-refresh-interval.png

Time Zone
---------

Hunt will try to detect your local time zone via your browser. You can manually specify your time zone if necessary.

Query Bar
---------
The easiest way to get started is to click the query drop down box and select one of the pre-defined queries. These pre-defined queries cover most of the major data types that you would expect to see in a Security Onion deployment: NIDS alerts from :ref:`suricata`, HIDS alerts from :ref:`wazuh`, protocol metadata logs from :ref:`zeek` or :ref:`suricata`, endpoint logs, and firewall logs. Each of the entries in the drop down list will show the actual query followed by a description of what that query does.

.. image:: https://user-images.githubusercontent.com/1659467/94723168-5256e880-0326-11eb-8952-37804962d526.png
  :target: https://user-images.githubusercontent.com/1659467/94723168-5256e880-0326-11eb-8952-37804962d526.png

Time Picker
-----------

By default, Hunt searches the last 24 hours. If you want to search a different time frame, you can change it in the upper right corner of the screen. You can use the default relative time or click the clock icon to change to absolute time.

.. image:: https://user-images.githubusercontent.com/1659467/94723208-64388b80-0326-11eb-959b-5ecfcd51fb9c.png
  :target: https://user-images.githubusercontent.com/1659467/94723208-64388b80-0326-11eb-959b-5ecfcd51fb9c.png

Visualization
-------------

The first section of output contains a Most Occurrences visualization, a timeline visualization, and a Fewest Occurrences visualization. Bar charts are clickable, so you can click a value to update your search criteria. Aggregation defaults to 10 values, so Most Occurrences is the Top 10 and Fewest Occurrences is the Bottom 10 (long tail). The number of aggregation values is controlled by the Fetch Limit setting in the Group Metrics section.

.. image:: https://user-images.githubusercontent.com/1659467/94723255-74506b00-0326-11eb-872f-9229e8efd9ac.png
  :target: https://user-images.githubusercontent.com/1659467/94723255-74506b00-0326-11eb-872f-9229e8efd9ac.png

Group Metrics
-------------

The middle section of output is the Group Metrics section and it's a data table that allows you to stack (aggregate) arbitrary fields. Group metrics are controlled by the ``groupby`` parameter in the search bar. Clicking the table headers allows you to sort ascending or descending. 

Clicking a value in the Group Metrics table brings up a context menu of actions for that value. This allows you to refine your existing search, start a new search, or even pivot to external sites like Google and VirusTotal.

The default Fetch Limit for the Group Metrics table is ``10``. If you need to see more than the top 10, you can increase the Fetch Limit and then page through the output using the left and right arrow icons or increase the ``Rows per page`` setting.

.. image:: images/hunt-group-metrics.png
  :target: _images/hunt-group-metrics.png

Events
------

The third and final section of output is a data table that contains all search results and allows you to drill into individual search results as necessary. Clicking the table headers allows you to sort ascending or descending. Starting from the left side of each row, there is an arrow which will expand the result to show all of its fields. To the right of that arrow is the ``Timestamp`` field. Next, a few standard fields are shown: ``source.ip``, ``source.port``, ``destination.ip``, ``destination.port``, ``log.id.uid`` (Zeek unique identifier), ``network.community_id`` (Community ID), and ``event.dataset``. Depending on what kind of data you're looking at, there may be some additional data-specific fields as well. 

Clicking a value in the Events table brings up a context menu of actions for that value. This allows you to refine your existing search, start a new search, or even pivot to external sites like Google and VirusTotal.

The default Fetch Limit for the Events table is ``100``. If you need to see more than 100 events, you can increase the Fetch Limit and then page through the output using the left and right arrow icons or increase the ``Rows per page`` setting.

.. image:: images/hunt-events.png
  :target: _images/hunt-events.png

When you click the arrow to expand a row in the Events table, it will show all of the individual fields from that event. Field names are shown on the left and field values on the right. When looking at the field names, there is an icon to the left that will add that field to the ``groupby`` section of your query. You can click on values on the right to bring up the context menu to refine your search or pivot to other pages. 

.. image:: images/hunt-expanded.png
  :target: _images/hunt-expanded.png

Statistics
----------

The bottom left corner of the page shows statistics about the current query including the speed of the backend data fetch and the total round trip time.

.. image:: https://user-images.githubusercontent.com/1659467/92963000-ca28a600-f43f-11ea-99ff-9a69604b03d0.png
  :target: https://user-images.githubusercontent.com/1659467/92963000-ca28a600-f43f-11ea-99ff-9a69604b03d0.png

Context Menu
------------

Clicking a value in the page brings up a context menu that allows you to refine your existing search, start a new search, or even pivot to external sites like Google and VirusTotal. 

Include
~~~~~~~

Clicking the ``Include`` option will add the selected value to your existing search to only show search results that include that value.

Exclude
~~~~~~~

Clicking the ``Exclude`` option will exclude the selected value from your existing search results.

Only
~~~~

Clicking the ``Only`` option will start a new search for the selected value and retain any existing groupby terms.

Group By
~~~~~~~~

Clicking the ``Group By`` option will update the existing query and aggregate the results based on the selected field.

Clipboard
~~~~~~~~~

The ``Clipboard`` sub-menu has several options that allow you to copy selected data to your clipboard in different ways.

Actions
~~~~~~~

The ``Actions`` sub-menu has several different options:

- Clicking the ``Hunt`` option will start a new search for the selected value and will aggregate the results by ``event.module`` and ``event.dataset`` to give you a good overview of what types of data are available for that indicator.

- Clicking the ``Correlate`` option will find related logs based on Community ID, uid, fuid, etc.

- Clicking the ``PCAP`` option will pivot to the :ref:`pcap` interface to retrieve full packet capture for the selected stream.

- Clicking the ``Google`` option will search Google for the selected value.

- Clicking the ``VirusTotal`` option will search VirusTotal for the selected value.

If you'd like to add your own custom actions, see the :ref:`soc-customization` section.

OQL
---

Onion Query Language (OQL) starts with standard `Lucene query syntax <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_ and then allows you to add optional segments that control what Hunt does with the results from the query. 

sortby
~~~~~~

Starting in Security Onion 2.3.100, the ``sortby`` segment can be added to the end of a hunt query. This can help ensure that you see the most recent data, for example, when sorting by descending timestamp. Otherwise, if the search yields a dataset larger than the X Limit size selected in the UI then you will only get the first X records and then those will be sorted on the web browser.

You can specify one field to sort by or multiple fields separated by spaces. The default order is descending but if you want to force the sort order to be ascending you can add the optional caret (^) symbol to the end of the field name.

::

  | sortby some.field another.field^

groupby
~~~~~~~

The ``groupby`` segment tells Hunt to group by (aggregate) a particular field. So, for example, if you want to group by destination IP address, you can add ``| groupby destination.ip`` to your search (assuming it didn't already have a groupby statement). The ``groupby`` segment supports multiple aggregations so you can add more fields that you want to group by, separating those fields with spaces. For example, to group by destination IP address and then destination port, you could use ``| groupby destination.ip destination.port``.

By default, grouping by a particular field won't show any values if that field is missing. If you would like to include missing values, you can add an asterisk after the field name. For example, you might have some non-HTTP traffic on port 80 that wouldn't be shown by the following query grouping by ``network.protocol``:

.. image:: images/hunt-groupby-default.png
  :target: _images/hunt-groupby-default.png

However, if you add an asterisk after the ``network.protocol`` field name, Hunt will show missing values which in this case will help you see the non-HTTP traffic on port 80:

.. image:: images/hunt-groupby-asterisk.png
  :target: _images/hunt-groupby-asterisk.png

Please note that adding the asterisk to a non-string field may not work as expected. As an alternative, you may be able to use the asterisk with the equivalent ``keyword`` field if it is available. For example, ``source.geo.ip*`` may return 0 results, or a query failure error, but ``source.geo.ip.keyword*`` may work as expected.
