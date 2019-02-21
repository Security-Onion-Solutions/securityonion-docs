Analyst VM
==========

Full-time analysts should install Security Onion in a VM on their workstation. Run through the Ubuntu installer, but you do not need to run our Setup wizard since the analyst VM won't be sniffing any live traffic. This gives you a local copy of `Wireshark <wireshark>`_, `NetworkMiner <networkminer>`_, and our customized `<Sguil>`_ client. 

To connect from the Analyst VM to your production master server, you will need to run `<so-allow>`_ on the master server and choose the ``analyst`` option to allow the traffic through the host-based `firewall <Firewall>`_.

Once you’ve allowed the traffic using so-allow, you can launch the Sguil client and connect to the IP address or hostname of your production master server and/or launch the web browser and connect to Squert or Kibana on your production master server.

This allows you to investigate pcaps without fear of impacting your production server/sensors.

Screen Resolution
-----------------

To change the resolution of your Security Onion VM:

-  click the ``Applications`` menu in the upper left corner
-  click ``System Tools``
-  click ``Setttings``
-  click ``Displays``
-  select your display
-  choose your desired resolution
-  click ``Apply``

If you prefer a CLI method for changing screen resolution, you can use `xrandr`. For a list of available screen resolutions, simply execute ``xrandr``. To set the screen resolution (replace ``W`` and ``H`` with the actual Width and Height desired):

::

    xrandr -s WxH

If you have limited screen resolution options, you may need to install the Virtual Tools for your virtualization solution. For example, this can happen if you're running VirtualBox and you'll need to install the VirtualBox Extensions.

Ultimate Forensics VM
---------------------

| Want an analyst VM that also includes forensics and reverse engineering tools from SANS SIFT and Remnux? See Brian Kellogg's Ultimate Forensics VM:
| https://github.com/theflakes/Ultimate-Forensics-VM
