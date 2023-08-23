.. _os:

Operating System
================

For most use cases, we recommend using our Security Onion ISO image which is based on Oracle Linux 9:
https://blog.securityonion.net/2023/07/security-onion-24-base-os.html

If you don’t want to use our Security Onion 2.4 ISO image, you can still perform a network installation of our Security Onion components after manually installing one of the following:

- Oracle Linux 9
- Rocky Linux 9
- Alma Linux 9
- CentOS Stream 9
- RHEL 9
- Ubuntu 22.04
- Debian 12

Support
-------

Supported
~~~~~~~~~

Our Security Onion 2.4 ISO image (based on Oracle Linux 9) is the only fully supported installation method. Choose this option if any of the following apply to you:

- You are deploying in an enterprise environment.
- You are deploying in an airgap environment.
- You are performing a distributed deployment.
- You want the quickest and easiest installation with the fewest issues.
- You need full support.

Unsupported
~~~~~~~~~~~

If you don’t want to use our Security Onion 2.4 ISO image and choose to perform a manual OS installation followed by a network installation of our Security Onion components, then we recommend using Oracle Linux 9 or Rocky Linux 9. CentOS Stream 9 or Alma Linux 9 should also work. Another option might be RHEL 9 itself although that is a paid option.

If you really want to run Ubuntu 22.04 or Debian 12, then please note that these distros may work but they get less testing and therefore you will be more likely to run into issues.

If you choose Ubuntu 22.04, we recommend the Ubuntu 22.04 Server ISO image and selecting the ``Ubuntu Server`` installation option as there are known issues when choosing the ``Ubuntu Server (minimized)`` option.
