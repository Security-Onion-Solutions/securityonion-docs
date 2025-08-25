.. _aqm:

Active Query Management
=======================

.. note::

    This is an enterprise-level feature of Security Onion. Contact Security Onion Solutions, LLC via our website at https://securityonion.com/pro for more information about purchasing a Security Onion Pro license to enable this feature.

Starting in version 2.4.130, Security Onion Pro customers can now view and cancel long-running Elasticsearch queries.

This screen is located under the Administration menu on the left side of the Security Onion Console. This menu option will only be visible for users having the ``superuser`` role.

Viewing Active Queries
----------------------

By default, the active query list will filter out internal, non-cancelable, and child queries. Therefore, in most
situations it will be normal for the list to be empty. If there is a desire to view all active queries without
any filtering the superuser can click the Options bar at the top of the screen and it will expand to show a filter slider that 
can be toggled off. Note that the query to show this list will be shown in the active query list. However, by the time the list 
is rendered on the screen that query will have already finished.

While it would be great to show the user that initiated the query on this active query list, unfortunately Elasticsearch does not
provide this information.

.. note::

    Be aware that queries not initiated by a user can appear in the filtered list. The filter only filters out a specific type of
    query that are always known to be internally initiated.

Canceling Active Queries
-------------------------

Sometimes a poorly written query or an indexing problem can result in a query running for an abnormally long time. This long-running
query can adversely affect other analysts' Security Onion experience, since their queries will begin performing slower than usual.
If a long-running query needs to be stopped the superuser can click the X icon at the right side of the active query listing. A popup
will appear asking for confirmation.

Canceling queries can take several seconds. Consequently, refreshing the active queries may still show that query in the list for 
a short time. 

.. note::

    Not all queries are cancelable. If a query cannot be canceled then no cancel icon will appear next to that query listing.

.. warning::

    Canceling internal, system queries can disrupt the Elasticsearch internal processes. Avoid canceling queries that are not
    confirmed to be user-created.