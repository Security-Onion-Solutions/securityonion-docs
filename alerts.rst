.. _alerts:

Alerts
======

:ref:`soc` includes an Alerts interface which gives you an overview of the alerts that Security Onion is generating. You can then quickly drill down into details, pivot to :ref:`hunt` or the :ref:`pcap` interface, and escalate alerts to :ref:`cases`.

.. image:: images/50_alerts.png
  :target: _images/50_alerts.png
  
Options
-------

At the top of the page, there is an Options menu that allows you to set several different options for the Alerts page.

.. image:: images/52_alerts_options.png
  :target: _images/52_alerts_options.png
  
Toggles
~~~~~~~

The first toggle is labeled ``Enable advanced interface features``. If you enable this option, then the interface will show more advanced features similar to :ref:`dashboards` and :ref:`hunt`. This includes an extra toggle labeled ``Automatically apply filters, groupings, and date ranges``.

Enabling the ``Acknowledged`` toggle will only show alerts that have previously been acknowledged by an analyst. 

Enabling the ``Escalated`` toggle will only show alerts that have previously been escalated by an analyst to :ref:`cases`.

Finally, the ``Show Details Panel`` toggle controls the Details panel on the right side. For more information, see the Details Panel section below.

Automatic Refresh Interval
~~~~~~~~~~~~~~~~~~~~~~~~~~

Another option is the Automatic Refresh Interval setting. When enabled, the Alerts page will automatically refresh at the time interval you select.

Time Zone
~~~~~~~~~

Alerts will try to detect your local time zone via your browser. You can manually specify your time zone if necessary.

Query Bar
---------

The query bar defaults to ``Group By Name, Module`` which groups the alerts by ``rule.name`` and ``event.module``. You can click the dropdown box to select other queries which will group by other fields.

On the right side of the query bar is a hunt button that will start a new hunt based on the current query.

If you would like to save your own personal queries, you can bookmark them in your browser. If you would like to customize the default queries for all users, please see the :ref:`soc-customization` section.

Time Picker
-----------

By default, Alerts searches the last 24 hours. If you want to search a different time frame, you can change it in the upper-right corner of the screen.

Details Panel
-------------

The details panel on the right side shows details for the currently selected alert. This includes an AI summary (if available) and options for tuning the rule that generated the alert. This functionality is part of :ref:`detections` so you can read more in that section. This panel can be disabled under the Options dropdown (see above).

Data Table
----------

The remainder of the page is a data table that starts in the grouped view and can be switched to the detailed view. Both views have some functionality in common:

- Clicking the table headers allows you to sort ascending or descending. 

- Starting from the left side of each row, there is an arrow which will expand the row to show more details.

- To the right of that arrow is a bell icon that acknowledges the alert. That alert can then be seen by selecting the ``Acknowledged`` toggle at the top of the page. In the ``Acknowledged`` view, clicking the bell icon removes the acknowledgement.

- To the right of that is a blue exclamation icon that escalates the alert to :ref:`cases` and allows you to create a new case or add to an existing case. If you need to find that original escalated alert in the Alerts page, you can enable the ``Escalated`` toggle (which will automatically enable the ``Acknowledged`` toggle as well).

- To the right of that is an information icon that populates the Details Panel on the right with information about the alert.

- Security Onion Pro users will find one more button. The last is a computer chip icon that investigates the alert with :ref:`onionai`.

- Clicking a value in the table brings up a context menu of actions for that value. This allows you to refine your existing search, start a new search, or even pivot to external sites like Google and VirusTotal.

- You can adjust the ``Rows per page`` setting in the bottom right and use the left and right arrow icons to page through the table.

.. note::

   If you are in the grouped view and looking at an alert that has multiple instances (the Count column is greater than 1) and you then click the arrow to expand the alert, it will show you the details for the most recent instance of that alert. If you need to see details for the other instances of the alert, then you will need to switch from the grouped view to the detailed view.

Guided Analysis
~~~~~~~~~~~~~~~

When you click the arrow to expand the alert, it starts on the ``ALERT DETAILS`` tab but you can switch to the ``GUIDED ANALYSIS`` tab which leverages Playbooks to show you plays associated with the alert. These plays include questions which help guide your investigation. You can expand all questions at once using the maximize button on the right side of the ``GUIDED ANALYSIS`` tab. 

Each question has an associated query and the results of that query will be displayed to help you answer the question. A maximum of 5 query results will be displayed but if you want to see more, then you can click the crosshairs icon to open the query in :ref:`hunt`. This also allows you to tweak the query if necessary. If you don't get any results, you could try changing the date range or other query parameters. In some cases, the query may be looking for data that you don't currently collect. For example, the query may be looking for endpoint data and so you may need to deploy the :ref:`elastic-agent` to start collecting this information.

.. note::

   To see Guided Analysis in action, check out our sneak peek video at https://youtu.be/SLGRB3PxB-o.

For more information about Playbooks, please see the :ref:`detections` section.

