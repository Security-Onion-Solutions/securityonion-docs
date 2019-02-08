Salt
====

"Salt delivers a dynamic communication bus for infrastructures that can
be used for orchestration, remote execution, configuration management
and much more."

http://docs.saltstack.com/

What is OnionSalt?
------------------

"OnionSalt is a tool created to manage multiple Security Onion sensors."

https://github.com/TOoSmOotH/onionsalt

Best Practices
--------------

For the Security Onion 14.04 ISO, ``securityonion-onionsalt`` is
pre-installed (via ``securityonion-iso syslog-ng-core``) , and Salt is
configured by default when choosing `Best
Practices <Best-Practices>`__
during setup.

Salt and OnionSalt are optional packages
----------------------------------------

If you choose to install Security Onion via PPA without installing
``securityonion-iso syslog-ng-core``, please note that Salt is totally
optional. If you're happy with your current method of sensor management,
then you don't have to install ``securityonion-onionsalt``, and nothing
will change for you. Otherwise, install ``securityonion-onionsalt``
before running setup to enable Salt for your deployment.

Firewall Requirements
---------------------

Sensors need to be able to connect to the master server on ports
4505/tcp and 4506/tcp:

http://docs.saltstack.com/topics/tutorials/firewall.html

Installation
------------

For new deployments, `Best
Practices <Best-Practices>`__
(Production Mode) checks to see if the ``securityonion-onionsalt``
package is installed and, if so, enables Salt by default. If choosing
the "Custom" configuration option (Production Mode), simply answer "Yes"
at the prompt (where applicable), and setup will configure salt-master
and/or salt-minion services and open firewall ports as necessary.

For existing deployments, please see:

`Existing Deployment <Salt#salting-an-existing-deployment>`__

Checking Status
---------------

Want to verify all your sensors are up?

::

    sudo salt '*' test.ping

Remote Execution
----------------

Want to execute a command on all your sensors at once?

::

    sudo salt '*' cmd.run 'InsertYourCommandHere'

Features
--------

When you install and enable securityonion-onionsalt, the following data
will replicate from the master server out to the sensors every 15
minutes:

-  NIDS rules in /etc/nsm/rules/ (Snort/Suricata/barnyard will
   automatically restart as necessary)
-  HIDS rules in /var/ossec/rules/local\_rules.xml (Wazuh will
   automatically restart as necessary)
-  Bro scripts in /opt/bro/share/bro/policy/

   -  Bro does not restart automatically, but you can easily use salt on
      your master server to tell all your Bro instances to update and
      restart:

      ::

          # Force all Salt minions to update Bro scripts
          sudo salt '*' state.highstate
          # Restart Bro
          sudo salt '*' cmd.run 'nsm_sensor_ps-restart --only-bro'

-  Bro intel in /opt/bro/share/bro/intel/

   -  You'll need to restart Bro as shown above if you add any intel
      files to the default intel.dat. After that initial Bro restart,
      Bro should be watching the intel files with the Input framework
      which should automatically notice if the files ever change (new
      intel is added). In many cases, you won't need to restart Bro if
      you're just adding intel to the existing intel file(s).

