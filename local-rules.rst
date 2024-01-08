.. _local-rules:

Adding Local Rules
==================

NIDS
----

You can add local NIDS rules by going to :ref:`administration` --> Configuration --> idstools.

.. image:: images/config-item-idstools.png
  :target: _images/config-item-idstools.png
   
At the top of the page, click the ``Options`` menu and then enable the ``Show all configurable settings, including advanced settings.`` option. Then navigate to idstools --> rules --> Local Rules. Add your new rule(s) and click the checkmark to save them. The configuration will be applied at the next 15-minute interval or you can apply it immediately by clicking the ``SYNCHRONIZE GRID`` button under the ``Options`` menu.

YARA
----

Default YARA rules are provided from Florian Roth's `signature-base` Github repo at https://github.com/Neo23x0/signature-base.

Local YARA Rules
~~~~~~~~~~~~~~~~

To add local YARA rules, create a directory in ``/opt/so/saltstack/local/salt/strelka/rules``, for example ``localrules``.  Inside of ``/opt/so/saltstack/local/salt/strelka/rules/localrules``, add your YARA rules.

After adding your rules, update the configuration by running ``so-strelka-restart`` on all nodes running Strelka.

Alternatively, run ``salt -G 'role:so-sensor' cmd.run "so-strelka-restart"`` to restart Strelka on all sensors at once.

Remote YARA Rules
~~~~~~~~~~~~~~~~~

If you have Internet access and want to have ``so-yara-update`` pull YARA rules from a remote Github repo, copy ``/opt/so/saltstack/local/salt/strelka/rules/``, and modify ``repos.txt`` to include the repo URL (one per line).

Next, run ``so-yara-update`` to pull down the rules. Finally, run ``so-strelka-restart`` to allow Strelka to pull in the new rules.
