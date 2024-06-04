.. _soc-customization:

SOC Customization
=================

You can customize :ref:`soc` by going to :ref:`administration` --> Configuration --> soc. 

.. image:: images/config-item-soc.png
  :target: _images/config-item-soc.png

Below are some ways in which you can customize SOC. Once all customizations are complete, you can make the changes take effect by clicking the ``Options`` bar at the top and then clicking the ``SYNCHRONIZE GRID`` button.

.. image:: images/88_config_options.png
  :target: _images/88_config_options.png

Login Page
----------

You can customize the SOC login page with a login banner by going to :ref:`administration` --> Configuration --> soc --> files --> soc --> Login Banner. The login banner uses the common Markdown (.md) format and you can learn more about that at `<https://markdownguide.org>`_.

Overview Page
-------------

After logging into SOC, you'll start on the main SOC Overview page which can be customized as well. You can customize this by going to :ref:`administration` --> Configuration --> soc --> files --> soc --> Overview Page. This uses Markdown format as mentioned above.

You can add images but they must be hosted from another host that is accessible by the user's browser. For example, let's use one of the images from our online documentation. The markdown to add that image would look like this:

::

        ![SOC Dashboards](https://docs.securityonion.net/en/2.4/_images/53_dashboards.png)

Links
-----

You can also customize the links on the left side. To do so, go to :ref:`administration` --> Configuration --> soc --> server --> client --> tools.

Reverse DNS Lookups
-------------------

When you are viewing IP addresses in :ref:`alerts`, :ref:`dashboards`, or :ref:`hunt`, you might want to enable automatic reverse DNS lookups to provide more information. You can do so by going to :ref:`administration` --> Configuration --> soc --> config --> server --> client --> enableReverseLookup.

Cases
-----

:ref:`cases` comes with presets for things like category, severity, TLP, PAP, tags, and status. You can modify these presets by going to :ref:`administration` --> Configuration --> soc --> server --> client --> case --> presets.

Session Timeout
---------------

The default timeout for user login sessions is 24 hours. This is a fixed timespan and will expire regardless of whether the user is active or idle in SOC. You can configure this by going to :ref:`administration` --> Configuration --> kratos --> sessiontimeout.

Custom Queries
--------------

If you'd like to add your own custom queries to :ref:`alerts`, :ref:`dashboards`, or :ref:`hunt`, you can go to :ref:`administration` --> Configuration --> soc --> server --> client and then select the specific app you'd like to modify.

To see all available fields for your queries, go down to the Events table and then click the arrow to expand a row. It will show all of the individual fields from that particular event.

For example, suppose you want to add GeoIP information like ``source.geo.region_iso_code`` or ``destination.geo.region_iso_code`` to :ref:`alerts`. You would go to :ref:`administration` --> Configuration --> soc --> server --> client --> alerts --> queries and insert the following line wherever you want it show up in the query list:

::

  { "name": "Group By Source IP/Port/Geo, Destination IP/Port/Geo, Name", "query": "* | groupby source.ip source.port source.geo.region_iso_code destination.ip destination.port destination.geo.region_iso_code rule.name" },

Please note that some events may not have GeoIP information and this query would only show those alerts that do have GeoIP information.

Action Menu
-----------

:ref:`alerts`, :ref:`dashboards`, and :ref:`hunt` have an action menu with several default actions. If you'd like to add your own custom HTTP GET or POST actions, you can go to :ref:`administration` --> Configuration --> soc --> actions. For example, suppose you want to add ``AbuseIPDB`` with URL ``https://www.abuseipdb.com/check/{value}``. Insert the following as the next to last line:

::

  ,{ "name": "AbuseIPDB", "description": "Search for this value at AbuseIPDB", "icon": "fa-external-link-alt", "target": "_blank","links": [ "https://www.abuseipdb.com/check/{value}" ]}

You can also create background actions that don't necessarily result in the user being taken to a new page or tab. For example, if you want to have a new action submit a case to JIRA, you would define it as a background POST action. When it completes the POST, it will show an auto-fading message in SOC telling you that the action completed. Alternatively, instead of the auto-fading message you can have it pop a new tab (or redirect SOC tab) to JIRA. Because of CORS restrictions, SOC can't expect to have visibility into the result of the background POST so there is no attempt to parse the response of any background action, other than the status code/text from the request's response.

Here is an example of a background action that submits a javascript fetch to a remote resource and then optionally shows the user a second URL:

::

  { 
    "name": "My Background Action", 
    "description": "Something wonderful!", 
    "icon": "fa-star", 
    "target": "_blank", 
    "links": [
      "http://somewhere.invalid/?somefield={:client.ip|base64}"
    ],
    "background": true, 
    "method": "POST", 
    "options": { 
      "mode": "no-cors", 
      "headers": { 
        "header1": "header1value",
        "header2": "header2value" 
      }
    }, 
    "body": "something={value|base64}",
    "backgroundSuccessLink": "https://securityonion.net?code={responseCode}&text={responseStatus}",
    "backgroundFailureLink": "https://google.com?q={error}"
  }

Note that the above JSON block cannot be pasted as-is into the SOC configuration screen, for the action field. Each custom action must be formatted onto a single line, as was shown in the earlier example. The immediate example above is formatted on multiple lines to make it easier to explain in the documentation below.

The ``options`` object is the same options object that will be passed into the Javascript ``fetch()`` method. You can read more about that at `<https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch>`_.

There may come a time where you are not sure what fields to target for the request body, or you may want to forward events of different types that contain different field names.  This is ideal if you would like to send the event to a case management system, a SOAR platform, or something similar.  In this case, the ``eventJson`` variable can be used to pass the entire event as a JSON string.

To use this variable, construct the body of the request within the action configuration, like so:

``"body": "{eventJson}"``

*NOTE*: You may run into issues using the ``eventJson`` variable, depending on the size of the event and the amount of data being passed in the request.

Escalation
----------

:ref:`alerts`, :ref:`dashboards`, and :ref:`hunt` display logs with a blue triangle that allows you to escalate the event. This defaults to our :ref:`cases` interface. If for some reason you want to escalate to a different case management system, you can change this setting. You can go to :ref:`administration` --> Configuration --> soc --> server --> modules --> cases and specify one of the following values:

- ``soc`` - Enables the built-in Case Management, with our Escalation menu (default).

- ``elasticcases`` - Enables escalation to the `Elastic Cases <https://www.elastic.co/guide/en/security/current/cases-overview.html>`_ tool. Escalations will always open a new case; there will not be an advanced escalation menu popup.  This module will use the same user/pass that SOC uses to talk to Elastic. Note, however, that Elastic cases is actually a Kibana feature, therefore, when this setting is used, SOC will be communicating with the local Kibana service (via its API) for case escalations.

