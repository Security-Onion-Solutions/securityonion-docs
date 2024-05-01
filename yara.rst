.. _yara:

YARA
====

YARA rules are loaded into :ref:`strelka` to monitor files for suspicious or noteworthy characteristics. Active YARA rules generate alerts that can be found in :ref:`alerts`.

From https://virustotal.github.io/yara/:

    YARA is a tool aimed at (but not limited to) helping malware researchers to identify and classify malware samples. With YARA you can create descriptions of malware families (or whatever you want to describe) based on textual or binary patterns. Each description, a.k.a rule, consists of a set of strings and a boolean expression which determine its logic.

Managing YARA Rules
-------------------

From the main :ref:`detections` interface, search for the desired detection and click the binoculars icon. You can then use the Status slider to enable or disable the detection.