-  user accounts and sudoers in /opt/onionsalt/pillar/users/init.sls
-  user ssh keys in /opt/onionsalt/salt/users/keys/

   -  For each user account in /opt/onionsalt/pillar/users/init.sls, you
      can add an SSH Public Key to
      /opt/onionsalt/salt/users/keys/USERNAME.id\_rsa.pub (replacing
      USERNAME with the user's actual username)

In addition, Salt is a full configuration management system, so you can
script anything that you want to deploy across your army of sensors.

Using Salt to Install Updates Across Your Entire Deployment
-----------------------------------------------------------

You can use Salt and Soup to install updates across your entire
deployment, but please remember to always update your master server
first:

::

    # Update Master first
    # If MySQL and/or kernel updates are installed, it will reboot
    sudo soup -y

    # After Master server is fully updated, now update the rest of the deployment
    # If MySQL and/or kernel updates are installed, the sensors will reboot
    sudo salt '*' cmd.run 'soup -y'

Also, please keep in mind that occasionally Ubuntu will release updates
that prompt for user input which would cause that last command to hang.
If you experience this, you should be able to ssh to each sensor and run
``soup`` interactively. For more information, please see `Issue
1108 <https://github.com/Security-Onion-Solutions/security-onion/issues/1108>`__.

Modifying Salt config files
---------------------------

If you need to modify the values in /etc/salt/master or
/etc/salt/minion, please pay attention to this note at the top of each
file:

::

    # /etc/salt/master
    # Per default, the master will automatically include all config files
    # from master.d/*.conf (master.d is a directory in the same directory
    # as the main master config file)
    #default_include: master.d/*.conf

::

    # /etc/salt/minion
    # Per default the minion will automatically include all config files
    # from minion.d/*.conf (minion.d is a directory in the same directory
    # as the main minion config file).
    #default_include: minion.d/*.conf

| Instead of modifying /etc/salt/master or /etc/salt/minion directly,
  please add your custom settings in /etc/salt/master.d/``*``.conf or
  /etc/salt/minion.d/``*``.conf, respectively.
| 

Changing Minion ID
------------------

If you need to change the ID for a minion, do the following:

On the minion machine:

::

    # Stop salt-minion 
    sudo service salt-minion stop

    # Edit /etc/salt/minion_id, modifying the ID as necessary.

    # Start salt-minion 
    sudo service salt-minion start

On the master machine:

::

    # Restart salt-master
    sudo service salt-master restart

    # List the salt keys
    sudo salt-key -L

    # Accept the new key for the modified minion
    sudo salt-key -A

    # Delete the old minion key 
    sudo salt-key -d OLD_MINION_NAME

    # Test the configuration -- minion should return "TRUE"
    sudo salt "MINION_NAME" test.ping

Salting an Existing Deployment
------------------------------

Configure the Master Server first
---------------------------------

::

    # Make sure the necessary packages are installed and updated
    sudo apt-get update && sudo apt-get install securityonion-onionsalt

    # Create a starting /opt/onionsalt/pillar/users/init.sls and /opt/onionsalt/salt/top.sls file from the template.
    sudo cp /opt/onionsalt/salt/top.sls.template /opt/onionsalt/salt/top.sls
    sudo cp /opt/onionsalt/pillar/users/init.sls.template /opt/onionsalt/pillar/users/init.sls

    # Edit /opt/onionsalt/salt/top.sls and add your master as a "backend".  
    # For example, if your SO master server's hostname is so-master, then replace:
       # My Onion Backend:
          'C*':
             - backend
    with:
       # My Onion Backend:
          'so-master':
             - backend

    # Open salt ports in firewall:
    # sudo ufw allow salt
    # OR preferably just allow from your sensor IP addresses like this:
    # sudo ufw allow proto tcp from a.b.c.d to any port 4505,4506
    # Also see our Firewall page:
    # https://securityonion.net/wiki/Firewall

    # Configure minion
    echo "master: localhost" | sudo tee -a /etc/salt/minion.d/onionsalt.conf

    # Allow salt-master and salt-minion to start on boot if they had previously been disabled
    [ -f /etc/init/salt-master.DISABLED ] && sudo mv /etc/init/salt-master.DISABLED /etc/init/salt-master.conf
    [ -f /etc/init/salt-master.override ] && sudo rm -f /etc/init/salt-master.override
    [ -f /etc/init/salt-minion.DISABLED ] && sudo mv /etc/init/salt-minion.DISABLED /etc/init/salt-minion.conf
    [ -f /etc/init/salt-minion.override ] && sudo rm -f /etc/init/salt-minion.override

    # Restart minion
    sudo service salt-minion restart

    # list the salt keys:
    sudo salt-key -L

    # You should see an unaccepted salt key for the minion, add it:
    sudo salt-key -a '*'

    # Verify that the master can communicate with the minion:
    sudo salt '*' test.ping

    # Tell salt to do an update
    sudo salt '*' state.highstate

Now configure salt-minion on a Sensor
-------------------------------------

::

    # Make sure the necessary packages are installed and updated
    sudo apt-get update && sudo apt-get install securityonion-onionsalt

    # Stop the running salt-master
    sudo service salt-master stop

    # Disable salt-master
    [ -f /etc/init/salt-master.conf ] && echo "manual" | sudo tee /etc/init/salt-master.override

    # Allow salt-minion to start on boot if it had previously been disabled
    [ -f /etc/init/salt-minion.DISABLED ] && sudo mv /etc/init/salt-minion.DISABLED /etc/init/salt-minion.conf
    [ -f /etc/init/salt-minion.override ] && sudo rm -f /etc/init/salt-minion.override

    # Configure minion
    MASTER=`grep SENSOR_SERVER_HOST /etc/nsm/*/sensor.conf |head -1 |cut -d\" -f2`
    echo "master: $MASTER" | sudo tee -a /etc/salt/minion.d/onionsalt.conf

    # Restart minion
    sudo service salt-minion restart

Now return to the Master and accept the new minion
--------------------------------------------------

::

    # Edit /opt/onionsalt/salt/top.sls and add the new minion as a "sensor"

    # list the salt keys:
    sudo salt-key -L

    # You should see an unaccepted salt key for the sensor, add it:
    sudo salt-key -a '*'

    # Verify that the master can communicate with all minions:
    sudo salt '*' test.ping

    # Tell all minions to do an update
    sudo salt '*' state.highstate

Maximum Event Size
------------------

Salt-master uses a default ``max_event_size`` of **1048576** bytes (1
`Mebibyte <https://en.wikipedia.org/wiki/Mebibyte>`__). For some
Security Onion deployments, this may need to be change to a larger value
to avoid receiving a ``VALUE_TRIMMED`` error (if the output of a command
run on a minion is too large to be passed back to the master).

See:
https://docs.saltstack.com/en/latest/ref/configuration/master.html#max-event-size

This setting should be changed in ``/etc/salt/master.d/onionsalt.conf``,
as opposed to directly in /etc/salt/master.

On a distributed Security Onion deployment
``/etc/salt/master.d/onionsalt.conf`` (on the master) should look like
the following:

::

    file_roots:
      base:
        - /opt/onionsalt/salt

    pillar_roots:
      base:
        - /opt/onionsalt/pillar

    max_event_size: YOUR_NEW_VALUE

After making changes, ensure salt-master has been started/restarted:

``sudo service salt-master restart``

Additional Reading
------------------

http://www.geekempire.com/2014/09/onionsalt-saltstack-cheat-sheer.html
