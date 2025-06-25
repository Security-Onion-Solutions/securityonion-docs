.. _console:

Console
=======

The current version of Security Onion automatically disables kernel messages in the local console (tty). If you are running an older version of Security Onion and log into the local console, you may see lots of messages from the Linux kernel. To avoid these kernel messages, you have a few options:

- You can use :ref:`ssh` instead of the local console.
- If you really need to use the local console, you can temporarily disable console messages with ``sudo dmesg -D``. For more information about dmesg, please see https://man7.org/linux/man-pages/man1/dmesg.1.html. Also see https://man7.org/linux/man-pages/man8/sysctl.8.html and https://www.kernel.org/doc/html/next/core-api/printk-basics.html.
- Upgrade to the latest version of Security Onion using :ref:`soup`.
