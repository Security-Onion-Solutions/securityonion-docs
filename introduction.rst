.. _introduction:

Introduction
============

Network Security Monitoring (NSM) is, put simply, monitoring your network for security related events. It might be proactive, when used to identify vulnerabilities or expiring SSL certificates, or it might be reactive, such as in incident response and network forensics. Whether you’re tracking an adversary or trying to keep malware at bay, NSM provides context, intelligence and situational awareness of your network. Enterprise Security Monitoring (ESM) takes NSM to the next level and includes endpoint visibility and other telemetry from your enterprise. There are some commercial solutions that get close to what Security Onion provides, but very few contain the vast capabilities of Security Onion in one package.

In the diagram below, we see Security Onion in a traditional enterprise network with a firewall, workstations, and servers. You can use Security Onion to monitor north/south traffic to detect an adversary entering an environment, establishing command-and-control (C2), or perhaps data exfiltration. You'll probably also want to monitor east/west traffic to detect lateral movement. As more and more of our network traffic becomes encrypted, it's important to fill in those blind spots with additional visibility in the form of endpoint telemetry. Security Onion can consume logs from your servers and workstations so that you can then hunt across all of your network and host logs at the same time.

.. image:: images/network-horiz.png
   :target: _images/network-horiz.png
   
Many assume NSM is a solution they can buy to fill a gap; purchase and deploy solution XYZ and problem solved. The belief that you can buy an NSM denies the fact that the most important word in the NSM acronym is “M” for Monitoring. Data can be collected and analyzed, but not all malicious activity looks malicious at first glance. While automation and correlation can enhance intelligence and assist in the process of sorting through false positives and malicious indicators, there is no replacement for human intelligence and awareness. I don’t want to disillusion you. Security Onion isn’t a silver bullet that you can setup, walk away from and feel safe. Nothing is and if that’s what you’re looking for you’ll never find it. Security Onion will provide visibility into your network traffic and context around alerts and anomalous events, but it requires a commitment from you the defender to review alerts, monitor the network activity, and most importantly, have a willingness, passion, and desire to learn.

Overview
--------

Security Onion seamlessly weaves together three core functions:

-  full packet capture
-  network and endpoint detection
-  powerful analysis tools

*Full-packet capture* is accomplished via :ref:`stenographer`. Stenographer captures all the network traffic your Security Onion sensors see and stores as much of it as your storage solution will hold (it has a built-in mechanism to purge old data before your disks fill to capacity). Full packet capture is like a video camera for your network, but better because not only can it tell us who came and went, but also exactly where they went and what they brought or took with them (exploit payloads, phishing emails, file exfiltration). It’s a crime scene recorder that can tell us a lot about the victim and the white chalk outline of a compromised host on the ground. There is certainly valuable evidence to be found on the victim’s body, but evidence at the host can be destroyed or manipulated; the camera doesn't lie, is hard to deceive, and can capture a bullet in transit.

*Network and endpoint detection* analyzes network traffic or host systems, respectively, and provide log and alert data for detected events and activity. Security Onion provides multiple options:

-  Rule-driven NIDS. For rule-driven network intrusion detection, Security Onion 2.0 uses :ref:`suricata`. Rule-based systems look at network traffic for fingerprints and identifiers that match known malicious, anomalous or otherwise suspicious traffic. You might say that they’re akin to antivirus signatures for the network, but they’re a bit deeper and more flexible than that.
-  Protocol metadata. For analysis-driven network intrusion detection, Security Onion offers :ref:`zeek` (Zeek).  Unlike rule-based systems that look for needles in the haystack of data, Zeek says, “Here’s all your data and this is what I’ve seen. Do with it what you will and here’s a framework so you can.” Zeek monitors network activity and logs any connections, DNS requests, detected network services and software, SSL certificates, and HTTP, FTP, IRC, SMTP, SSH, SSL, and Syslog activity that it sees, providing a real depth and visibility into the context of data and events on your network. Additionally, Zeek includes analyzers for many common protocols and by default has the capacity to check MD5 sums for HTTP file downloads against Team Cymru’s Malware Hash Registry project. Beyond logging activity and traffic analyzers, the Zeek framework provides a very extensible way to analyze network data in real time. The input framework allows you to feed data into Zeek, which can be scripted, for example, to read a comma delimited file of C-level employee usernames and correlate that against other activity, such as when they download an executable file from the Internet. The file analysis framework provides protocol independent file analysis, allowing you to capture files as they pass through your network and automatically pass them to a sandbox or a file share for antivirus scanning. The flexibility of Zeek makes it an incredibly powerful ally in your defense.
-  For endpoint detection, Security Onion offers :ref:`wazuh`, a free, open source HIDS for Windows, Linux and Mac OS X. When you add the Wazuh agent to endpoints on your network, you gain invaluable visibility from endpoint to your network’s exit point. Wazuh performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting and active response. As an analyst, being able to correlate host-based events with network-based events can be the difference in identifying a successful attack. A new addition to Security Onion 2.0 is :ref:`osquery`, which is another free and open source endpoint agent.

