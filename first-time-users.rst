.. _first-time-users:

First Time Users
================

Welcome first time users! You're going to be peeling back the layers of your network in just a few minutes! 

First, download our ISO image as shown in the :ref:`download` section. Then install the ISO image as shown below (also see the :ref:`installation` and :ref:`configuration` sections). This can be done in a minimal virtual machine with as little as 4GB RAM, 2 CPU cores, and 200GB of storage. For more information about virtualization, please see the :ref:`vmware`, :ref:`virtualbox`, and :ref:`proxmox` sections. (Once you're comfortable with your IMPORT installation, then you can move on to more advanced installations as shown in the :ref:`architecture` section.)

After booting the ISO image, the boot menu appears:

.. image:: images/01_grub.png
  :target: _images/01_grub.png

When prompted, specify your username and password:

.. image:: images/02_initial_install.png
  :target: _images/02_initial_install.png

Once installation is complete, you are prompted to reboot:

.. image:: images/03_initial_install_finished.png
  :target: _images/03_initial_install_finished.png

After rebooting, login using the username and password that you specified and then Setup will start automatically:

.. image:: images/04_setup_init.png
  :target: _images/04_setup_init.png

Perform a standard installation:

.. image:: images/05_setup_option.png
  :target: _images/05_setup_option.png

When prompted for installation type, select IMPORT:

.. image:: images/06_setup_type.png
  :target: _images/06_setup_type.png

If your Security Onion machine has full Internet access as described in the :ref:`firewall` section, select Standard. Otherwise, select :ref:`airgap`:

.. image:: images/06_setup_airgap.png
  :target: _images/06_setup_airgap.png

Review the license and agree:

.. image:: images/07_setup_license.png
  :target: _images/07_setup_license.png

Set the hostname:

.. image:: images/08_setup_hostname.png
  :target: _images/08_setup_hostname.png

If you use the default hostname of ``securityonion``, you will see a warning:

.. image:: images/09_setup_hostname_conflict.png
  :target: _images/09_setup_hostname_conflict.png

Select your management interface:

.. image:: images/10_setup_mn_nic.png
  :target: _images/10_setup_mn_nic.png

Select static IP addressing (recommended) or DHCP:

.. image:: images/11_setup_mn_int.png
  :target: _images/11_setup_mn_int.png

Specify IP address and CIDR mask:

.. image:: images/12_setup_cidr.png
  :target: _images/12_setup_cidr.png

Set gateway address:

.. image:: images/13_setup_gateway.png
  :target: _images/13_setup_gateway.png

Enter DNS servers:

.. image:: images/14_setup_dns_servers.png
  :target: _images/14_setup_dns_servers.png

Configure DNS search domain:

.. image:: images/15_setup_dns_domain.png
  :target: _images/15_setup_dns_domain.png

If necessary, you can change the default Docker IP range:

.. image:: images/16_setup_docker_range.png
  :target: _images/16_setup_docker_range.png

If you are connected to the Internet, select whether it is direct or via proxy:

.. image:: images/18_setup_direct_proxy.png
  :target: _images/18_setup_direct_proxy.png

Create username for :ref:`soc`:

.. image:: images/20_setup_webuser.png
  :target: _images/20_setup_webuser.png

Set password for :ref:`soc`:

.. image:: images/21_setup_webpass1.png
  :target: _images/21_setup_webpass1.png

Confirm password for :ref:`soc`:

.. image:: images/22_setup_webpass2.png
  :target: _images/22_setup_webpass2.png

Select how to access :ref:`soc`:

.. image:: images/23_setup_access_type.png
  :target: _images/23_setup_access_type.png

Allow connections through the host-based firewall if necessary:

.. image:: images/26_setup_so_allow.png
  :target: _images/26_setup_so_allow.png

Specify an IP address or range to allow through the host-based firewall:

.. image:: images/27_setup_so_allow_input.png
  :target: _images/27_setup_so_allow_input.png

Confirm all options:

.. image:: images/28_setup_summary.png
  :target: _images/28_setup_summary.png

Setup complete:

.. image:: images/29_setup_finished.png
  :target: _images/29_setup_finished.png

Login to :ref:`soc`:

.. image:: images/37_login.png
  :target: _images/37_login.png

After logging in, you will see the :ref:`soc` Overview page:

.. image:: images/38_overview.png
  :target: _images/38_overview.png

Check :ref:`grid` to verify all services are running properly:

.. image:: images/39_grid.png
  :target: _images/39_grid.png

While on the :ref:`grid` page, you can upload a PCAP or EVTX file:

.. image:: images/40_upload.png
  :target: _images/40_upload.png

Review alerts on the :ref:`alerts` page:

.. image:: images/50_alerts.png
  :target: _images/50_alerts.png

Review other logs on the :ref:`dashboards` page:

.. image:: images/51_dashboards.png
  :target: _images/51_dashboards.png

If you find something interesting on the :ref:`alerts` or :ref:`dashboards` pages, you may want to use the Correlate or Hunt actions to find related logs on the :ref:`hunt` page:

.. image:: images/52_hunt.png
  :target: _images/52_hunt.png

If you find interesting network traffic, you can pivot to full packet capture via the :ref:`pcap` action:

.. image:: images/53_pcap.png
  :target: _images/53_pcap.png

You can change the view to ASCII transcript for a more human readable view of the traffic:

.. image:: images/54_pcap_details.png
  :target: _images/54_pcap_details.png

If you find an interesting artifact, you can send it to :ref:`cyberchef`:

.. image:: images/55_cyberchef.png
  :target: _images/55_cyberchef.png

If you need to refer back to previous PCAP jobs, you can find them on the :ref:`pcap` page:

.. image:: images/56_jobs.png
  :target: _images/56_jobs.png

IMPORT installations do not support remote agents, but if you were running another installation type you could download the Elastic Agent installer from :ref:`downloads`:

.. image:: images/58_downloads.png
  :target: _images/58_downloads.png

The :ref:`administration` section allows to you manage user accounts:

.. image:: images/59_users.png
  :target: _images/59_users.png

It also allows you to manage grid members:

.. image:: images/60_gridmembers.png
  :target: _images/60_gridmembers.png

The :ref:`administration` section also allows you to configure various aspects of the system:

.. image:: images/61_config.png
  :target: _images/61_config.png

It also allows you to upload a license key for additional enterprise features:

.. image:: images/62_licensekey.png
  :target: _images/62_licensekey.png

All this in a minimal VM with only 4GB RAM!

.. image:: images/99_top.png
  :target: _images/99_top.png
