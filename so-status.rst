.. _so-status:

so-status
=========

To check the status of Security Onion services, you can either run ``sudo so-status`` or simply view the Status panel on the :ref:`grid` page.

so-status reads the list of enabled services from ``/opt/so/conf/so-status/so-status.conf`` and checks the status of each. If you ever disable a service, you may need to remove it from that file.

Quiet Mode
----------

so-status supports a quiet mode:

::

	so-status -h
	Usage: /usr/sbin/so-status [OPTIONS]
	  Options:
	   -h                  - Prints this usage information
	   -q                  - Suppress output; useful for automation of exit code value
	   -j                  - Output in JSON format
	   -i                  - Consider the installation outcome regardless of whether the system appears healthy
	
	  Exit codes:
	    0                  - Success, system appears to be running correctly
	    1                  - Error, one or more subsystems are not running
	    2                  - System is starting
	    99                 - Installation in progress
	    100                - System installation encountered errors


	sudo so-status -q
	echo $?
	0

