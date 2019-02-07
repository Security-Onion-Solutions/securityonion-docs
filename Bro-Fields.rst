Bro Fields
============

The following lists field names as they are formatted in Bro logs, then
processed by Logstash and ingested into Elasticsearch.

The original field name (from Bro) appears on the left, and if changed,
the updated name or formatting of the field (Elasticsearch) will appear
on the right.

**(Bro => Elastic)**

#### conn.log
-------------

| ``type:bro_conn``
| ``/etc/logstash/conf.d/1100_preprocess_bro_conn.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| proto => protocol
| service
| duration
| orig\_bytes => original\_bytes
| resp\_bytes => respond\_bytes
| conn\_state => connection\_state => connection\_state\_description

::

    Dictionary
    S0 "Connection attempt seen, no reply"   
    S1 "Connection established, not terminated"   
    S2 "Connection established and close attempt by originator seen (but no reply from responder)"   
    S3 "Connection established and close attempt by responder seen (but no reply from originator)"   
    SF "Normal SYN/FIN completion"   
    REJ "Connection attempt rejected"   
    RSTO "Connection established, originator aborted (sent a RST)"   
    RSTR "Established, responder aborted"  

| local\_orig
| local\_resp => local\_respond
| missed\_bytes
| history
| orig\_pkts => original\_packets
| orig\_ip\_bytes => original\_ipbytes
| resp\_pkts => respond\_packets
| resp\_ip\_bytes => respond\_ipbytes
| tunnel\_parents
| original\_country\_code
| respond\_country\_code
| sensor\_name

#### dhcp.log
-------------

| ``type:bro_dhcp``
| ``/etc/logstash/conf.d/1101_preprocess_bro_dhcp.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| mac
| assigned\_ip
| lease\_time
| trans\_id => transaction\_id

#### dns.log
------------

| ``type:bro_dns``
| ``/etc/logstash/conf.d/1102_preprocess_bro_dns.conf``

| ts = > timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| proto => protocol
| trans\_id => transaction\_id
| rtt
| query
| qclass => query\_class
| qclass\_name => query\_class\_name
| qtype => query\_type
| qtype\_name => query\_type\_name
| rcode
| rcode\_name
| AA => aa
| TC => tc
| RD => rd
| RA => ra
| Z => z
| answers
| TTLS => ttls (removed if not available)
| rejected

#### dpd.log
------------

| ``type:bro_dpd``
| ``/etc/logstash/conf.d/1103_preprocess_bro_dpd.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| proto => protocol
| analyzer
| failure\_reason

#### files.log
--------------

| ``type:bro_files``
| ``/etc/logstash/conf.d/1104_preprocess_bro_files.conf``

| ts => timestamp
| fuid
| tx\_hosts => file\_ip
| rx\_hosts => destination\_ip
| conn\_uids => connection\_uids
| source
| depth
| analyzers => analyzer
| mime\_type => mimetype
| filename => file\_name
| duration
| local\_orig
| is\_orig
| seen\_bytes
| total\_bytes
| missing\_bytes
| overflow\_bytes
| timedout => timed\_out
| parent\_fuid
| md5
| sha1
| sha256
| extracted
| extracted\_cutoff
| extracted\_size

#### ftp.log
------------

| ``type:bro_ftp``
| ``/etc/logstash/conf.d/1105_preprocess_bro_ftp.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| user => ftp\_username
| password
| command => ftp\_command
| arg => ftp\_argument
| mime\_type => mimetype
| file\_size
| reply\_code
| reply\_msg => reply\_message
| data\_channel.passive => data\_channel\_passive
| data\_channel.orig\_h => data\_channel\_source\_ip
| data\_channel.resp\_h => data\_channel\_destination\_ip
| data\_channel.resp\_h => data\_channel\_destination\_port
| fuid

#### http.log
-------------

| ``type:bro_http``
| ``/etc/logstash/conf.d/1106_preprocess_bro_http.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| trans\_depth
| method
| host => virtual\_host
| uri
| referrer
| version
| user\_agent => useragent
| request\_body\_len => request\_body\_length
| response\_body\_len => response\_body\_length
| status\_code
| status\_message
| info\_code
| info\_msg => info\_message
| tags (removed)
| username => user
| password
| proxied
| orig\_fuids
| orig\_filenames
| orig\_mime\_types
| resp\_fuids
| resp\_filenames
| resp\_mime\_types

#### intel.log
--------------

| ``type:bro_intel``
| ``/etc/logstash/conf.d/1124_preprocess_bro_intel.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| seen.indicator => indicator
| seen.indicator\_type => indicator\_type
| seen.where => seen\_where
| seen.node => seen\_node
| matched
| sources
| fuid
| file\_mime\_type => mimetype
| file\_desc => file\_description

#### irc.log
------------

