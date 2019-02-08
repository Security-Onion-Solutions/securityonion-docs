Elastic Stack
=============

We've completed our initial integration of the Elastic Stack
(`Elasticsearch <Elasticsearch>`__, `Logstash <Logstash>`__, and
`Kibana <Kibana>`__)!

In addition, we've added the following:

| `Curator <Curator>`__
| `DomainStats <DomainStats>`__
| `ElastAlert <ElastAlert>`__
| `FreqServer <FreqServer>`__

Each component has its own `Docker <Docker>`__ image.

You can get an idea of what this whole integration might look like at a
high-level by viewing our `proposed architecture
diagram <Elastic-Architecture>`__.

Blog Posts
----------

| General Availability:
| https://blog.securityonion.net/2018/04/security-onion-elastic-stack-general.html

| Release Candidate 4:
| https://blog.securityonion.net/2018/03/security-onion-elastic-stack-release_28.html

| Release Candidate 3:
| https://blog.securityonion.net/2018/03/security-onion-elastic-stack-release.html

| Release Candidate 2:
| https://blog.securityonion.net/2018/02/security-onion-elastic-stack-release.html

| Release Candidate 1:
| https://blog.securityonion.net/2018/01/security-onion-elastic-stack-release.html

| Beta 3 Release:
| https://blog.securityonion.net/2017/12/security-onion-elastic-stack-beta-3.html

| Beta 2 Release:
| https://blog.securityonion.net/2017/11/elastic-stack-beta-2-release-and.html

| Beta Release:
| https://blog.securityonion.net/2017/11/elastic-stack-beta-release-and-security.html

| Alpha Release:
| https://blog.securityonion.net/2017/09/elastic-stack-alpha-release-and.html

| Technology Preview 3:
| https://blog.securityonion.net/2017/07/towards-elastic-on-security-onion.html

| Technology Preview 2:
| https://blog.securityonion.net/2017/06/towards-elastic-on-security-onion.html

| Technology Preview 1:
| https://blog.securityonion.net/2017/03/towards-elk-on-security-onion.html

Videos
------

`Doug Burks - State of the
Onion <https://www.youtube.com/watch?v=N1jmk7L4jj0&index=7&list=PLljFlTO9rB15jhnSfR6shBEskTgGbta2k>`__

Hardware Requirements
---------------------

Please note the following MINIMUM requirements for the Elastic stack:

-  2 CPU cores
-  8GB RAM

Installation
------------

| The easiest way to try the new Elastic integration is using our
  14.04.5.11 (or newer) ISO image:
| https://blog.securityonion.net/2018/04/security-onion-elastic-stack-general.html

Alternatively, if you have an existing TEST installation or if you want
to install using an ISO image other than our 14.04.5.11 (or newer), you
can install the ``securityonion-elastic`` package and then run
``so-elastic-download`` as follows:

::

    sudo soup
    sudo apt install securityonion-elastic
    sudo so-elastic-download

If this is a fresh installation where you haven't run Setup yet, then
you can run sosetup:

::

    sudo sosetup

If you would like to install on your own preferred flavor of Ubuntu
14.04, you can follow steps 1-11 here:

`<InstallingOnUbuntu>`__

Then run:

::

    sudo apt install securityonion-elastic 
    sudo so-elastic-download 
    sudo sosetup

Upgrading from ELSA to Elastic
------------------------------

For best results, we recommend performing a fresh installation, but if
you really need to do an in-place upgrade from ELSA to Elastic, you can
try the steps on the `ELSA-to-Elastic <ELSA-to-Elastic>`__ page.
