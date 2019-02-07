Analyst VM
==========

Full-time analysts should install Security Onion in a VM on their
workstation. Run through the Ubuntu installer, but you do not need to
run our Setup wizard since the analyst VM won't be sniffing any live
traffic. This gives you a local copy of Wireshark, NetworkMiner, and our
customized Sguil client. Launch the Sguil client and connect to the
IP/hostname of your production Sguil server (you may need to run
so-allow on the server to allow you to connect). This allows you to
investigate pcaps without fear of impacting your production
server/sensors.

Screen Resolution
-----------------

To change the resolution of your Security Onion VM:

-  click the menu in the upper left corner
-  click Setttings
-  click Display
-  choose your desired resolution

If you prefer a CLI method for changing screen resolution, you can use
xrandr. For a list of available screen resolutions, simply execute
``xrandr``. To set the screen resolution (replace W and H with the
actual Width and Height desired):

::

    xrandr -s WxH

If you have limited screen resolution options, you may need to install
the Virtual Tools for your virtualization solution. For example, this
can happen if you're running VirtualBox and you'll need to install the
VirtualBox Extensions.

Ultimate Forensics VM
---------------------

| Want an analyst VM that also includes forensics and reverse
  engineering tools from SANS SIFT and Remnux? See Brian Kellogg's
  Ultimate Forensics VM:
| https://github.com/theflakes/Ultimate-Forensics-VM
