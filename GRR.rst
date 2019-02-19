GRR
===

From: https://github.com/google/grr

    GRR Rapid Response: remote live forensics for incident response

We can add GRR to Security Onion as a Docker container to enhance its current capabilities and leverage the great work from the folks at `Google <https://github.com/google/grr>`__.

Warning
-------

Please keep in mind we do not officially support GRR, so installation is at your own risk.

Installation
------------

To install GRR on Security Onion:

Get the install script:

::

   sudo wget https://raw.githubusercontent.com/weslambert/securityonion-grr/master/install_grr

Make the script executable:

::

   sudo chmod +x install_grr

Run the script:

::

   sudo ./install_grr

Follow the prompts, and once finished, you should be able to navigate to GRR via ``https://domain.you.specified``.  (Note this address in also referenced in ``/etc/apache2/sites-available/grr.conf``.)

Keep in mind, GRR is still accessible at ``http://localhost:8000``, so you will want to make sure only port 443 is allowed externally, or alter your web server settings appropriately.

Also note, to access GRR by the above name you will need to:

-  configure a hosts file on your local host
   OR
-  create a DNS record pointing to it.

Firewall Rules
--------------

Analyst/Web Interface:

::

   sudo so-allow
   
OR

::

   sudo ufw allow proto tcp from REMOTE_IP to any port 443

GRR Client IP:

::

   sudo iptables -I DOCKER-USER ! -i docker0 -o docker0 -s ClIENT_IP -p tcp --dport 8080 -j ACCEPT

Management
----------

| If you would like to add another user, aside from the default, you can follow the instructions here:
| https://github.com/google/grr-doc/blob/master/admin.adoc#user-management
|
| For more information on the GRR Docker image, see here:
| https://github.com/google/grr-doc/blob/master/docker.adoc
