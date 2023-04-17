.. _soc-logs:

SOC Logs
========

Standard :ref:`soc` logs can be found at ``/opt/so/log/soc/``.

SOC Auth Logs
-------------

SOC auth is handled by Kratos and you can read more about that at https://github.com/ory/kratos. SOC auth logs can be found at ``/opt/so/log/kratos/``. To look for successful SOC logins, you can run the following:

::

        sudo zgrep "Identity authenticated successfully and was issued an Ory Kratos Session Cookie" /opt/so/log/kratos/*

Those logs should be ingested into :ref:`elasticsearch` and available for searching in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. Both :ref:`dashboards` and :ref:`hunt` have pre-defined queries for SOC auth logs.

.. image:: images/soc-logins.png
  :target: _images/soc-logins.png

identity_id
~~~~~~~~~~~

Once you see the auth logs, you will notice that the login is logged as ``identity_id``. You can find your desired ``identity_id`` as follows, replacing USERNAME@DOMAIN.COM with your desired SOC username:

::

        echo "select * from identities;" | sudo sqlite3 /nsm/kratos/db/db.sqlite |grep USERNAME@DOMAIN.COM | cut -d\| -f1
