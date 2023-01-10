.. _soc-customization:

SOC Customization
=================

Below are some ways in which you can customize :ref:`soc`. Once all customizations are complete, you can then restart SOC to make the changes take effect:

::

        sudo so-soc-restart

Login Page
----------

You can customize the SOC login page with a login banner. The content of this banner is stored in the ``banner.md`` file, which uses the common Markdown (.md) format. You can learn more about Markdown format at `<https://markdownguide.org>`_. To customize the login banner, copy ``banner.md`` as follows and then edit ``/opt/so/saltstack/local/salt/soc/files/soc/banner.md`` using your favorite text editor:

::

        sudo cp /opt/so/saltstack/default/salt/soc/files/soc/banner.md /opt/so/saltstack/local/salt/soc/files/soc/
        
Overview Page
-------------

After logging into SOC, you'll start on the main SOC Overview page which can be customized as well. The content of this page is stored in the ``motd.md`` file, which uses Markdown format as mentioned above. To customize the Overview page content, copy ``motd.md`` as follows and then edit ``/opt/so/saltstack/local/salt/soc/files/soc/motd.md`` using your favorite text editor:

::

        sudo cp /opt/so/saltstack/default/salt/soc/files/soc/motd.md /opt/so/saltstack/local/salt/soc/files/soc/

Links
-----

You can also customize the links on the left side. To do so, copy ``tools.json`` as follows and then edit ``/opt/so/saltstack/local/salt/soc/files/soc/tools.json`` using your favorite text editor:

::

        sudo cp /opt/so/saltstack/default/salt/soc/files/soc/tools.json /opt/so/saltstack/local/salt/soc/files/soc/

Session Timeout
---------------

Another possible SOC customization is the session timeout. The default timeout for user login sessions is 24 hours. This is a fixed timespan and will expire regardless of whether the user is active or idle in SOC. This can be adjusted by adding a pillar value to the manager node's pillar sls. For example, on an eval node, edit ``/opt/so/saltstack/local/pillar/minions/eval_eval.sls`` and add a new ``kratos.sessiontimeout`` value:

::

        kratos:
          kratoskey: 'abcdef1234567890'
          sessiontimeout: 720h
          
Advanced Interface
------------------

The interface for :ref:`alerts` and :ref:`cases` is a simplified version of the interface seen in :ref:`dashboards` and :ref:`hunt`. :ref:`alerts` and :ref:`cases` have a new toggle under Options labeled ``Temporarily enable advanced interface features``.

.. image:: images/soc-toggle-advanced.png
  :target: _images/soc-toggle-advanced.png

If you enable this option, then the interface will show more advanced features similar to :ref:`dashboards` and :ref:`hunt`. These advanced features are only enabled temporarily so if you navigate away from the page and then return to the page, it will default back to its simplified view.

In versions older than 2.3.160, you can temporarily enable this by opening your browser console and then pasting the following:

::

        document.getElementById('hunt').__vue__.$parent._data.advanced=true
        

.. warning::

        Making this change permanent requires changes to ``soc.json`` which changes at nearly every release. So if you proceed with this, please be prepared to update to the new ``soc.json`` every time you update.

If you would like to make this change permanent, make a copy of ``soc.json``:

::

        cp /opt/so/saltstack/default/salt/soc/files/soc/soc.json /opt/so/saltstack/local/salt/soc/files/soc/
        
Then edit ``/opt/so/saltstack/local/salt/soc/files/soc/`` using your favorite text editor, find the ``alerts`` or ``cases`` section, and set ``advanced`` to ``true``. Don't forget that you will need to manually update ``soc.json`` every time you update to the latest version.

Custom Queries
--------------

If you'd like to add your own custom queries to :ref:`alerts`, :ref:`dashboards`, or :ref:`hunt`, you can copy the relevant ``queries.json`` file from ``/opt/so/saltstack/default/salt/soc/files/soc/`` to ``/opt/so/saltstack/local/salt/soc/files/soc/`` and then add new entries. For example, if you want to add a new dashboard, you can copy ``dashboards.queries.json`` and then add your new dashboard there.

To see all available fields for your queries, go down to the Events table and then click the arrow to expand a row. It will show all of the individual fields from that particular event.

For example, suppose you want to add GeoIP information like ``source.geo.region_iso_code`` or ``destination.geo.region_iso_code`` to :ref:`alerts`. You would first copy the ``alerts.queries.json``:

::

  sudo cp -n /opt/so/saltstack/default/salt/soc/files/soc/alerts.queries.json /opt/so/saltstack/local/salt/soc/files/soc/alerts.queries.json

Next edit the ``/opt/so/saltstack/local/salt/soc/files/soc/alerts.queries.json`` using your favorite text editor and insert the following line wherever you want it show up in the query list:

::

  { "name": "Group By Source IP/Port/Geo, Destination IP/Port/Geo, Name", "query": "* | groupby source.ip source.port source.geo.region_iso_code destination.ip destination.port destination.geo.region_iso_code rule.name" },

Please note that some events may not have GeoIP information and this query would only show those alerts that do have GeoIP information.

Action Menu
-----------

