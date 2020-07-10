.. _freqserver:

FreqServer
==========

| FreqServer is based on freq.py and freq\_server.py (originally created by Mark Baggett).
| Thanks to Justin Henderson for all his work with the FreqServer docker image!

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

From https://isc.sans.edu/forums/diary/Continuous+Monitoring+for+Random+Strings/20451/

    Freq\_server.py is a multithreaded web based API that will allow you
    to quickly query your frequency tables. The server isn’t intended to
    replace freq.py. Instead, after building a frequency table of normal
    strings in your environment with freq.py, you start a server up to
    allow services to measure various strings against that table. You
    can run multiple servers to provide access to different frequency
    tables.

Configuration
-------------

For information on how to modify configuration for FreqServer, please see https://github.com/SMAPPER/docker_freq_server.

FreqServer is currently disabled by default.
