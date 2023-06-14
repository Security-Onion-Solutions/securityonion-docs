.. _mfa:

MFA
===

You can enable Multi-Factor Authentication (MFA) to further protect your account. This can be enabled in :ref:`soc` by clicking the user icon in the upper right corner, clicking ``Settings``, and then going to the ``Security`` tab. 

TOTP
----

Time-based One-Time Passwords (TOTP) can be activated on a user account. TOTP requires the use of an authenticator app. Currently only Google Authenticator has been tested, however other authenticator apps that implement the time-based one-time password (TOTP) specification could also work.

.. warning::

  Please note that TOTP requires that both the Security Onion manager and the device supplying the TOTP code to have their system time set correctly. Otherwise, the TOTP code may be seen as invalid and rejected.

.. note::

  If you have a user account on multiple Security Onion deployments with TOTP activated, they may be listed identically in your authenticator app. If so, you should be able to edit the listing in your authenticator app so that you can distinguish between them.

.. note::

  If you've lost access to your authenticator app, an administrator can change your password using the :ref:`administration` interface, which will also remove the TOTP from your account.

WebAuthn Security Keys
----------------------

WebAuthn allows the use of built-in mobile device biometric sensors, USB security devices, and other PKI-based security devices to authenticate users during the login process.

If the Security Onion installation has been configured to use security keys for MFA instead of passwordless logins then you can add one or more security keys to your account as a second authentication factor.

.. note::

  If you've lost access to your security key device, an administrator can change your password using the :ref:`administration` interface, which will also remove the security keys from your account.