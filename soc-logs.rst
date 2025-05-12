.. _soc-logs:

SOC Logs
========

Standard :ref:`soc` logs can be found at ``/opt/so/log/soc/``.

SOC Auth Logs
-------------

SOC auth is handled by Kratos and you can read more about that at https://github.com/ory/kratos. SOC auth logs can be found at ``/opt/so/log/kratos/``. Those logs are ingested into :ref:`elasticsearch` and available for searching in :ref:`dashboards`, :ref:`hunt`, and :ref:`kibana`. Both :ref:`dashboards` and :ref:`hunt` have pre-defined queries for SOC auth logs.
