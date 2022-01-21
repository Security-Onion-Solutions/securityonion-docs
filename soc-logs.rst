.. _soc-logs:

SOC Logs
========

If you need to see SOC auth logs, you can run the following:

::

        sudo zgrep "Identity authenticated successfully and was issued an Ory Kratos Session Cookie" /opt/so/log/kratos/*

Once you see the auth logs, you will notice that Kratos logs using ``identity_id``. You can find your desired ``identity_id`` as follows, replacing USERNAME@DOMAIN.COM with your desired SOC username:

::

        echo "select * from identities;" | sudo sqlite3 /opt/so/conf/kratos/db/db.sqlite |grep USERNAME@DOMAIN.COM | cut -d\| -f1
