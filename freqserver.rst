FreqServer
==========

| FreqServer is based on freq.py and freq\_server.py (originally created
  by Mark Baggett).
| Thanks to Justin Henderson for all his work with the FreqServer docker
  image!

From https://github.com/sans-blue-team/freq.py:

    Mark Baggett's (@MarkBaggett - GSE #15, SANS SEC573 Author)
    Awesome-Sauce tool for detecting randomness using NLP techniques
    rather than pure entropy calculations. Uses character pair frequency
    analysis to determine the likelihood of tested strings of characters
    occurring based upon the chosen frequency tables (some prebuilt
    English text freq tables provided). Extremely useful for detecting
    high entropy where it shouldn't be. Especially powerful for
    discovering DNS based DGAs commonly used for malware C2 and
    exfiltration. Think bigger than DGAs though. Random file names,
    script names, process names, service names, workstation names, TLS
    certificate subjects and issuer subjects, etc.

From
https://isc.sans.edu/forums/diary/Continuous+Monitoring+for+Random+Strings/20451/

    Freq\_server.py is a multithreaded web based API that will allow you
    to quickly query your frequency tables. The server isn’t intended to
    replace freq.py. Instead, after building a frequency table of normal
    strings in your environment with freq.py, you start a server up to
    allow services to measure various strings against that table. You
    can run multiple servers to provide access to different frequency
    tables.

Configuration
-------------

| For information how to modify configuration for FreqServer, consult
  the following:
| https://github.com/SMAPPER/docker_freq_server

| FreqServer is disabled by default when running ``Production Mode``
  with ``Best Practices``.
| You can enable it by doing the following:

::

    sudo sed -i 's/FREQ_SERVER_ENABLED="no"/FREQ_SERVER_ENABLED="yes"/' /etc/nsm/securityonion.conf
    sudo so-elastic-start
    sudo so-logstash-restart

FreqServer's logs can be found in ``/var/log/freq_server/``.

Kibana
------

You can find FreqServer data on the Frequency Analysis dashboard.

DNS Frequency Analysis
----------------------

| |freq1-dns|
| |freq2-dns|

HTTP Frequency Analysis
-----------------------

|freq3-http|

SSL Frequency Analysis
----------------------

| |freq4-ssl|
| |freq5-ssl|
| |freq6-ssl|

X.509 Frequency Analysis
------------------------

| |freq7-x509|
| |freq8-x509|
| |freq9-x509|

.. |freq1-dns| image:: https://user-images.githubusercontent.com/1659467/30856300-e60be17a-a285-11e7-87fc-acc27665cd7e.PNG
.. |freq2-dns| image:: https://user-images.githubusercontent.com/1659467/30856292-e5d0b186-a285-11e7-875e-7e55c4684507.PNG
.. |freq3-http| image:: https://user-images.githubusercontent.com/1659467/30856293-e5d0d47c-a285-11e7-8c91-af45cab8276e.PNG
.. |freq4-ssl| image:: https://user-images.githubusercontent.com/1659467/30856295-e5d1014a-a285-11e7-9dd4-19a2844dc824.PNG
.. |freq5-ssl| image:: https://user-images.githubusercontent.com/1659467/30856296-e5d1f320-a285-11e7-8892-86f6a0f599f1.PNG
.. |freq6-ssl| image:: https://user-images.githubusercontent.com/1659467/30856294-e5d0dd0a-a285-11e7-8186-179e52c49383.PNG
.. |freq7-x509| image:: https://user-images.githubusercontent.com/1659467/30856297-e5e2bbc4-a285-11e7-9cc4-87781d3d7768.PNG
.. |freq8-x509| image:: https://user-images.githubusercontent.com/1659467/30856299-e5e41500-a285-11e7-937b-dda97690c386.PNG
.. |freq9-x509| image:: https://user-images.githubusercontent.com/1659467/30856298-e5e2f9f4-a285-11e7-9c95-b24f44199701.PNG
