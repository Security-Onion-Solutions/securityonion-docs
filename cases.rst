.. _cases:

Cases
=====

Starting in Security Onion 2.3.100, we have a new Cases interface for case management. It allows you to manage your cases from start to finish including escalating logs from Alerts and Hunts, assigning analysts, commenting, adding attachments, and tracking observables.

.. image:: images/cases.png
  :target: _images/cases.png

Options
-------

Starting at the top of the main Cases page, the Options drop-down menu allows you to set options such as Automatic Refresh Interval and Time Zone.

New Case
--------

To create a new case, click the + icon and then fill out the Title and Description and optionally the fields on the right side:

.. image:: images/cases-add.png
  :target: _images/cases-add.png

Escalating Events
-----------------

If you find events of interest in :ref:`alerts` or :ref:`hunt`, you can click the blue escalate button to escalate to a new case or an existing case:

.. image:: images/cases-escalate.png
  :target: _images/cases-escalate.png

Comments
--------

On the Comments tab, you can add comments about the case. The Comments field uses Github flavored markdown.

.. image:: images/cases-comments.png
  :target: _images/cases-comments.png

Attachments
-----------

On the Attachments tab, you can upload attachments. 

.. image:: images/cases-attachments.png
  :target: _images/cases-attachments.png

Observables
-----------

On the Observables tab, you can track observables like IP addresses, domain names, hashes, etc.

.. image:: images/cases-observables.png
  :target: _images/cases-observables.png

Events
------

On the Events tab, you can see any events that have been escalated to the case.

.. image:: images/cases-events.png
  :target: _images/cases-events.png

History
-------

On the History tab, you can see the history of the case itself, including any changes made by each user.

.. image:: images/cases-history.png
  :target: _images/cases-history.png

Query Bar
---------

Once you have one or more cases, you can use the main Cases page to get an overview of all cases. The query bar defaults to Open Cases. Clicking the dropdown box reveals other options such as Closed Cases and Templates. If you want to send your current query to Hunt, you can click the crosshair icon to the right of the query bar.

Under the query bar, you’ll notice colored bubbles that represent the individual components of the query and the fields to group by. If you want to remove part of the query, you can click the X in the corresponding bubble to remove it and run a new search.

Time Picker
-----------

The time picker is to the right of the query bar. By default, Cases searches the last 12 months. If you want to search a different time frame, you can change it here.

Data Table
----------

The remainder of the main Cases page is a data table that shows a high level overview of the cases matching the current search criteria.

- Clicking the table headers allows you to sort ascending or descending.

- Clicking a value in the table brings up a context menu of actions for that value. This allows you to refine your existing search, start a new search, or even pivot to external sites like Google and VirusTotal.

- You can adjust the Rows per page setting in the bottom right and use the left and right arrow icons to page through the table.

- You can drill into a case by clicking the binoculaurs icon. This detail view shows you more information about the case including Comments, Attachments, Observables, Events, and History.
