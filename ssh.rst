.. _ssh:

SSH
===

Security Onion uses the latest SSH packages. It does not modify the default SSH configuration in ``/etc/ssh/sshd_config`` or manage it in any way with :ref:`salt`. You are free to add any PAM modules or enable two factor authentication (2FA) of your choosing. 

For distributed deployments, nodes only connect to the manager via SSH when they initially join the grid. If you enable 2FA, you will need to disable 2FA for the ``soremote`` account. The ``soremote`` account can be disabled when you are not adding any nodes to the grid.

Some organizations require the removal of certain ciphers from sshd. An easy way to do this is by running the following command and restarting sshd:

::

  sshd -T | grep ciphers | sed -e "s/\(3des-cbc\|aes128-cbc\|aes192-cbc\|aes256-cbc\|arcfour\|arcfour128\|arcfour256\|blowfish-cbc\|cast128-cbc\|rijndael-cbc@lysator.liu.se\)\,\?//g" >> /etc/ssh/sshd_config