:ref:`alerts`, :ref:`dashboards`, and :ref:`hunt` have an action menu with several default actions. If you'd like to add your own custom HTTP GET or POST actions, you can copy ``/opt/so/saltstack/default/salt/soc/files/soc/menu.actions.json`` to ``/opt/so/saltstack/local/salt/soc/files/soc/menu.actions.json`` and then add new entries. (Previous to Security Onion 2.3.60, this would be done in ``alerts.actions.json`` or ``hunt.actions.json``.)

For example, suppose you want to add ``AbuseIPDB`` with URL ``https://www.abuseipdb.com/check/{value}``. First, copy ``/opt/so/saltstack/default/salt/soc/files/soc/menu.actions.json`` to ``/opt/so/saltstack/local/salt/soc/files/soc/menu.actions.json``:

::

  sudo cp -n /opt/so/saltstack/default/salt/soc/files/soc/menu.actions.json /opt/so/saltstack/local/salt/soc/files/soc/menu.actions.json


Next, edit ``/opt/so/saltstack/local/salt/soc/files/soc/menu.actions.json`` using your favorite text editor and insert the following as the next to last line of the file:

::

  ,{ "name": "AbuseIPDB", "description": "Search for this value at AbuseIPDB", "icon": "fa-external-link-alt", "target": "_blank","links": [ "https://www.abuseipdb.com/check/{value}" ]}

So once you've restarted SOC to make the change take effect:

- ``AbuseIPDB`` will display on the Actions menu.
- When you hover over that ``AbuseIPDB`` option, the description ``Search for this value at AbuseIPDB`` will appear.
- When you click the ``AbuseIPDB`` option, the browser will open a new tab and go to ``https://www.abuseipdb.com/check/{value}`` (replacing ``{value}`` with the original value that you clicked on that spawned the Action menu).

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
        "header2:" "header2value" 
      }
    }, 
    "body": "something={value|base64}",
    "backgroundSuccessLink": "https://securityonion.net?code={responseCode}&text={responseStatus}",
    "backgroundFailureLink": "https://google.com?q={error}"
  },
  
The ``options`` object is the same options object that will be passed into the Javascript ``fetch()`` method. You can read more about that at `<https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch>`_.

Cases
-----

:ref:`cases` comes with presets for things like category, severity, TLP, PAP, tags, and status. You can modify these presets by copying the appropriate presets file from ``/opt/so/saltstack/default/salt/soc/files/soc/`` to ``/opt/so/saltstack/local/salt/soc/files/soc/``, making changes there, and then restarting SOC.

Escalation
----------

:ref:`alerts`, :ref:`dashboards`, and :ref:`hunt` display logs with a blue triangle that allows you to escalate the event which defaults to our own :ref:`cases` interface. If for some reason you want to escalate to a different case management system, you can change this setting. To do so, locate the ``soc`` :ref:`salt` pillar and then set ``case_module`` to one of the following values:

- ``soc`` - Enables the new built-in Case Management, with the new Escalation menu (default).

- ``thehive`` - Enables escalation directly to TheHive v3 instance running in the Security Onion cluster (only applicable to existing installations that upgrade to 2.3.100). Escalations will always open a new case; there will not be an advanced escalation menu popup. Note that Security Onion support for TheHive has ended, and TheHive will no longer be included in future Security Onion releases. Therefore this option should only be considered for short-term, temporary usage.

- ``elasticcases`` - Enables escalation to the `Elastic Cases <https://www.elastic.co/guide/en/security/current/cases-overview.html>`_ tool. Escalations will always open a new case; there will not be an advanced escalation menu popup.  This module will use the same user/pass that SOC uses to talk to Elastic. Note, however, that Elastic cases is actually a Kibana feature, therefore, when this setting is used, SOC will be communicating with the local Kibana service (via its API) for case escalations.

- ``httpcase`` - Enables escalation directly to an arbitrary web URL. Escalations will always open a new case; there will not be an advanced escalation menu popup. To use this module, you will need to add a second pillar value, for the pillar ``httpcase_config``. The value can include some, or all, of the following settings:

::

      "hostUrl": "http://some.external.host/some/api",
      "headers": [
        "Authorization: basic Fa3Fa01mDmCC09dA",
        "x-some-key: 1122"
      ],
      "verifyCert": true,
      "createPath": "/some/url/path/to/create/a/case",
      "createMethod": "PUT",
      "createBody": "{\"myid\":\"{{ '{{ .Id }}' }}\", \"title\":\"{{ '{{ .Title }}' }}\", \"desc\":\"{{ '{{ .Description | js }}' }}\"}",
      "createContentType": "application/json",
      "createSuccessCode": 200
      
Example of a customized SOC pillar file located in ``/opt/so/saltstack/local/pillar/minions/import_import.sls`` (your file path will vary depending on your installation choices):

::

      soc:
        es_index_patterns: '*:so-*,*:endgame-*'
        case_module: httpcase
        httpcase_config: |
          "hostUrl": "http://172.17.0.1/some/api",
          "headers": [
            "Authorization: basic Fa3Fa01mDmCC09dA",
            "x-some-key: 1122"
          ],
          "verifyCert": true,
          "createPath": "/some/url/path/to/create/a/case",
          "createMethod": "PUT",
          "createBody": "{\"myid\":\"{{ '{{ .Id }}' }}\", \"title\":\"{{ '{{ .Title }}' }}\", \"desc\":\"{{ '{{ .Description | js }}' }}\"}",
          "createContentType": "application/json",
          "createSuccessCode": 200


