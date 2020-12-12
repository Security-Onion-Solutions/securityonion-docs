.. _grafana:

Grafana
=======

Once you've logged into :ref:`soc`, you can then click the Grafana link to see system health information. 

.. image:: https://user-images.githubusercontent.com/1659467/87230207-57864600-c37c-11ea-98a2-e9a4d4494c3a.png
  :target: https://user-images.githubusercontent.com/1659467/87230207-57864600-c37c-11ea-98a2-e9a4d4494c3a.png

On a distributed deployment, you will default to the manager dashboard. There are also dashboards for other node types. Once you've accessed the node dashboards, they should be added to ``Recently viewed dashboards`` which is accessible by simply clicking the Dashboards icon:

.. image:: https://user-images.githubusercontent.com/1659467/97081308-9361b600-15cf-11eb-890d-585efb58e6aa.png
  :target: https://user-images.githubusercontent.com/1659467/97081308-9361b600-15cf-11eb-890d-585efb58e6aa.png

Accounts
--------
By default, you will be viewing Grafana as an anonymous user. If you want to make changes to the default Grafana dashboards, you will need to log into Grafana with username ``admin`` and the randomized password found via ``sudo salt-call pillar.get secrets``.

Configuration
-------------
Grafana configuration can be found in ``/opt/so/conf/grafana/etc/``. However, please keep in mind that most configuration is managed with :ref:`salt`, so if you manually make any modifications in ``/opt/so/conf/grafana/etc/``, they may be overwritten at the next salt update.
The default configuration options can be seen in ``/opt/so/saltstack/default/salt/grafana/defaults.yaml``. Any options not specified in here, will use the Grafana default. 

.. Example::
If you want to configure and enable SMTP for Grafana, place the following in the ``global.sls`` file. 
If you have files referenced in the config file, those can be placed in ``/opt/so/saltstack/default/salt/grafana/etc/files/``.
Those files will be then be placed in ``/opt/so/conf/grafana/etc/files`` on the minion and mapped to ``/etc/grafana/config/files/`` within the container.

::

  grafana:
    config:
      smtp:
        enabled: true
        host: smtphost.mydomain:25
        user: myuser
        # If the password contains # or ; you have to wrap it with triple quotes wrapped by single quotes. Ex '"""#password;"""'
        password: mypassword
  #      cert_file: /etc/grafana/config/files/smtp_cert_file.crt
  #      key_file: /etc/grafana/config/files/smtp_key_file.key
  #      skip_verify: false
        from_address: admin@grafana.localhost
        from_name: Grafana
  #      ehlo_identity: dashboard.example.com

More Information
----------------

.. seealso::

  For more information about Grafana, please see https://grafana.com/.
