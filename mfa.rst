.. _mfa:

MFA
===

You can enable Multi-Factor Authentication (MFA) to further protect your account. This can be enabled in :ref:`soc` by clicking the user icon in the upper-right corner, clicking ``Settings``, and then going to the ``Security`` tab. 

TOTP
----

Time-based One-Time Passwords (TOTP) can be activated on a user account. TOTP requires the use of an authenticator app. Currently only Google Authenticator has been tested, however other authenticator apps that implement the time-based one-time password (TOTP) specification could also work.

To require all users setup TOTP upon login, enable the ``Require TOTP`` configuration setting, located on the Configuration screen: ``soc > config > server > Require TOTP``.

.. warning::

  Please note that TOTP requires that both the Security Onion manager and the device supplying the TOTP code to have their system time set correctly. Otherwise, the TOTP code may be seen as invalid and rejected.

.. note::

  If you lose access to your authenticator app, an administrator can reset your password using the :ref:`administration` interface which will also remove the TOTP from your account.

Customizing the MFA Name
~~~~~~~~~~~~~~~~~~~~~~~~

If you utilize multiple Security Onion environments, such as one for testing and one for production, and both are setup with TOTP MFA, SOC users may have trouble distinguishing them in their authenticator app. There are two options for handling this situation:

1. Most authenticator apps allow the user to edit or rename the entry. For example, in Google Authenticator on Android, swiping right on the entry provides an Edit screen. This is useful if it's just affecting one or two users.
2. Edit the TOTP issuer via the SOC Configuration screen, specifically the ``kratos > config > selfservice > methods > totp > config > issuer`` setting. This should be done prior to enabling TOTP since it will not help users that already setup TOTP.

WebAuthn Security Keys
----------------------

WebAuthn allows the use of built-in mobile device biometric sensors, USB security devices, and other PKI-based security devices to authenticate users during the login process.

If the Security Onion installation has been configured to use security keys for MFA instead of passwordless logins then you can add one or more security keys to your account as a second authentication factor.

.. note::

  If you lose access to your security key device, an administrator can reset your password using the :ref:`administration` interface which will also remove the security keys from your account.

.. important::

   The webauthn specification requires that the web server be accessed via a hostname. Therefore, IP addresses cannot be used to access SOC when utilizing webauthn. Also, the server's TLS certificate must not have any errors. Consequently, self-signed certificates will only be permitted provided the certificate authority (CA) has also been imported into analyst's browsers and/or operating systems, and marked as trusted.
