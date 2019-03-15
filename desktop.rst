Disabling Desktop
=================

You can disable the GUI after the system is fully configured:

::

   sudo sed -i.bak 's|GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"|GRUB_CMDLINE_LINUX_DEFAULT="text"|g' /etc/default/grub
   sudo update-grub
   sudo systemctl enable multi-user.target --force
   sudo systemctl set-default multi-user.target
   sudo reboot

| For more information, please see:
| http://askubuntu.com/questions/16371/how-do-i-disable-x-at-boot-time-so-that-the-system-boots-in-text-mode
