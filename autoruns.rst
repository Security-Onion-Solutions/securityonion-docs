Autoruns
========

From https://technet.microsoft.com/en-us/sysinternals/bb963902.aspx:

    This utility, which has the most comprehensive knowledge of
    auto-starting locations of any startup monitor, shows you what
    programs are configured to run during system bootup or login, and
    when you start various built-in Windows applications like Internet
    Explorer, Explorer and media players. These programs and drivers
    include ones in your startup folder, Run, RunOnce, and other
    Registry keys. Autoruns reports Explorer shell extensions, toolbars,
    browser helper objects, Winlogon notifications, auto-start services,
    and much more. Autoruns goes way beyond other autostart utilities.

Integration
-----------

Wazuh
~~~~~

Currently, our Autoruns dashboard in Kibana works only with Autoruns logs shipped via Wazuh. If you are trying to ship Autoruns logs via Winlogbeat, you can create a custom dashboard and visualizations that reference the ``logstash-beats-*`` indices, or view Autoruns logs via the ``Beats`` dashboard.

Pertinax
~~~~~~~~

| Josh Brower developed a great project called Pertinax to normalize autoruns data and integrate it into Security Onion:
| https://github.com/defensivedepth/Pertinax/wiki/Introduction
|
| Execute autoruns and ar-normalize.ps1 as shown here:
| https://github.com/defensivedepth/Pertinax/wiki/Reference%20Architecture

AutorunsToWinEventLog
~~~~~~~~~~~~~~~~~~~~~

| Another method for integrating Autoruns into your logging infrastructure is AutorunsToWinEventLog:
| https://github.com/palantir/windows-event-forwarding/tree/master/AutorunsToWinEventLog

Downloads
---------

| Download Autoruns here:
| https://download.sysinternals.com/files/Autoruns.zip
|
| Download ar-normalize.ps1 here:
| https://raw.githubusercontent.com/defensivedepth/Pertinax/master/normalize/ar-normalize.ps1
