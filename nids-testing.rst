.. _nids-testing:

NIDS Testing
============

testmynids.org
--------------

The easiest way to test that our NIDS is working as expected might be to simply access http://testmynids.org/uid/index.html from a machine that is being monitored by Security Onion. You can do so via the command line using ``curl``:

::
   
   curl testmynids.org/uid/index.html

tmNIDS
------

Alternatively, you could also test for additional hits with a utility called ``tmNIDS``, running the tool in interactive mode:

::

   curl -sSL https://raw.githubusercontent.com/0xtf/testmynids.org/master/tmNIDS -o /tmp/tmNIDS && chmod +x /tmp/tmNIDS && /tmp/tmNIDS
    
If everything is working correctly, you should see a corresponding alert (``GPL ATTACK_RESPONSE id check returned root``) in :ref:`alerts`, :ref:`dashboards`, :ref:`hunt`, or :ref:`kibana`.

If you do not see this alert, try checking to see if the rule is enabled by going to :ref:`detections` and searching for the SID of the rule which is `2100498`. One way to search for this rule is to specify it in the URL as follows:

https://YourSecurityOnionHostHere.example.com/#/detections?q=2100498

so-test
-------

You can also test using :ref:`so-test`.
