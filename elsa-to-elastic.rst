ELSA to Elastic
===============

The Elastic Stack typically requires more CPU and more RAM than ELSA. In
addition, you will most likely want SSD storage for Elastic data if at
all possible. For best results, we recommend performing a fresh
installation on new hardware designed to meet these requirements. If
your ELSA hardware already meets these requirements and you really need
to perform an in-place upgrade from ELSA to Elastic, this page will
provide an overview of steps necessary.

.. warning::

   The in-place upgrade process is still considered EXPERIMENTAL and so the
   usual warnings and disclaimers apply:

   -  This is BLEEDING EDGE and TOTALLY UNSUPPORTED!
   -  If this breaks your system, you get to keep both pieces!
   -  This may result in nausea, vomiting, or a burning sensation.

Exporting Data from ELSA
------------------------

By default, this process does NOT export data from ELSA. If you need the
data that is in ELSA, there is an experimental script called
``so-elsa-export`` that can export data from ELSA to raw logs in the
filesystem. Before running this script, please check your disk space as
this will duplicate all your logs. Once exported, you may want to move
these logs off to a separate system for archival. They are standard
cleartext logs so you can use standard command line tools such as
``grep``, ``awk``, and ``sed`` to search through them if necessary.

Importing Data to Elastic
-------------------------

The export script provides information on how to import the data into
Elastic. However, please note the following caveats:

-  this creates yet another copy of the data and so it is essential that
   you have plenty of free space
-  Logstash only has parsers for the current version of Zeek, so older
   Zeek/Bro logs may not parse correctly

Upgrade Process
---------------

Standalone
~~~~~~~~~~

For a single standalone box that doesn't have any separate sensor boxes
connected to it:

Install all updates:

::

    sudo soup

Reboot:

::

    sudo reboot

Install and configure Elastic:

::

    sudo apt update
    sudo apt install securityonion-elastic
    sudo so-elastic-download
    sudo so-elastic-configure

Distributed Deployment
~~~~~~~~~~~~~~~~~~~~~~

For distributed deployments consisting of a master server and one or
more sensor boxes, start the upgrade process with the master server.
Once the master server has been fully converted to the Elastic Stack,
then start updating sensors one at a time.

Master Server
~~~~~~~~~~~~~

Before initiating the upgrade process on the master server, run sostat:

::

    sudo sostat

At the very end of the sostat output, look for the section entitled
"ELSA Log Node SSH Tunnels". Save the information in this section as you
will need it later in this procedure.

Install all updates:

::

    sudo soup

Reboot:

::

    sudo reboot

Install and configure Elastic:

::

    sudo apt update
    sudo apt install securityonion-elastic
    sudo so-elastic-download
    sudo so-elastic-configure

For each sensor ssh account, add lines to ``/etc/ssh/sshd_config`` like
the following (replacing ``$SSH_USERNAME`` with the actual sensor ssh
account):

::

    Match User $SSH_USERNAME
       GatewayPorts clientspecified

Restart ``sshd``:

::

    sudo service ssh restart

Sensors
~~~~~~~

Perform the following steps on each sensor box, one at a time (finish
the first sensor before starting the second sensor, etc.).

Install all updates:

::

    sudo soup

Reboot:

::

    sudo reboot

Install and configure Elastic:

::

    sudo apt update
    sudo apt install securityonion-elastic
    sudo so-elastic-download
    echo "KIBANA_ENABLED=no" | sudo tee -a /etc/nsm/securityonion.conf
    echo "ELASTALERT_ENABLED=no" | sudo tee -a /etc/nsm/securityonion.conf
    sudo so-elastic-configure
    sudo so-autossh-restart

Check to make sure the old ELSA autossh tunnel is not still running --
if it is, it could cause problems starting our new one for
Elasticsearch:

``ps aux | grep autossh``

If you see something like the following, you'll need to kill it and run
``so-autossh-start`` again:

::

  4356  0.0  0.0   4356    92 ?        Ss   18:26   0:00 /usr/lib/autossh/autossh -M 0    -q -N -o ServerAliveInterval 60 -o ServerAliveCountMax 3 -i /root/.ssh/securityonion -L 3306:127.0.0.1:3306 -R 50000:localhost:3154 sensor@192.168.1.3

  sudo kill -9 4356
  ps aux | grep autossh (verify no process)
  sudo so-autossh-start

Checking again with ``ps aux | grep autossh``, we see the correct
connection information:

::

  17707  0.0  0.0   4356    92 ?        Ss   18:50   0:00 /usr/lib/autossh/autossh -M 0    -q -N -o ServerAliveInterval 60 -o ServerAliveCountMax 3 -i /root/.ssh/securityonion -R 172.18.0.1:50000:localhost:9300 sensor@192.168.1.3

Next we'll want to check to make sure ``$REVERSE_PORT`` was correctly
set in ``/root/.ssh/securityonion_ssh.conf``:

::

  sudo cat /root/.ssh/securityonion_ssh.conf

We should get something like the following:

``SSH_USERNAME=sensor SERVERNAME=192.168.1.3 REVERSE_PORT=50000``

Next, we'll manually add transport settings to
``/etc/elasticsearch/elasticsearch.yml`` (replacing ``$REVERSE_PORT``
with the actual reverse port):

::

    transport.bind_host: 0.0.0.0
    transport.publish_host: 172.18.0.1
    transport.publish_port: $REVERSE_PORT.

``transport.publish_host`` should ALWAYS be set to ``172.18.0.1``

Restart Elasticsearch:

::

    sudo docker restart so-elasticsearch

Back to the master server
~~~~~~~~~~~~~~~~~~~~~~~~~

Next, we'll need to add the correct information for UFW and
Elasticsearch so that we can query the sensor's Elasticsearch instance
via Cross Cluster Search:

For each sensor, add a firewall rule (replacing ``5000X`` with the
actual reverse port):

::

    sudo ufw allow proto tcp from 172.18.0.0/24 to 172.18.0.1 port 5000X

Log into Kibana, click Dev Tools, paste the following, and then click
the green triangle to send the request:

::

    GET _cluster/settings

The output pane on the right will then display ``_cluster/settings``
which will list the master server and any remote nodes.

If any of your hostnames have capital letters, you'll want to lowercase
those letters when adding these settings, given that our new standard is
to use lowercase. Paste the following into Dev Tools with the actual
node name and $REVERSE\_PORT you'd like to add:

::

    PUT _cluster/settings
    {
      "persistent": {
        "search": {
          "remote": {
            "sensorname": {
              "seeds": [ "172.18.0.1:5000X" ],
              "skip_unavailable": true
            }
          }
        }
      }
    }

Next, we can do the following from within Kibana Dev Tools to check our
configuration:

::

  GET _cluster/settings

If everything worked, then you should see the new sensor listed in the
output.

Last, check the Kibana Overview Dashboard or Discover and search for
logs from the new sensor.
