.. _fir:

FIR
===

From: https://github.com/certsocietegenerale/FIR:

    FIR (Fast Incident Response) is an cybersecurity incident management
    platform designed with agility and speed in mind. It >allows for
    easy creation, tracking, and reporting of cybersecurity incidents.

    FIR is for anyone needing to track cybersecurity incidents (CSIRTs,
    CERTs, SOCs, etc.). It's was tailored to suit our >needs >and our
    team's habits, but we put a great deal of effort into making it as
    generic as possible before releasing it >so that >other teams around
    the world may also use it and customize it as they see fit.

We can add FIR to Security Onion as a Docker container to enhance its current capabilities and leverage the great work from the folks at `CERT Societe Generale <https://github.com/certsocietegenerale>`__.

.. warning::

    Please keep in mind we do not officially support FIR, so installation is at your own risk.

Installation
------------

To install FIR on Security Onion, use the following steps.

Get the install script:

::

   wget https://raw.githubusercontent.com/weslambert/securityonion-fir/master/install_fir

Run the script:

::

   sudo bash ./install_fir

Follow the prompts, and once finished, you should be able to navigate to FIR via ``https://domain.you.specified``. (Note this address in also referenced in ``/etc/apache2/sites-available/fir.conf``.)

Keep in mind, FIR is still accessible at ``http://localhost:8001``, so you will want to make sure only port 443 is allowed externally, or alter your web server settings appropriately.

Also note, to access FIR by the above name you will need to:

-  configure a hosts file on your local host
   or
-  create a DNS record pointing to it.

| For more information on the FIR, see here:
| https://github.com/certsocietegenerale/FIR
