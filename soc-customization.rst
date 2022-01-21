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

In :ref:`alerts` and :ref:`hunt`, logs are shown with a blue triangle that allows you to escalate the event. Starting in Security Onion 2.3.100, this defaults to our new :ref:`cases` interface. If for some reason you want to escalate to a different case management system, you can change this setting.

Locate the ``soc`` :ref:`salt` pillar and then set ``case_module`` to one of the following values:

``soc`` - Enables the new built-in Case Management, with the new Escalation menu.

``thehive`` - Enables escalation directly to TheHive3. No escalation menu popup.

``generichttp`` - Enables escalation directly to an arbitrary web URL. No escalation menu popup.

``elasticcases`` - Enables escalation to the Elastic case system. No escalation menu popup.

When using ``thehive``, it is hardcoded to use TheHive instance URL bundled with Security Onion:

::
      "thehive": {
        "hostUrl": "http://{{ MANAGERIP }}:9000/thehive",
        "key": "{{ THEHIVEKEY }}",
        "verifyCert": false
      },

When using ``generichttp``, another pillar value under the same pillar group ``soc`` can be specified: ``generic_case_config``. This can contain all the options as mentioned at https://github.com/Security-Onion-Solutions/securityonion/issues/5791#issuecomment-946721865.

When using ``elasticcases`` it will use the same user/pass that SOC uses to talk to Elastic. Note that Elastic cases is actually a Kibana feature.

Making Changes Take Effect
--------------------------

Once all customizations are complete, you can then restart SOC to make the changes take effect:

::

        sudo so-soc-restart
