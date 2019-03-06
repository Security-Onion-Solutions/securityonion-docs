Resolution
----------

To change the resolution of your Security Onion installation:

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
