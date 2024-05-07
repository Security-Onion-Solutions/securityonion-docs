.. _yara:

YARA
====

YARA rules are loaded into :ref:`strelka` to monitor files for suspicious or noteworthy characteristics. Active YARA rules generate alerts that can be found in :ref:`alerts`.

From https://virustotal.github.io/yara/:

    YARA is a tool aimed at (but not limited to) helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families (or whatever you want to describe) based on textual or binary patterns. Each description, a.k.a rule, consists of a set of strings and a boolean expression which determine its logic.

Managing YARA Rules
-------------------

You can enable or disable YARA rules using :ref:`detections`. From the main :ref:`detections` interface, search for the desired detection and click the binoculars icon. You can then use the Status slider to enable or disable the detection.

Custom Repositories
-------------------

You can configure Security Onion to pull YARA rules from custom git repos via :ref:`administration` --> Configuration --> soc --> config --> server --> modules --> strelkaengine --> rulesRepos --> default. Repos can be accessed via https or from the local filesystem (for example: ``file://nsm/rules/detect-yara/repos/my-custom-rep``).

Update Frequency
----------------

By default, Security Onion checks for new YARA rules every 24 hours. You can change this value as follows:

- Navigate to :ref:`administration` --> Configuration.
- At the top of the page, click the ``Options`` menu and then enable the ``Show all configurable settings, including advanced settings.`` option.
- Navigate to soc --> config --> server --> modules --> strelkaengine --> communityRulesImportFrequencySeconds.
