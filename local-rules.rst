.. _local-rules:

Adding Local Rules
==================

NIDS
----

You can add local NIDS rules by going to :ref:`administration` --> Configuration --> idstools --> rules --> Local Rules.

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
