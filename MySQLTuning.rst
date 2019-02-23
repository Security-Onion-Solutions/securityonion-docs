MySQL Tuning
============

As of Security Onion 16.04.4.1 MySQL (on the master server) should have a randomized root password set by default. You can still access MySQL using the following as an example of the syntax to run a command against securityonion_db (Sguil DB):

::

   sudo mysql --defaults-file=/etc/mysql/debian.cnf -Dsecurityonion_db -e 'select * from event limit 10';

mysqltuner
----------

You can install and run ``mysqltuner`` to get some initial recommendations.

Install ``mysqltuner`` if you haven't already:

::

    sudo apt update && sudo apt install mysqltuner

Run ``mysqltuner`` with privileges:

::

    sudo mysqltuner

You may also want to install ``mysqltuner`` via the following manner, given that Security Onion now uses ``defaults-file`` to handle MySQL database credentials:

::

    wget http://mysqltuner.pl/ -O mysqltuner.pl && chmod +x mysqltuner.pl
    sudo ./mysqltuner.pl

/etc/mysql/my.cnf vs /etc/mysql/conf.d/
---------------------------------------

Implement mysqltuner's recommendations in ``/etc/mysql/my.cnf`` or create a new file in ``/etc/mysql/conf.d/`` with the changes. We recommend ``/etc/mysql/conf.d/`` so that your changes don't get overwritten during MySQL package upgrades.

Restart MySQL
-------------

Changes don't take effect until MySQL is restarted and you should ensure that Sguil and other services aren't using MySQL before shutting it down.

Variables
---------

Here are some common variables that may need to be tuned for your system:

-  ``open-files-limit``
-  ``table_cache``
-  ``key_buffer``
-  ``max_connections``

MySQL slow to start on boot
---------------------------

At boot time, MySQL checks all tables, which can take a long time. If you wish to disable this check, comment out ``check_for_crashed_tables`` in ``/etc/mysql/debian-start``.

table_definition_cache
------------------------

MySQL defaults ``table_definition_cache`` to ``400``. You may want to increase this value if one or more of the following conditions applies to you:

-  you have more than 400 MySQL ``.frm`` files
-  you've increased ``DAYSTOKEEP`` in ``/etc/nsm/securityonion.conf`` above its default value of 30 (each day requires 5 ``.frm`` files for OSSEC and 5 ``.frm`` files for each sniffing interface)
-  you're running prepared statements

Check mysql ``table_definition cache`` (defaults to ``400``):

::

    mysql -uroot -e "show global variables like 'table_definition_cache'"

Check current ``open_table_definitions`` (probably maxed out at ``table_definition_cache``):

::

    mysql -uroot -e "show global status like 'open_table_definitions'"

Check number of ``.frm`` files:

::

    sudo find /var/lib/mysql/ -name "*.frm" |wc -l

Increase table\_definition\_cache above number of ``.frm`` files by creating a file called ``/etc/mysql/conf.d/securityonion-table_definition_cache.cnf`` (please note ``.cnf`` extension NOT ``.conf``) and adding the following (replacing ``4000`` with your desired setting):

::

    [mysqld]
    table_definition_cache = 4000

Reboot and then verify that ``open_table_definitions`` never gets limited by ``table_definition_cache``.

For more information, please see:

https://bugs.mysql.com/bug.php?id=42041

https://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_table_definition_cache