| ``type:bro_irc``
| ``/etc/logstash/conf.d/1107_preprocess_bro_irc.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| nick
| user => irc\_username
| command => irc\_command
| value
| addl => additional\_info
| dcc\_file\_name
| dcc\_file\_size
| dcc\_mime\_type
| fuid

#### kerberos.log
-----------------

| ``type:bro_kerberos``
| ``/etc/logstash/conf.d/1108_preprocess_bro_kerberos.conf``

| timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| request\_type
| client
| service
| success => kerberos\_success
| error\_msg => error\_message
| from => email\_from
| till => valid\_till
| cipher
| forwardable
| renewable
| client\_cert => client\_certificate\_subject
| client\_cert\_fuid => client\_certificate\_uid
| server\_cert\_subject => server\_certificate\_subject
| server\_cert\_fuid => server\_certificate\_fuid

#### modbus.log
---------------

| ``type:bro_modbus``
| ``/etc/logstash/conf.d/1125_preprocess_bro_modbus.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| func => function
| exception

#### mysql.log
--------------

| ``type:bro_mysql``
| ``/etc/logstash/conf.d/1121_preprocess_bro_mysql.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| cmd => mysql\_command
| arg => mysql\_argument
| success => mysql\_success
| rows
| response

#### notice.log
---------------

| ``type:bro_notice``
| ``/etc/logstash/conf.d/1109_preprocess_bro_notice.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| fuid
| mime => file\_mime\_type
| desc => file\_description
| proto => protocol
| note => note
| msg => msg
| sub => sub\_msg
| src => source\_ip
| dst => destination\_ip
| p
| n
| peer\_descr => peer\_description
| actions => action
| suppress\_for
| dropped
| destination\_country\_code
| destination\_region
| destination\_city
| destination\_latitude
| destination\_longitude

#### pe.log
-----------

| ``type:bro_pe``
| ``/etc/logstash/conf.d/1128_preprocess_bro_pe.conf``

| ts => timestamp
| fuid
| machine
| compile\_ts
| os
| subsystem
| is\_exe
| is\_64bit
| uses\_aslr
| uses\_dep
| uses\_code\_integrity
| uses\_seh
| has\_import\_table
| has\_export\_table
| has\_cert\_table
| has\_debug\_data
| section\_names

#### radius.log
---------------

| ``type:bro_radius``
| ``/etc/logstash/conf.d/1127_preprocess_bro_radius.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| username => radius\_username
| mac
| remote\_ip
| connect\_info
| result
| logged

#### rdp.log
------------

| ``type:bro_rdp``
| ``/etc/logstash/conf.d/1110_preprocess_bro_rdp.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| cookie
| result
| security\_protocol
| keyboard\_layout
| client\_build
| client\_name
| client\_dig\_product\_id => client\_digital\_product\_id
| desktop\_width
| desktop\_height
| requested\_color\_depth
| cert\_type => certificate\_type
| cert\_count => certificate\_count
| cert\_permanent => certificate\_permanent
| encryption\_level
| encryption\_method

#### rfb.log
------------

| ``type:bro_rfb``
| ``/etc/logstash/conf.d/1129_preprocess_bro_rfb.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| client\_major\_version
| client\_minor\_version
| server\_major\_version
| server\_minor\_version
| authentication\_method
| auth
| share\_flag
| desktop\_name
| width
| height

#### signatures.log
-------------------

| ``type:bro_ssl``
| ``/etc/logstash/conf.d/1111_preprocess_bro_signatures.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| note
| sig\_id => signature\_id
| event\_msg => event\_message
| sub\_msg => sub\_message
| sig\_count => signature\_count
| host\_count

#### sip.log
------------

| ``type:bro_sip``
| ``/etc/logstash/conf.d/1126_preprocess_bro_sip.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| trans\_depth
| method
| uri
| date
| request\_from
| request\_to
| response\_from
| response\_to
| reply\_to
| call\_id
| seq
| subject
| request\_path
| response\_path
| user\_agent
| status\_code
| status\_msg
| warning
| request\_body\_len
| response\_body\_len
| content\_type

#### smtp.log
-------------

| ``type:bro_smtp``
| ``/etc/logstash/conf.d/1112_preprocess_bro_smtp.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| trans\_depth
| helo
| mailfrom => mail\_from
| rcptto => recipient\_to
| date => mail\_date
| from
| to
| cc
| reply\_to
| msg\_id => message\_id
| in\_reply\_to
| subject
| x\_originating\_ip
| first\_received
| second\_received
| last\_reply
| path
| useragent => user\_agent
| tls
| fuids
| is\_webmail

#### snmp.log
-------------

| ``type:bro_snmp``
| ``/etc/logstash/conf.d/1113_preprocess_bro_snmp.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| duration
| version
| community
| get\_requests
| get\_bulk\_requests
| get\_responses
| set\_requests => set\_responses
| display\_string
| up\_since

