.. _appendix:

Appendix
========

This appendix provides an overview of the process of migrating from the old Security Onion 2.3 to the new Security Onion 2.4.

.. tip::

   If you are a current Security Onion Solutions customer with Professional Services or Appliance coverage, contact SOS support and we can help you through this process.

.. warning::

   Security Onion 2.4 is a MAJOR change, so please note the following:

   - Security Onion 2.4 has higher hardware requirements, so you should check that your hardware meets those requirements. 
   - The /nsm partition must be on a separate disk.
   - InfluxDB data is not migrated.
   - If you have a distributed deployment, please note that 2.3 search nodes defaulted to cross cluster search whereas 2.4 defaults to full Elastic clustering. This means that you may need to rename or delete some Elasticsearch indices.
   - We do not provide any guarantees that the upgrade process will work! If the upgrade fails, be prepared to perform a fresh installation of Security Onion 2.4.
 
For the reasons listed above, we recommend that most users procure new hardware and perform a fresh installation of Security Onion 2.4.

.. tip::

   If you're planning to purchase new hardware, please consider official Security Onion appliances from Security Onion Solutions (https://securityonionsolutions.com). Our custom appliances have already been designed for certain roles and traffic levels and have Security Onion 2 pre-installed. Purchasing from Security Onion Solutions will save you time and effort **and** help to support development of Security Onion as a free and open platform!

If you have reviewed all of the warnings above and still want to attempt migration, you should be able to do the following.

.. warning::

   Please ensure that you have local access to the machine being upgraded via console, DRAC, IPMI, etc. Failure to do so could result in an unsuccessful upgrade, requiring a clean installation of Security Onion 2.4.

First, make sure that there is a backup in /nsm/backup:
::

    sudo ls -alh /nsm/backup

Disable services and reboot:
::

    sudo systemctl disable salt-minion
    sudo reboot

Make sure docker containers are stopped:
::

    sudo systemctl restart docker
    sudo docker ps

If there are any reminaing docker processes, stop them (replacing $CONT_ID with the actual ID):
::

    sudo docker stop $CONT_ID

Unmount /nsm:
::

    sudo umount /nsm
    sudo vgchange -an /dev/mapper/nsm
    sudo vgexport /dev/mapper/nsm

Boot the Security Onion 2.4 ISO image, go through the initial OS installation, and reboot.

After reboot, cancel setup and change partitioning (replacing /home/user with your desired temporary location):
::

    sudo cp -av /nsm/* /home/user/
    sudo umount /nsm
    sudo lvremove /dev/system/nsm

    sudo lvresize -L +XG /dev/system/root
    sudo xfs_growfs /dev/system/root

    sudo vgimport /dev/mapper/nsm
    sudo vgchange -ay /dev/mapper/nsm

Add entry into /etc/fstab and then mount:
::

    sudo mount -a 
    sudo systemctl daemon-reload

Remove /nsm/repo and /nsm/docker-registry from the old 2.3 /nsm.

Copy the /nsm contents of /home/user/ (or wherever they were copied to) back to /nsm
(repo, docker-registry, and elastic-fleet)

Run through setup as described in the :ref:`configuration` section.

After setup, get the secrets pillar from /nsm/backup:
::

    tar -xvf /nsm/backup/so-config-backup-2023_08_30.tar opt/so/saltstack/local/pillar/secrets.sls

Replace the mysql secret in secrets.sls with the backed-up value:
::

    docker exec -it so-mysql  mysql -u root -p
    # when prompted, enter the password from the 2.3 secrets.sls

At the mysql prompt, run the following query:
::

    SELECT User, Host from mysql.user;

If you get the error ``mysql error 1130: 172.17.1.1' is not allowed to connect to this mysql server``, then run the following:
::

    UPDATE mysql.user SET Host = '172.17.1.1' WHERE User = 'root' AND Host = 'localhost';

Exit the mysql shell and restart the so-mysql container.

Run a full checkin:
::

    sudo so-checkin
