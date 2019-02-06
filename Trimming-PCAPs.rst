Introduction
============

PCAPs (as a data type) typically take up the most disk space on a
Security Onion sensor, and usually aren't able to be kept for extended
periods of time. We can lessen the space consumed by PCAPs and extend
our retention time by trimming them, using a special tool called
`TrimPCAP <https://www.netresec.com/?page=TrimPCAP>`__ from
`NETRESEC <https://www.netresec.com/>`__. Using this tool, we can trim
the flows within PCAPs to a desired size.

**Please be aware and cognizant of the fact that it may take a while to
process a large amount of PCAPs. With this in mind, you'll want to
consider running TrimPCAP at non-peak times (without high PCAP write
volume, etc.).**

| One retention schedule that could be used is as follows:
| (http://www.netresec.com/?page=Blog&month=2017-12&post=Don%27t-Delete-PCAP-Files---Trim-Them)

+----------------------+-------------------+
| Age                  | Size (per flow)   |
+======================+===================+
| Older than 3 days    | 1MB               |
+----------------------+-------------------+
| Older than 6 days    | 102KB             |
+----------------------+-------------------+
| Older than 30 days   | 10KB              |
+----------------------+-------------------+

Trimming
========

We can install TrimPCAP using the following commands:

::

    sudo apt-get install python-pip
    sudo pip install dpkt
    sudo pip install repoze.lru
    sudo wget -O /opt/trimpcap.py https://www.netresec.com/?download=trimpcap

Then we can run TrimPCAP, as follows (specifying a size of ``102KB`` per
flow, iterating over all PCAPs of all ages, in all directories):

``sudo /usr/bin/find /nsm/sensor_data/ -name "snort.log.??????????" -type f -exec sudo python /opt/trimpcap.py 102400 {} \;``

If we want to this for PCAPs older than 3 days, we can do something like
the following:

``sudo /usr/bin/find /nsm/sensor_data/ -name "snort.log.??????????" -mmin +$((60*72)) -type f -exec sudo python /opt/trimpcap.py 102400 {} \;``

We can then automate this using a cron job, so our PCAPs are checked
daily.

::

    #/etc/cron.d/trimpcap
    #
    #crontab entry for TrimPCAP

    TRIMPCAP="/opt/trimpcap.py"
    LOG="/var/log/trimpcap.log"
    SHELL=/bin/sh
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

    # Trim after 3 days
    0 1 * * * root echo $(date) >> $LOG; /usr/bin/find /nsm/sensor_data/ -name "snort.log.??????????" -mmin +$((60*72)) -type f -exec /usr/bin/python
    $TRIMPCAP 1000000 {} \; >> $LOG 2>&1;

To automatically configure PCAPs to be trimmed at the above recommended
intervals, we can do the following:

::

    sudo wget https://raw.githubusercontent.com/weslambert/misc/master/trimpcap_install && sudo chmod +x ./trimpcap_install && sudo ./trimpcap_install
