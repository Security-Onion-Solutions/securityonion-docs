ElastAlert
==========

From
http://elastalert.readthedocs.io/en/latest/elastalert.html#overview:

    ElastAlert is a simple framework for alerting on anomalies, spikes,
    or other patterns of interest from data in Elasticsearch.

    At Yelp, we use Elasticsearch, Logstash and Kibana for managing our
    ever increasing amount of data and logs. Kibana is great for
    visualizing and querying data, but we quickly realized that it
    needed a companion tool for alerting on inconsistencies in our data.
    Out of this need, ElastAlert was created. If you have data being
    when that data matches certain patterns, ElastAlert is the tool for
    you.

ElastAlert runs as a Docker container within Security Onion, queries ElasticSearch, and provides an alerting mechanism with multiple output types, such as Slack, Email, JIRA, OpsGenie, and many more.

Configuration
-------------

ElastAlert rules are stored in ``/etc/elastalert/rules/``.

Security Onion's default ElastAlert rules are configured with an output type of "debug", which simply outputs all matches queries to a log file, found in ``/var/log/elastalert/elastalert_stderr.log``.

Slack
~~~~~

To have ElastAlert send alerts to something like Slack, we can simply change the alert type and details for a rule like so:

::

    alert:
    - "slack":
        slack_webhook_url: "https://hooks.slack.com/services/YOUR_WEBHOOK_URI"

Email - Internal
~~~~~~~~~~~~~~~~

To have ElastAlert send to email, we could do something like the following:

::

    alert:
    - "email"
    email:
    - "youremail@yourcompany.com"
    smtp_host: "your_company_smtp_server"
    smtp_port: 25
    from_addr: "elastalert@yourcompany.com"

Email - External
~~~~~~~~~~~~~~~~

If we need to use an external email provider like Gmail, we can add something like the following:

::

    alert:
    - "email"
    email:
    - "youremail@gmail.com"
    smtp_host: "smtp.gmail.com"
    smtp_port: 465
    smtp_ssl: true
    from_addr: "youremail@gmail.com"
    smtp_auth_file: '/etc/elastalert/rules/smtp_auth_file.txt'

In the ``smtp_auth_file.txt``, add:

::

    user: youremail@gmail.com
    password: yourpassword   

MISP
~~~~~~~

See `<MISP>`__

TheHive
~~~~~~~

See `TheHive <hive>`__


so-elastalert-create
~~~~~~~~~~~~~~~~~~~~

``so-elastalert-create`` is a tool created by `Bryant Treacle <https://github.com/bryant-treacle/so-elastalert-create>`__ that can be used to help ease the pain of ensuring correct syntax and creating Elastalert rules from scratch. It will walk you through various questions, and eventually output an Elastalert rule file that you can deploy in your environment to start alerting quickly and easily.

Defaults
~~~~~~~~

With Security Onion's example rules, Elastalert is configured by default to only count the number of hits for a particular match, and will not return the actual log entry for which an alert was generated.

This is governed by the use of ``use_count_query: true`` in each rule file.

If you would like to view the data for the match, you can simply remark this line in the rule file(s). Keep in mind, this may impact performance negatively, so testing the change in a single file at a time may be the best approach.

Timeframe
~~~~~~~~~

Keep in mind, for queries that span greater than a minute back in time, you may want to add the following fields to your rule to ensure searching occurs as planned (for example, for 10 minutes):

::

    buffer_time:   
        minutes: 10   

``allow_buffer_time_overlap: true``

| https://elastalert.readthedocs.io/en/latest/ruletypes.html#buffer-time
| https://github.com/Yelp/elastalert/issues/805

More Information
----------------

| You can learn more about ElastAlert and its output types here:
| http://elastalert.readthedocs.io/en/latest/
