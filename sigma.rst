.. _sigma:

Sigma
=====

Sigma rules are loaded into :ref:`elastalert` to monitor incoming logs for suspicious or noteworthy activity. Active sigma rules generate alerts that can then be found in :ref:`alerts`.

From https://github.com/Neo23x0/sigma:

    Sigma is a generic and open signature format that allows you to describe relevant log events in a straightforward manner. The rule format is very flexible, easy to write and applicable to any type of log file. The main purpose of this project is to provide a structured form in which researchers or analysts can describe their once developed detection methods and make them shareable with others.

Managing Sigma Rules
--------------------

You can manage Sigma rules via :ref:`detections`. There are two main ways to do so:

- From the main :ref:`detections` interface, you can search for the desired detection and click the binoculars icon.
- From the :ref:`alerts` interface, you can click an alert and then click the ``Tune Detection`` menu item.

Once you've used one of these methods to reach the detection detail page, you can check the Status field and use the slider to enable or disable the detection.

To tune the detection:

- click the TUNING tab
- click the blue + button
- select the type of tuning (Custom Filter)
- enter your custom filter in the Custom Filter field
- click the ``CREATE`` button

.. warning::

	Performance testing is still ongoing. We recommend avoiding the ``Malicious Nishang PowerShell Commandlets`` detection as it can cause serious performance problems. You may also want to avoid others with a status of ``experimental``.

Sigma Packages
--------------

You can choose from different Sigma packages:

https://github.com/SigmaHQ/sigma/blob/master/Releases.md

You can modify this setting via :ref:`administration` --> Configuration --> soc --> config --> server --> modules --> elastalertengine --> sigmaRulePackages.

Custom Repositories
-------------------

You can configure Security Onion to pull Sigma rules from custom git repos via :ref:`administration` --> Configuration --> soc --> config --> server --> modules --> elastalertengine --> rulesRepos --> default. Repos can be accessed via https or from the local filesystem (for example: ``file://nsm/rules/detect-sigma/repos/my-custom-rep``).

Update Frequency
----------------

By default, Security Onion checks for new Sigma rules every 24 hours. You can change this value as follows:

- Navigate to :ref:`administration` --> Configuration.
- At the top of the page, click the ``Options`` menu and then enable the ``Show all configurable settings, including advanced settings.`` option.
- Navigate to soc --> config --> server --> modules --> elastalertengine --> communityRulesImportFrequencySeconds.
