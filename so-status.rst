.. _so-status:

so-status
=========

To check the status of Security Onion services, you can either run ``sudo so-status`` or simply view the Status panel on the :ref:`grid` page.

so-status reads the list of enabled services from ``/opt/so/conf/so-status/so-status.conf`` and checks the status of each. If you ever disable a service, you may need to remove it from that file.

Quiet Mode
----------

so-status supports a quiet mode:

::

	sudo so-status -h

    	/usr/sbin/so-status  [-h] [-q|--quiet]

   	-h             Show this message.
   	-q|--quiet     Suppress the output and only return a
	              single status code for overall status
	0:Ok, 1:Error, 2:Starting/Pending, 99:Installing SO

	sudo so-status -q
	echo $?
	0

