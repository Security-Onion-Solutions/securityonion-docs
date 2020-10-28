.. _ssh:

SSH
===

Security Onion uses the latest SSH packages. It does not modify the default SSH configuration in ``/etc/ssh/sshd_config`` or manage it in any way with :ref:`salt`. Users are free to add any PAM modules or enable 2FA of their choosing. Keep in mind SSH connectivity is only required when adding a new node and if you enable 2FA you need to disable that for the soremote account. This account can be disabled when you are not adding any nodes to the grid.

Some organizations require the removal of certain cyphers from sshd. An easy way to do this is by running to following command and restarting sshd:

``sshd -T | grep ciphers | sed -e "s/\(3des-cbc\|aes128-cbc\|aes192-cbc\|aes256-cbc\|arcfour\|arcfour128\|arcfour256\|blowfish-cbc\|cast128-cbc\|rijndael-cbc@lysator.liu.se\)\,\?//g" >> /etc/ssh/sshd_config``


