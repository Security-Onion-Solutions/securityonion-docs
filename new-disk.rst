Adding a new disk
=================

Before doing this in production, make sure you practice this on a
non-production system!

There are at least 3 different ways to do this:

Method 1: LVM (Logical Volume Management)
-----------------------------------------

| If you chose the LVM option in the Ubuntu installer, then this should be the easiest way of adding disk space:
| https://wiki.ubuntu.com/Lvm

Method 2: Mount a separate drive to /nsm
----------------------------------------

This can be done in the Ubuntu installer, or after installation is complete. If doing this after running Setup, then you'll need to copy the existing data in ``/nsm`` to the new drive using something like this:

#. Comment out the cron job in ``/etc/cron.d/nsm-watchdog``
#. Restart cron:

   ::

     sudo service cron restart
   
#. Stop all services:

   ::
   
     sudo so-stop
     sudo service syslog-ng stop
     sudo service apache2 stop (if master server or standalone)
     sudo service mysql stop (if master server or standalone)
     
#. Determine your new drive's path:

   ::
   
     sudo fdisk -l
     
#. Partition the new drive using ``fdisk`` or ``parted``
#. Format the new partition using ``mkfs``
#. Mount the new drive to a temporary location in the filesystem:

   ::
   
     sudo mount /dev/sdb2 /mnt
     
#. Copy the existing data from ``/nsm`` to the temporary location:

   ::
   
     sudo cp -av /nsm/* /mnt/
     
#. Unmount the new drive from the temporary location:

   ::
   
     sudo umount /mnt
     
#. Rename the existing ``/nsm``:

   ::
   
     sudo mv /nsm /nsm-backup
#. Update ``/etc/fstab`` to mount the new drive to ``/nsm``:

   ::
   
     sudo vi /etc/fstab
   
   (You can use blkid to find your drive's UUID to write in /etc/fstab)
   
   ::
   
     sudo blkid /dev/sdb2
     
#. Re-create nsm directory after it was renamed:

   ::
   
     mkdir /nsm
     
#. Mount the new ``/nsm``:

   ::
   
     sudo mount /nsm
     
#. Start all services:

   ::
   
     sudo service mysql start (if master server or standalone)
     sudo service apache2 start (if master server or standalone)
     sudo service syslog-ng start
     sudo so-start
     
#. Uncomment the cron job in ``/etc/cron.d/nsm-watchdog``

#. Restart cron:

   ::
   
     sudo service cron restart
     
#. Test and verify that everything works

#. Reboot:

   ::
   
     sudo reboot
     
#. Test and verify that everything works

Method 3: Make /nsm a symlink to the new logging location
---------------------------------------------------------

If you do this, you'll need to do something like the following to avoid AppArmor issues:

Stop all services:

::

  sudo so-stop

Copy existing data from ``/nsm`` to new mount point:

::

  sudo cp -av /nsm/* /mnt/nsm

Rename existing ``/nsm``:

::

  sudo mv /nsm /nsm-backup

Make ``/nsm`` a symlink to the new logging location:


::

  sudo ln -s /mnt/nsm /nsm

Go to ``/etc/apparmor.d/local/``:

::

  cd /etc/apparmor.d/local/

Edit ``usr.sbin.mysqld``, copy the ``/nsm`` line(s), and change ``/nsm`` to the new location:

::

  sudo vi usr.sbin.mysqld

Edit ``usr.sbin.tcpdump``, copy the ``/nsm`` line(s), and change ``/nsm`` to the new location:

::

  sudo vi usr.sbin.tcpdump

Restart apparmor:

::

  sudo service apparmor restart

Start all services:

::

  sudo service nsm start

Moving the MySQL Databases
--------------------------

In this section, we'll cover how to move the MySQL databases containing all of your important alert and event data to another place.  This section assumes we'll be moving the databases to ``/nsm``, though, any other location will do.

The MySQL databases are stored under ``/var/lib/mysql``. We will need to move this folder and its sub-contents to the destination location. First, we must stop all processes that may be writing or using the databases.

::

  sudo so-stop
  sudo service mysql stop

Now, we need to make sure all other nsm-related processes are stopped. To double-check, run ``lsof`` on the nsm mount point to list any processes that have open file descriptors. Kill everything, or nearly everything, that comes up in the list.

::

  lsof /nsm

Next, let’s copy the data over to the new location leaving the original intact. You can use ``cp`` or ``rsync`` or another similar tool but be sure to preserve permissions ( -p ) and copy recursively ( -r ). Both examples are listed below, choose one:

::

  sudo cp -rp /var/lib/mysql /nsm
  sudo rsync -avpr var/lib/mysql /nsm

Once that’s finished, rename or backup the original just in case something goes wrong.

::

  sudo mv /var/lib/mysql /var/lib/mysql.bak

Next, create a symbolic link from ``/var/lib/mysql`` to the new location:

::

  sudo ln -s /nsm/mysql /var/lib/mysql

Ubuntu uses AppArmor to add an additional layer of security to running applications. We must tell apparmor about the new mysql database locations otherwise it will prevent the system from using it.

::

  sudo service apparmor stop

Edit ``/etc/apparmor.d/usr.sbin.mysqld`` to reflect the following patch which adds the new location:

::

  sudo vim /etc/apparmor.d/usr.sbin.mysqld

::

    --- a/apparmor.d/usr.sbin.mysqld
    +++ b/apparmor.d/usr.sbin.mysqld
    @@ -19,8 +19,8 @@

    /etc/hosts.allow r,
    /etc/hosts.deny r,

    +  /nsm/mysql/ r,
    +  /nsm/mysql/** rwk,
    +  /nsm/elsa/data/mysql/ r,
    +  /nsm/elsa/data/mysql/** rwk,
    /etc/mysql/*.pem r,
    /etc/mysql/conf.d/ r,
    /etc/mysql/conf.d/* r,

Finally, start all the processes back up:

::

  sudo service apparmor start
  sudo service mysql start
  sudo so-start
