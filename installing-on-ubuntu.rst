Quick Evaluation on Ubuntu
==========================

If you want to quickly evaluate Security Onion on your preferred flavor of Ubuntu 16.04 64-bit (not using our ISO image), follow these steps:

- Review the `Hardware Requirements <Hardware>`__ page.
- Download the ISO image for your preferred flavor of Ubuntu 16.04 64-bit, verify the ISO image, and boot from it.
- Follow the prompts in the installer. If prompted to ``encrypt home folder`` or ``encrypt partition``, **DO NOT** enable either of these. When asked about automatic updates, **DO NOT** enable automatic updates.
- Reboot into your new installation.
- Login using the username/password you specified during installation.
- Verify that you have Internet connectivity. If necessary, configure your `proxy <Proxy>`__ settings.
- Log back in (using ``ssh -X`` if you’re installing on Ubuntu Server or a headless distro).
- Configure ``MySQL`` not to prompt for root password (Setup will generate a random password later):

  ::

    echo "debconf debconf/frontend select noninteractive" | sudo debconf-set-selections
   
- Clean apt list repository:

  ::

    sudo rm -rf /var/lib/apt/lists/*
   
- Update package list:

  ::

    sudo apt-get update
   
- Install software-properties-common if necessary:

  ::

    sudo apt-get -y install software-properties-common
   
- Add the Security Onion stable repository:

  ::

    sudo add-apt-repository -y ppa:securityonion/stable
   
- Update package list:

  ::

    sudo apt-get update
   
- Install the securityonion-all metapackage:

  ::

    sudo apt-get -y install securityonion-all syslog-ng-core
   
- Run the Setup wizard (if you're using Ubuntu Server with no GUI and are doing this over SSH, you will need to forward X for this to work):

  ::

    sudo sosetup
   
- Follow the prompts in the Setup wizard.

- Once Setup is complete, review alerts and logs using `<Sguil>`_, `<Squert>`__, and `<Kibana>`_.

- Review the `PostInstallation <PostInstallation>`__ page.
