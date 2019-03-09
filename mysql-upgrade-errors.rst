MySQL Upgrade Errors
====================

Ubuntu releases new MySQL packages periodically as needed. If you have a
Security Onion 16.04 installation and run ``soup`` to install these new
MySQL packages, you may see a few error messages as described below.

Error messages regarding MySQL upgrade process
----------------------------------------------

If your installation has MySQL disabled (because you haven't yet run
Setup or you've run Setup and chosen Forward Node or Storage Node), then
you may also see error messages like the following:

::

    mysql_upgrade: Got error: 2002: Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2) while connecting to the MySQL server
    Upgrade process encountered error and will not continue.
    mysql_upgrade failed with exit status 11
    dpkg: error processing package mysql-server-5.7 (--configure):
     subprocess installed post-installation script returned error exit status 1

    No apport report written because the error message indicates its a followup error from a previous failure.
                                                                                                              dpkg: dependency problems prevent configuration of mysql-server:
     mysql-server depends on mysql-server-5.7; however:
      Package mysql-server-5.7 is not configured yet.

    dpkg: error processing package mysql-server (--configure):
     dependency problems - leaving unconfigured

    Errors were encountered while processing:
     mysql-server-5.7
     mysql-server
    E: Sub-process /usr/bin/dpkg returned an error code (1)

You can resolve this issue using the following one-liner:

::

    sudo systemctl enable mysql.service && sudo apt -f install && sudo systemctl stop mysql.service && sudo systemctl disable mysql.service

Error message regarding MySQL 5.5
---------------------------------

Older versions of soup may result in error messages regarding MySQL 5.5.
Newer versions of soup have been updated to correct this. If you are
running an older version of soup and see error messages like this, they
can be ignored as Security Onion 16.04 uses MySQL 5.7:

::

    Package mysql-server-5.5 is not available, but is referred to by another package.
    This may mean that the package is missing, has been obsoleted, or
    is only available from another source
    However the following packages replace it:
      mysql-server-5.7 mysql-common percona-xtradb-cluster-server-5.6:i386 percona-server-server-5.6:i386 mysql-testsuite-5.7:i386 mariadb-server-10.0:i386 percona-xtradb-cluster-server-5.6
      percona-server-server-5.6 mysql-testsuite-5.7 mariadb-server-10.0 mysql-server-5.7:i386

    Package mysql-server-core-5.5 is not available, but is referred to by another package.
    This may mean that the package is missing, has been obsoleted, or
    is only available from another source
    However the following packages replace it:
      mysql-server-core-5.7 percona-server-server-5.6:i386 mariadb-server-core-10.0:i386 percona-server-server-5.6 mariadb-server-core-10.0 mysql-server-core-5.7:i386

    E: Package 'mysql-server-core-5.5' has no installation candidate
    E: Package 'mysql-server-5.5' has no installation candidate
