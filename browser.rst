Browser
=======

Many of our analyst tools are browser-based.  Our Security Onion ISO image includes the Chromium browser.  We recommend chromium-based browsers (this includes Google Chrome).  Other browsers may work, but we recommend chromium-based browsers for best compatibility.

Mac OS X Catalina
-----------------

If you try to connect to Security Onion from Google Chrome on Mac OS X Catalina, you may get a NET::ERR_CERT_REVOKED error.  This is because Catalina is enforcing new SSL certificate standards.  Here are a few possible workarounds:

- Click into the page, blindly type ``thisisunsafe``, and then accept the certificate.

- Try a different browser like Safari.

- Replace the default Ubuntu SSL certificate with one that meets Catalina's requirements.
