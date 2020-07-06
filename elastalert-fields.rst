.. _elastalert-fields:

Elastalert Fields
=================

The following lists field names as they are formatted in Elasticsearch.
Elastalert provides its own template to use for mapping into Elastalert,
so we do not current utilize a config file to parse data from
Elastalert.

``index:*:elastalert_status``

| alert\_info.type
| alert\_sent
| alert\_time
| endtime
| hist
| matches
| match\_body.@timestamp
| match\_body.num\_hits
| match\_body.num\_matches
| rule\_name
| starttime
| time\_taken
