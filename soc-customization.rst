.. _soc-customization:

SOC Customization
=================

Overview Page
-------------

You can customize the main SOC Overview page that you see when you first log into SOC. The content of this page is stored in the ``motd.md`` file, which uses the common Markdown (.md) format. You can learn more about Markdown format at `<https://markdownguide.org>`_. To customize the Overview page content, copy ``motd.md`` as follows and then edit ``/opt/so/saltstack/local/salt/soc/files/soc/motd.md`` using your favorite text editor:

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

Escalation
----------

In :ref:`alerts` and :ref:`hunt`, logs are shown with a blue triangle that allows you to escalate the event. Starting in Security Onion 2.3.100, this defaults to our new :ref:`cases` interface. If for some reason you want to escalate to a different case management system, you can change this setting. To do so, locate the ``soc`` :ref:`salt` pillar and then set ``case_module`` to one of the following values:

- ``soc``: Enables the new built-in Case Management, with the new Escalation menu (default).

- ``thehive``: Enables escalation directly to TheHive v3 instance running in the Security Onion cluster (only applicable to existing installations that upgrade to 2.3.100). Escalations will always open a new case; there will not be an advanced escalation menu popup. Note that Security Onion support for thehive has ended, and thehive will no longer be included in future Security Onion releases. Therefore this option should only be considered for short-term, temporary usage.

- ``httpcase``: Enables escalation directly to an arbitrary web URL. Escalations will always open a new case; there will not be an advanced escalation menu popup. To use this module, you will need to add a second pillar value, for the pillar ``httpcase_config``. The value can include some, or all, of the following settings:

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
      
Example of a customized SOC pillar file located in /opt/so/saltstack/local/pillar/minions/import_import.sls (your file path will vary depending on your installation choices)

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

- ``elasticcases``: Enables escalation to the Elastic Cases tool. Escalations will always open a new case; there will not be an advanced escalation menu popup.  This module will use the same user/pass that SOC uses to talk to Elastic. Note, however, that Elastic cases is actually a Kibana feature, therefore, when this setting is used, SOC will be communicating with the local Kibana service (via its API) for case escalations.

Making Changes Take Effect
--------------------------

Once all customizations are complete, you can then restart SOC to make the changes take effect:

::

        sudo so-soc-restart
