SSH
===

Changing the default ssh listening port
---------------------------------------

By default secure shell (ssh) listens on ``tcp port 22``. If you want to obfuscate it by changing the listening port from ``port 22`` to ``port 31337``, you can do so in the ``sshd_config`` file.

You can use your favorite text editor (e.g., ``vi``, ``gedit``, ``nano``, ``emacs``) to edit the ``sshd_conf`` file, but for the purpose of this example ``vi`` will be used.

::

    sudo vi /etc/ssh/sshd_conf

Change the port to 31337.  Then restart the ssh daemon so that it will now start listening on port ``31337``:

::

   sudo killall -HUP sshd 

Verify that ssh is listening on the new port:

::

   netstat -nltp | grep sshd

Allow the new ssh port in the firewall:

::

   sudo ufw allow 31337/tcp
