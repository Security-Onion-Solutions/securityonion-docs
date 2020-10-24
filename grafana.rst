.. _grafana:

Grafana
=======

Once you've logged into :ref:`soc`, you can then click the Grafana link to see system health information. 

.. image:: https://user-images.githubusercontent.com/1659467/87230207-57864600-c37c-11ea-98a2-e9a4d4494c3a.png
  :target: https://user-images.githubusercontent.com/1659467/87230207-57864600-c37c-11ea-98a2-e9a4d4494c3a.png

On a distributed deployment, you will default to the manager dashboard. There are also dashboards for other node types. Once you've accessed the node dashboards, they should be added to `Recently viewed dashboards` which is accessible by simply clicking the Dashboards icon:

.. image:: https://user-images.githubusercontent.com/1659467/97081308-9361b600-15cf-11eb-890d-585efb58e6aa.png
  :target: https://user-images.githubusercontent.com/1659467/97081308-9361b600-15cf-11eb-890d-585efb58e6aa.png

By default, you will be viewing Grafana as an anonymous user. If you want to make changes to the default Grafana dashboards, you will need to log into Grafana with username ``admin`` and the randomized password found via ``sudo salt-call pillar.get secrets``.

Configuration
-------------
Grafana configuration can be found in ``/opt/so/conf/grafana/etc/``. However, please keep in mind that most configuration is managed with :ref:`salt`, so if you manually make any modifications in ``/opt/so/conf/grafana/etc/``, they may be overwritten at the next salt update.

More Information
----------------

.. seealso::

  For more information about Grafana, please see https://grafana.com/.
