TheHive
=======

Elastalert Rules
----------------

We can send events to an instance of the TheHive, as Elastalert includes the TheHive alerter (`Nclose-ZA <https://github.com/Nclose-ZA/elastalert_hive_alerter>`__).

Simply modify the following rule as desired, and place the rule in ``/etc/elastalert/rules``, on your Security Onion box (master server if running Distributed Deployment).
::
    # hive.yaml
    # Elastalert rule to forward IDS alerts from Security Onion to a specified TheHive instance.
    #
    es_host: elasticsearch
    es_port: 9200
    name: TheHive - New IDS Alert!
    type: frequency
    index: "*:logstash-ids*"
    num_events: 1
    timeframe:
        minutes: 10
    buffer_time:
        minutes: 10
    allow_buffer_time_overlap: true

    filter:
    - term:
        event_type: "snort"

    alert: hivealerter
    
    hive_connection:
      hive_host: http(s)://YOUR_HIVE_INSTANCE:PORT # Add port if necessary
      hive_apikey: APIKEY

    hive_proxies:
      http: ''
      https: ''

    hive_alert_config:
      title: '{rule[name]} -- {match[alert]}'
      type: 'external'
      source: 'SecurityOnion'
      description: '{match[message]}'
      severity: 2
      tags: ['elastalert, SecurityOnion']
      tlp: 3
      status: 'New'
      follow: True

    hive_observable_data_mapping:
      - ip: '{match[source_ip]}'
      - ip: '{match[destination_ip]}'

