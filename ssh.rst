.. _ssh:

SSH
===

Security Onion uses the latest SSH packages. It does not modify the default SSH configuration in ``/etc/ssh/sshd_config`` or manage it in any way with :ref:`salt`. If you receive a vulnerability scan with findings related to ssh config, you can modify ``/etc/ssh/sshd_config`` and restart sshd.
