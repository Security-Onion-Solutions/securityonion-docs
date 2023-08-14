.. _console:

Console
=======

When you log into the local bash console (tty1), you may see lots of messages from the Linux kernel. To avoid these kernel messages, you have a few options:

- You can use :ref:`ssh` instead of the local bash console.
- If you really need to use the local console, you can temporarily disable console messages with ``dmesg -D``. For more information about dmesg, please see https://man7.org/linux/man-pages/man1/dmesg.1.html. Also see https://man7.org/linux/man-pages/man8/sysctl.8.html and https://www.kernel.org/doc/html/next/core-api/printk-basics.html.
