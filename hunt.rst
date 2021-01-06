.. _hunt:

Hunt
====

:ref:`soc` gives you access to our new Hunt interface. This interface allows you to hunt through all of the data in :ref:`elasticsearch` and is highly tuned for stacking, pivoting, data expansion, and data reduction.

.. image:: images/hunt.png
  :target: _images/hunt.png

Auto Hunt
---------

The top of the page has a toggle for Auto Hunt which defaults to enabled. When enabled, Hunt will automatically submit your query any time you change filters, groupings, or date ranges.

.. image:: https://user-images.githubusercontent.com/1659467/94722720-af05d380-0325-11eb-9139-ce49c3a549cf.png
  :target: https://user-images.githubusercontent.com/1659467/94722720-af05d380-0325-11eb-9139-ce49c3a549cf.png

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

The first section of output contains a Most Occurences visualization, a timeline visualization, and a Fewest Occurences visualization. Bar charts are clickable, so you can click a value to update your search criteria. Aggregation defaults to 10 values, so Most Occurences is the Top 10 and Fewest Occurences is the Bottom 10 (long tail). The number of aggregation values is controlled by the Fetch Limit setting in the Group Metrics section.

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

When you click the down arrow to expand a row in the Events table, it will show all of the individual fields from that event. Field names are shown on the left and field values on the right. When looking at the field names, there is an icon to the left that will add that field to the ``groupby`` section of your query. You can click on values on the right to bring up the context menu to refine your search or pivot to other pages. 

.. image:: images/hunt-expanded.png
  :target: _images/hunt-expanded.png

Statistics
----------

The bottom left corner of the page shows statistics about the current query including the speed of the backend data fetch and the total round trip time.

.. image:: https://user-images.githubusercontent.com/1659467/92963000-ca28a600-f43f-11ea-99ff-9a69604b03d0.png
  :target: https://user-images.githubusercontent.com/1659467/92963000-ca28a600-f43f-11ea-99ff-9a69604b03d0.png

Context Menu
------------

Clicking a value in the page brings up a context menu that allows you to refine your search, start a new search, or even pivot to external sites like Google and VirusTotal. If you'd like to add additional external sites, you can do so by copying ``/opt/so/saltstack/default/salt/soc/files/soc/hunt.actions.json`` to ``/opt/so/saltstack/local/salt/soc/files/soc/hunt.actions.json`` and then adding new entries. 

For example, suppose we want to add ``AbuseIPDB`` with URL ``https://www.abuseipdb.com/check/{value}``. First, we need to copy ``/opt/so/saltstack/default/salt/soc/files/soc/hunt.actions.json`` to ``/opt/so/saltstack/local/salt/soc/files/soc/hunt.actions.json``:

::

  sudo cp -n /opt/so/saltstack/default/salt/soc/files/soc/hunt.actions.json /opt/so/saltstack/local/salt/soc/files/soc/hunt.actions.json


Next, we need to edit ``/opt/so/saltstack/local/salt/soc/files/soc/hunt.actions.json`` using our favorite text editor and insert the following as the next to last line of the file:

::

  { "name": "AbuseIPDB", "description": "AbuseIPDB", "icon": "fa-external-link-alt", "target": "_blank","links": [ "https://www.abuseipdb.com/check/{value}" ]}


Finally, restart SOC to make the changes take effect:

::

  sudo so-soc-restart

OQL
---

Onion Query Language (OQL) starts with standard `Lucene query syntax <https://lucene.apache.org/core/2_9_4/queryparsersyntax.html>`_ and then allows you to add optional segments that control what Hunt does with the results from the query. The ``groupby`` segment tells Hunt to group by (aggregate) a particular field. So, for example, if you want to group by destination IP address, you can add ``| groupby destination.ip`` to your search (assuming it didn't already have a groupby statement). The ``groupby`` segment supports multiple aggregations so you can add more fields that you want to group by, separating those fields with spaces. For example, to group by destination IP address and then destination port, you could use ``| groupby destination.ip destination.port``.

Videos
------

.. seealso::

  To see Hunt in action, check out these Youtube videos:
  
  https://www.youtube.com/watch?v=TZ96aBEVhFU
  
  https://www.youtube.com/watch?v=0bwwZyedqdA

  https://www.youtube.com/watch?v=Is2shLAOyJs

  https://www.youtube.com/watch?v=Y-nZInToH8s