In addition to the above, Security Onion can collect data via syslog or other agent transport like :ref:`beats`.

Analysis Tools
--------------

With full packet capture, IDS alerts, Zeek data, and endpoint telemetry, there is a daunting amount of data available at the analyst’s fingertips. Fortunately, Security Onion tightly integrates the following tools to help make sense of this data:

-  :ref:`hive` is the incident response interface. It displays alerts and allows you to turn them into cases where you and your fellow defenders can record your case notes and ultimately close the case. TheHive allows you to pivot to Hunt or Kibana for further context.

.. image:: https://user-images.githubusercontent.com/1659467/87230310-2d815380-c37d-11ea-9af8-a89a43afe0ef.png
  :target: https://user-images.githubusercontent.com/1659467/87230310-2d815380-c37d-11ea-9af8-a89a43afe0ef.png

- :ref:`soc` is the first thing you see when you log into Security Onion. It includes a new :ref:`Hunt` interface for threat hunting which allows you to query all of your NIDS/HIDS alerts, Zeek logs, and system logs. SOC also includes an interface for full packet capture retrieval.

.. image:: https://user-images.githubusercontent.com/1659467/87226371-4da31980-c361-11ea-8583-728f6d553884.png
  :target: https://user-images.githubusercontent.com/1659467/87226371-4da31980-c361-11ea-8583-728f6d553884.png
  
-  :ref:`kibana`, created by the team at Elastic, allows us to quickly analyze and pivot between all of the different data types generated by Security Onion through a "single pane of glass".  This includes not only NIDS/HIDS alerts, but also Zeek logs and system logs collected via syslog or other agent transport.  Kibana can pivot to full packet capture via :ref:`soc`.

.. image:: https://user-images.githubusercontent.com/1659467/87230185-168e3180-c37c-11ea-90a5-57c9d2f34f7b.png
  :target: https://user-images.githubusercontent.com/1659467/87230185-168e3180-c37c-11ea-90a5-57c9d2f34f7b.png
  
-  :ref:`cyberchef` allows you decode, decompress, and analyze artifacts.

.. image:: https://user-images.githubusercontent.com/1659467/87230242-9c11e180-c37c-11ea-90a2-e956771f3466.png
  :target: https://user-images.githubusercontent.com/1659467/87230242-9c11e180-c37c-11ea-90a2-e956771f3466.png
  
-  :ref:`playbook` is a web application that allows you to create a Detection Playbook, which itself consists of individual plays. These plays are fully self-contained and describe the different aspects around the particular detection strategy.

.. image:: https://user-images.githubusercontent.com/1659467/87230271-c5cb0880-c37c-11ea-8a36-24cabf137ed2.png
  :target: https://user-images.githubusercontent.com/1659467/87230271-c5cb0880-c37c-11ea-8a36-24cabf137ed2.png
  
Deployment Scenarios
--------------------

Analysts around the world are using Security Onion today for many different :ref:`architectures <architecture>`.  The Security Onion Setup wizard allows you to easily configure the best installation scenario to suit your needs.

Conclusion
----------

So we have full packet capture, :ref:`suricata` rule-driven intrusion detection, :ref:`zeek` event-driven intrusion detection and :ref:`wazuh` host-based intrusion detection, all running out of the box once you run Security Onion setup. These disparate systems with various dependencies and complexities all run seamlessly together and would otherwise take hours, days or weeks to assemble and integrate on their own. What was once a seemingly impossible task is now as easy as answering a few questions.
