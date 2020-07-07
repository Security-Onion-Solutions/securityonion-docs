.. _osquery:

osquery
=======

From https://osquery.io/:

    Osquery uses basic SQL commands to leverage a relational data-model to describe a device.
      
Fleet
-----

We include Fleet to manage your osquery deployment. For more information, please see the :ref:`fleet` section.

Kibana
------

All osquery logs can be found by using the following query: ``event_type: osquery``

Dashboard: Osquery - Overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This dashboard gives an overview of the osquery logs. It should work out of the box no matter how you schedule or name your queries & packs as long as the osquery configuration (from the prereq) is used.

Dashboard: Osquery - Chrome Extensions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This dashboard gives an idea of how to visualize osquery data - in this example, Chrome Extensions. This dashboard is not linked on the navigation page but can be found at https://MASTERSERVER/kibana/blah . For this dashboard to work the following query should be scheduled (it's a bit longer because it filters out common benign Chrome extensions). Also, the query name should include the word chrome somewhere in it.
 
    SELECT users.username,chrome_extensions.*,chrome_extensions.path FROM users CROSS JOIN chrome_extensions USING (uid) where identifier not in ('aapocclcgogkmnckokdopfmhonfmgoek','aohghmighlieiainnegkcijnfilokake', 'apdfllckaahabafndbhieahigkjlhalf','felcaaldnbdncclmgdcncolpebgiejap','pjkljhegncpnkpknbcohdijeoejaedia','pkedcjkdefgpdelpbcmbmeomcjbeemfm','blpcfgokakmgnkcojhhkbfbldkacnbeo','ghbmnnjooekpmoecnnnilnnbdlolhkhi','nmmhkkegccagdldgiimedpiccmgmieda');

Community ID
------------

We sponsored the development of Community ID support for osquery:

https://dactiv.llc/blog/correlate-osquery-network-connections/

More Information
----------------

For more information about osquery, please see https://osquery.io/.
