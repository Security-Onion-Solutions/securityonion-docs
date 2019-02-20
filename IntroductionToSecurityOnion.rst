Introduction
============

Network Security Monitoring (NSM) is, put simply, monitoring your network for security related events. It might be proactive, when used to identify vulnerabilities or expiring SSL certificates, or it might be reactive, such as in incident response and network forensics. Whether you’re tracking an adversary or trying to keep malware at bay, NSM provides context, intelligence and situational awareness of your network. Enterprise Security Monitoring (ESM) takes NSM to the next level and includes endpoint visibility and other telemetry from your enterprise. There are some commercial solutions that get close to what Security Onion provides, but very few contain the vast capabilities of Security Onion in one package.

Many assume NSM is a solution they can buy to fill a gap; purchase and deploy solution XYZ and problem solved. The belief that you can buy an NSM denies the fact that the most important word in the NSM acronym is “M” for Monitoring. Data can be collected and analyzed, but not all malicious activity looks malicious at first glance. While automation and correlation can enhance intelligence and assist in the process of sorting through false positives and malicious indicators, there is no replacement for human intelligence and awareness. I don’t want to disillusion you. Security Onion isn’t a silver bullet that you can setup, walk away from and feel safe. Nothing is and if that’s what you’re looking for you’ll never find it. Security Onion will provide visibility into your network traffic and context around alerts and anomalous events, but it requires a commitment from you the administrator or analyst to review alerts, monitor the network activity, and most importantly, have a willingness, passion and desire to learn.

Core Components
---------------

Security Onion seamlessly weaves together three core functions:

-  full packet capture;
-  network-based and host-based intrusion detection systems (NIDS and HIDS, respectively);
-  and powerful analysis tools.

*Full-packet capture* is accomplished via `<netsniff-ng>`_, “the packet sniffing beast”. netsniff-ng captures all the network traffic your Security Onion sensors see and stores as much of it as your storage solution will hold (Security Onion has a built-in mechanism to purge old data before your disks fill to capacity). Full packet capture is like a video camera for your network, but better because not only can it tell us who came and went, but also exactly where they went and what they brought or took with them (exploit payloads, phishing emails, file exfiltration). It’s a crime scene recorder that can tell us a lot about the victim and the white chalk outline of a compromised host on the ground. There is certainly valuable evidence to be found on the victim’s body, but evidence at the host can be destroyed or manipulated; the camera doesn't lie, is hard to deceive, and can capture a bullet in transit.

*Network-based and host-based intrusion detection systems* (IDS) analyze network traffic or host systems, respectively, and provide log and alert data for detected events and activity. Security Onion provides multiple IDS options:

NIDS:

-  Rule-driven NIDS. For rule-driven network intrusion detection, Security Onion offers the choice of `<Snort>`_ or `<Suricata>`_. Rule-based systems look at network traffic for fingerprints and identifiers that match known malicious, anomalous or otherwise suspicious traffic. You might say that they’re akin to antivirus signatures for the network, but they’re a bit deeper and more flexible than that.
-  Analysis-driven NIDS. For analysis-driven network intrusion detection, Security Onion offers `<Bro>`_ (Zeek).  Unlike rule-based systems that look for needles in the haystack of data, Bro says, “Here’s all your data and this is what I’ve seen. Do with it what you will and here’s a framework so you can.” Bro monitors network activity and logs any connections, DNS requests, detected network services and software, SSL certificates, and HTTP, FTP, IRC SMTP, SSH, SSL, and Syslog activity that it sees, providing a real depth and visibility into the context of data and events on your network. Additionally, Bro includes analyzers for many common protocols and by default has the capacity to check MD5 sums for HTTP file downloads against Team Cymru’s Malware Hash Registry project. Beyond logging activity and traffic analyzers, the Bro framework provides a very extensible way to analyze network data in real time. The input framework allows you to feed data into Bro, which can be scripted, for example, to read a comma delimited file of C-level employee usernames and correlate that against other activity, such as when they download an executable file from the Internet. The file analysis framework provides protocol independent file analysis, allowing you to capture files as they pass through your network and automatically pass them to a sandbox or a file share for antivirus scanning. The flexibility of Bro makes it an incredibly powerful ally in your defense.

HIDS:

-  For host-based intrusion detection, Security Onion offers `<Wazuh>`_, a free, open source HIDS for Windows, Linux and Mac OS X. When you add the Wazuh agent to endpoints on your network, you gain invaluable visibility from endpoint to your network’s exit point. Wazuh performs log analysis, file integrity checking, policy monitoring, rootkit detection, real-time alerting and active response. As an analyst, being able to correlate host-based events with network-based events can be the difference in identifying a successful attack.

Analysis Tools
--------------

With full packet capture, IDS logs and Bro data, there is a daunting amount of data available at the analyst’s fingertips. Fortunately, Security Onion integrates the following tools to help make sense of this data:

-  `<Sguil>`_, created by Bamm Visscher, is “The Analyst Console for Network Security Monitoring.” It is the analyst’s right hand, providing visibility into the event data being collected and the context to validate the detection. Sguil provides a single GUI in which to view Snort, Suricata, and Wazuh alerts. More importantly, Sguil allows you to pivot directly from an alert into a packet capture (via `Wireshark <wireshark>`_ or `NetworkMiner <networkminer>`_) or a transcript of the full session that triggered the alert. So, instead of seeing only an individual packet associated with an alert and being left with the unanswerable question, “What now?” or “What happened next?,” you can view all of the associated traffic and actually answer that question. Sguil differs from other alert interfaces in that it allows collaboration among analysts by allowing alerts to be commented on and escalated to more senior analysts who can take action on the alerts.

-  `<Squert>`_, originally developed by Paul Halliday, is a web application interface to the Sguil database. Although it is neither meant to be a real-time (or near real-time) interface nor a replacement for Sguil, it allows querying of the Sguil database and provides several visualization options for the data such as “time series representations, weighted and logically grouped result sets” and geo-IP mapping.  Squert can pivot to full packet capture via `<CapMe>`_.

-  `<Kibana>`_, created by the team at Elastic, allows us to quickly analyze and pivot between all of the different data types generated by Security Onion through a "single pane of glass".  Kibana can pivot to full packet capture via `<CapMe>`_.
    
- `<CapMe>`_, originally developed by Paul Halliday, allows you to view PCAP transcripts and download full PCAP files.  Squert and Kibana are pre-configured to pivot to CapMe to retrieve full packet capture.

Deployment Scenarios
--------------------

Analysts around the world are using Security Onion today for many different `use cases <Use-Cases>`_ and `architectures <Elastic-Architecture.html#deployment-types>`__.  The Security Onion Setup wizard allows you to easily configure the best installation scenario to suit your needs.

Conclusion
----------

So we have full packet capture, `<Snort>`_ or `<Suricata>`_ rule-driven intrusion detection, `<Bro>`_ event-driven intrusion detection and `<Wazuh>`_ host-based intrusion detection, all running out of the box once you run Security Onion setup. These disparate systems with various dependencies and complexities all run seamlessly together and would otherwise take hours, days or weeks to assemble and integrate on their own. What was once a seemingly impossible task is now as easy as answering a few questions.
