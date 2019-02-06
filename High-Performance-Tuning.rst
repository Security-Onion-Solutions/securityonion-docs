First, make sure you're following `Best Practices <Best-Practices>`__.

| **Tune Disk/Memory**:
| If you have plenty of RAM, disable swap altogether.

| Use ``hdparm`` to gather drive statistics and alter settings, as
  described here:
| http://www.linux-magazine.com/Online/Features/Tune-Your-Hard-Disk-with-hdparm

``vm.dirty_ratio`` is the maximum amount of system memory that can be
filled with dirty pages before everything must get committed to disk.

``vm.dirty_background_ratio`` is the percentage of system memory that
can be filled with “dirty” pages, or memory pages that still need to be
written to disk -- before the pdflush/flush/kdmflush background
processes kick in to write it to disk.

More information:
https://lonesysadmin.net/2013/12/22/better-linux-disk-caching-performance-vm-dirty_ratio/

| **Disable GUI**:
| http://askubuntu.com/questions/16371/how-do-i-disable-x-at-boot-time-so-that-the-system-boots-in-text-mode

**Disable Bluetooth**:

::

    sudo systemctl stop bluetooth.service
    sudo systemctl disable bluetooth.service

| **Other**
| Consider adopting some of the suggestions from here:
| https://github.com/pevma/SEPTun

https://github.com/pevma/SEPTun-Mark-II
