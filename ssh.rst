.. _ssh:

SSH
===

Security Onion uses the latest SSH packages. It does not manage the SSH configuration in ``/etc/ssh/sshd_config`` with :ref:`salt`. This allows you to add any PAM modules or enable two factor authentication (2FA) of your choosing. 

Distributed Deployments
-----------------------

For distributed deployments, nodes only connect to the manager via SSH when they initially join the grid. That initial connection is done using the ``soremote`` account. If you enable 2FA for SSH, you will need to disable 2FA for the ``soremote`` account. The ``soremote`` account can be disabled when you are not adding any nodes to the grid.

Hardening
---------

Some organizations require the removal of certain ciphers and algorithms from sshd. Starting in Security Onion 2.3.40, Setup will automatically do this for you by running ``so-ssh-harden``. Alternatively, you can manually run ``so-ssh-harden`` or manually modify your ``sshd_config`` as follows:

::

  sshd -T | grep "^ciphers" | sed -e "s/\(3des-cbc\|aes128-cbc\|aes192-cbc\|aes256-cbc\|arcfour\|arcfour128\|arcfour256\|blowfish-cbc\|cast128-cbc\|rijndael-cbc@lysator.liu.se\)\,\?//g" >> /etc/ssh/sshd_config
  sshd -T | grep "^kexalgorithms" | sed -e "s/\(diffie-hellman-group14-sha1\|ecdh-sha2-nistp256\|diffie-hellman-group-exchange-sha256\|diffie-hellman-group1-sha1\|diffie-hellman-group-exchange-sha1\|ecdh-sha2-nistp521\|ecdh-sha2-nistp384\)\,\?//g" >> /etc/ssh/sshd_config
  sshd -T | grep "^macs" | sed -e "s/\(hmac-sha2-512,\|umac-128@openssh.com,\|hmac-sha2-256,\|umac-64@openssh.com,\|hmac-sha1,\|hmac-sha1-etm@openssh.com,\|umac-64-etm@openssh.com,\|hmac-sha1\)//g" >> /etc/ssh/sshd_config
  sshd -T | grep "^hostkeyalgorithms" | sed "s|ecdsa-sha2-nistp256,||g" | sed "s|ssh-rsa,||g" >> /etc/ssh/sshd_config

.. warning::

  Any time you modify ``sshd_config``, there is a possibility of a syntax error preventing ssh from starting correctly which would then prevent you from accessing remotely. Please exercise caution in editing the file and have a backup method of accessing the box just in case.
