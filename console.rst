.. _console:

Console
=======

When you log into the local bash console, you may see lots of kernel messages. To avoid these kernel messages, you have a few options:

- Kernel messages should only log to the first tty, so you should be able to switch to the second tty using Ctrl+Alt+F2 or whatever the equivalent is on your keyboard and OS combination.
- You can use :ref:`ssh` instead of the local bash console.
- You can change the default kernel logging level as described at https://www.kernel.org/doc/html/next/core-api/printk-basics.html. This can be done via sysctl (https://man7.org/linux/man-pages/man8/sysctl.8.html) or dmesg (https://man7.org/linux/man-pages/man1/dmesg.1.html).
