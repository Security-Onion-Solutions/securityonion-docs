Introduction
============

We can easily pull in `Alienvault OTX <https://otx.alienvault.com>`__
pulses into Security Onion and have Bro utilize them for the `Intel
Framework <https://www.bro.org/sphinx-git/frameworks/intel.html>`__ by
leveraging `Stephen Hosom <https://github.com/hosom/bro-otx>`__'s work
with Alienvault OTX integration.

Warning
=======

Please keep in mind we do not officially support use of this script, so
installation is at your own risk.

Installation
============

In order to do begin, we will need to make sure we satisfy a few
prerequisites:

| **Alienvault OTX API key** - can be obtained for free at:
  https://otx.alienvault.com
| **Security Onion standalone/sensor** (running Bro)
| **External internet access** - to retrieve updated pulses
  (https://otx.alienvault.com/api/v1/pulses/subscribed)

**Grab the installation script and run it.**

``wget https://raw.githubusercontent.com/weslambert/securityonion-otx/master/securityonion-otx``

``sudo bash securityonion-otx``

| **Test it**
| After using the above script, ``/opt/bro/share/bro/policy/bro-otx``
  will house all necessary files, etc (including ``otx.dat``, the intel
  file where all pulses will be fed).

We can test our configuration by adding another piece of intel to the
end of ``/opt/bro/share/bro/policy/bro-otx/otx.dat``.

| Ex:
| ``google.com[literal tab]Intel::DOMAIN[literal tab]Test-Google-Intel[literal tab]https://google.com[literal tab]T``

As long as our syntax is correct, we should not need to restart Bro. We
can check for errors in ``/nsm/bro/logs/current/reporter.log``.

| Let's see if we can get an intel hit by doing the following:
| ``curl google.com``

| Next, we need to check ``/nsm/bro/logs/current/intel.log`` for entries
  in regard to our indicator:
| ``grep google /nsm/bro/logs/current/intel.log``

| We should have received a Bro Notice as well, so lets check that as
  well:
| ``grep google /nsm/bro/logs/current/notice.log``

| After successful testing, we can remove our addition from
  ``/opt/bro/share/bro/policy/bro-otx/otx.dat``
| or just run ``/opt/bro/share/bro/policy/bro-otx/bro-otx.py`` again.

| **Change it**
| By default, pulses will be retrieved on an hourly basis. To change
  this to a different value, simply alter the interval in
  ``/etc/cron.d/bro-otx``.