.. warning::

   Guided Analysis is a new experimental feature. Some of these playbooks were generated by AI and it's possible that they may not be 100% accurate. Please let us know if you see any issues.

.. image:: images/51_alerts_play.png
  :target: _images/51_alerts_play.png

Grouped View
~~~~~~~~~~~~

By default, alerts are grouped by whatever criteria is selected in the query bar. Clicking a field value and then selecting the Drilldown option allows you to drill down into that value which switches to the detailed view. You can also click the value in the Count column to perform a quick drilldown. Note that this quick drilldown feature is only enabled for certain queries.

If you'd like to remove a particular field from the grouped view, you can click the trash icon at the top of the table to the right of the field name.

Detailed View
~~~~~~~~~~~~~

If you click a value in the grouped view and then select the Drilldown option, the display will switch to the detailed view. This shows all search results and allows you to then drill into individual search results as necessary. Clicking the table headers allows you to sort ascending or descending. Starting from the left side of each row, there is an arrow which will expand the result to show all of its fields. To the right of that arrow is the ``Timestamp`` field. Next, a few standard fields are shown: ``rule.name``, ``event.severity_label``, ``source.ip``, ``source.port``, ``destination.ip``, and ``destination.port``. Depending on what kind of data you're looking at, there may be some additional data-specific fields as well. 

When you click the arrow to expand a row in the Events table, it will show all of the individual fields from that event. Field names are shown on the left and field values on the right. When looking at the field names, there are two icons to the left. The Groupby icon, the left most icon, will add a new groupby table for that field. The Toggle Column icon, to the right of the Groupby icon, will toggle that column in the Events table, and the icon will be a blue color if the column is visible. You can click on values on the right to bring up the context menu to refine your search or pivot to other pages. 

Context Menu
------------

Clicking a value in the page brings up a context menu that allows you to refine your existing search, start a new search, or even pivot to external sites like Google and VirusTotal. 

Include
~~~~~~~

Clicking the ``Include`` option will add the selected field:value pair to your existing search with an ``AND``. This will only show search results that include that value in that field.

Exclude
~~~~~~~

Clicking the ``Exclude`` option will add the selected field:value pair to your existing search with an ``AND NOT``. This will only show search results that do not include that value in that field.

Only
~~~~

Clicking the ``Only`` option will start a new search for the selected value in any field. It will remove any existing filters but retain any existing groupby terms.

Drilldown
~~~~~~~~~

Clicking the ``Drilldown`` option will drill down into a group of alerts to show each individual alert.

Tune Detection
~~~~~~~~~~~~~~

Clicking the ``Tune Detection`` option will take you to :ref:`detections` and allow you disable or modify the detection that fired the alert.

Group By
~~~~~~~~

Clicking the ``Group By`` option will update the existing query and aggregate the results based on the selected field.

New Group By
~~~~~~~~~~~~

Clicking the ``New Group By`` option will create a new data table for the selected field.

Numeric Ops
~~~~~~~~~~~

If the value you clicked is numeric, then the ``Numeric Ops`` sub-menu allows you to choose operations like less than, less than or equal, greater than, greater than or equal, or Between. Choosing the Between option displays a window so that you can specify a range of values.

Clipboard
~~~~~~~~~

The ``Clipboard`` sub-menu has several options that allow you to copy selected data to your clipboard in different ways.

Actions
~~~~~~~

The ``Actions`` sub-menu has several different options. Please note that some of these actions will only display on the Actions menu if you click on a specific log type.

- Clicking the ``Hunt`` option will start a new search for the selected value and will give you a good overview of what types of data are available for that indicator.

- Clicking the ``Add to Case`` option will add an observable to a new or existing case.

- Clicking the ``Correlate`` option will find related logs based on Community ID, uid, fuid, etc.

- Clicking the ``PCAP`` option will pivot to the :ref:`pcap` interface to retrieve full packet capture for the selected stream. This option will only appear if you click on a log that contains source IP, source port, destination IP, destination port, etc.

- Clicking the ``Google`` option will search Google for the selected value. 

- Clicking the ``VirusTotal`` option will search VirusTotal for the selected value.

- Clicking the ``Process Info`` option will show all logs that include this process's entity_id in the ``process.entity_id`` field. This option will only appear if you click on a log that contains the ``process.entity_id`` field.

- Clicking the ``Process and Child Info`` option will show all logs that include this process's entity_id in either the ``process.entity_id`` or ``process.parent.entity_id`` fields. Depending on the process, this may show the same logs as the ``Process Info`` option or it may show more. This option will only appear if you click on a log that contains the ``process.entity_id`` field.

- Clicking the ``Process All Info`` option will show all logs that include this process's entity_id in any field. Depending on the process, this may show the same logs as the ``Process and Child Info`` option or it may show more. This option will only appear if you click on a log that contains the ``process.entity_id`` field.

- Clicking the ``Process Ancestors`` option will show all parent processes for the selected process. This option will only appear if you click on a log that contains the ``process.Ext.ancestry`` field.

If you'd like to add your own custom actions, see the :ref:`soc-customization` section.