#### socks.log
--------------

| ``type:bro_socks``
| ``/etc/logstash/conf.d/1122_preprocess_bro_socks.conf``

| timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| version
| user
| password
| status => server\_status
| request

-  => request\_host
-  => request\_name

request\_p => request\_port

bound

-  => bound\_host
-  => bound\_name

bound\_p => bound\_port

#### software.log
-----------------

| ``type:bro_software``
| ``/etc/logstash/conf.d/1114_preprocess_bro_software.conf``

| ts => timestamp
| host => source\_ip
| host\_p => source\_port
| software\_type
| name
| major => version\_major
| minor => version\_minor
| minor2 => version\_minor2
| minor3 => version\_minor3
| addl => version\_additional\_info
| unparsed\_version

#### ssh.log
------------

| ``type:bro_ssh``
| ``/etc/logstash/conf.d/1115_preprocess_bro_ssh.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| version
| auth\_success => authentication\_success
| auth\_attempts => authentication\_attempts
| direction
| client
| server
| cipher\_alg => cipher\_algorithm
| mac\_alg => mac\_algorithm
| compression\_alg => compression\_algorithm
| kex\_alg => kex\_algorithm
| host\_key\_alg => host\_key\_algorithm
| host\_key
| destination\_country\_code
| destination\_region
| destination\_city
| destination\_latitude
| destination\_longitude

#### ssl.log
------------

| ``type:bro_ssl``
| ``/etc/logstash/conf.d/1116_preprocess_bro_ssl.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| version
| cipher
| curve
| server\_name
| resumed
| last\_alert
| next\_protocol
| established
| cert\_chain\_fuids => certificate\_chain\_fuids
| client\_cert\_chain\_fuids => client\_certificate\_chain\_fuids
| subject => certificate\_subject

::

    CN => "certificate_common_name"
    C => "certificate_country_code"
    O => "certificate_organization"
    OU => "certificate_organization_unit"
    ST => "certificate_state"
    SN => "certificate_surname"
    L => "certificate_locality"
    GN => "certificate_given_name"
    pseudonym => "certificate_pseudonym"
    serialNumber => "certificate_serial_number"
    title => "certificate_title"
    initials" => "certificate_initials" 

certificate\_issuer

::

    CN => "issuer_common_name"
    C => "issuer_country_code"
    O => "issuer_organization"
    OU => "issuer_organization_unit"
    ST => "issuer_state"
    SN => "issuer_surname"
    L => "issuer_locality"
    DC => "issuer_distinguished_name"
    GN => "issuer_given_name"
    pseudonym => "issuer_pseudonym"
    serialNumber => "issuer_serial_number"
    title => "issuer_title"
    initials => "issuer_initials"

| client\_subject
| client\_issuer
| validation\_status
| ja3 (if JA3 enabled)

#### syslog.log
---------------

| ``type:bro_syslog``
| ``/etc/logstash/conf.d/1117_preprocess_bro_syslog.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| proto => protocol
| facility
| severity
| message

#### tunnel.log
---------------

| ``type:bro_tunnel``
| ``/etc/logstash/conf.d/1118_preprocess_bro_tunnel.conf``

| ts => timestamp
| uid
| id.orig\_h => source\_ip
| id.orig\_p => source\_port
| id.resp\_h => destination\_ip
| id.resp\_p => destination\_port
| tunnel\_type
| action

#### weird.log
--------------

| ``type:bro_weird``
| ``/etc/logstash/conf.d/1119_preprocess_bro_weird.conf``

| ts => timestamp
| uid
| name
| addl => additional\_info
| notice
| peer

#### x509.log
-------------

| ``type:bro_x509``
| ``/etc/logstash/conf.d/1123_preprocess_bro_x509.conf``

| ts => timestamp
| id
| certificate =>

-  certificate\_version
-  certificate\_serial
-  certificate\_subject
-  certificate\_issuer
-  certificate\_not\_valid\_before
-  certificate\_not\_valid\_after
-  certificate\_key\_algorithm
-  certificate\_signing\_algorithm
-  certificate\_key\_type
-  certificate\_key\_length
-  certificate\_exponent
-  certificate\_curve

san =>

-  san\_dns
-  san\_uri
-  san\_email
-  san\_ip

basic\_constraints =>

-  basic\_constraints\_ca
-  basic\_constraints\_path\_length

Pivot Fields
------------

The following fields are formatted as a URL within Kibana, so we can
easily pivot from them to the Indicator dashboard by clicking on them:

| destination\_ip
| destination\_port
| file\_ip
| indicator
| orig\_fuids
| query
| resp\_fuids
| server\_name
| source\_ip
| source\_port
| uid
| virtual\_host
