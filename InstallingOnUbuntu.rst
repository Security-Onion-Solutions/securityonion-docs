Quick Evaluation on Ubuntu
==========================

If you want to quickly evaluate Security Onion on your preferred flavor of Ubuntu 16.04 64-bit (not using our ISO image), follow these steps:

#. First, check the `Hardware Requirements <Hardware>`__ page.
#. Download the ISO image for your preferred flavor of Ubuntu 16.04, verify the ISO image, and boot from it.
#. Follow the prompts in the installer. When prompted to ``encrypt home folder`` or ``encrypt partition`` option, **DO NOT** enable this feature. When asked about automatic updates, **DO NOT** enable automatic updates.
#. Reboot into your new installation.
#. Login using the username/password you specified during installation.
#. Verify that you have Internet connectivity. If necessary, configure your `proxy <Proxy>`__ settings.
#. Log back in (using ``ssh -X`` if you’re installing on Ubuntu Server or a headless distro).
#. Configure ``MySQL`` not to prompt for root password (Setup will generate a random password later):

 ::

   echo "debconf debconf/frontend select noninteractive" | sudo debconf-set-selections
   
#. Clean apt list repository:

 ::

   sudo rm -rf /var/lib/apt/lists/*
   
#. Update package list:

 ::

   sudo apt-get update
   
#. Install software-properties-common if necessary:

 ::

   sudo apt-get -y install software-properties-common
   
#. Add the Security Onion stable repository:

 ::

   sudo add-apt-repository -y ppa:securityonion/stable
   
#. Update package list:

 ::

   sudo apt-get update
   
#. Install the securityonion-all metapackage:

 ::

   sudo apt-get -y install securityonion-all syslog-ng-core
   
#. Run the Setup wizard:

 ::

   sudo sosetup
   
   If you're using Ubuntu Server (no GUI), then you will need to forward X for this to work:
   https://groups.google.com/d/msg/security-onion/ceamp2XztVI/ECPOjaIqBwAJ)
   
#. Follow the prompts.

#. Analyze alerts using the `<Sguil>`_ client, or open a browser to https://localhost where you can access `<Squert>`__ and `<Kibana>`_.

Please review the `PostInstallation <PostInstallation>`__ page.
