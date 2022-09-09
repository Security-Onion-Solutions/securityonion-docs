.. _so-status:

so-status
=========

To check the status of Security Onion services, run ``sudo so-status``:

::

	Checking Docker status

	    Docker ---------------------------------------- [ OK ]    

	Checking container statuses

	    so-curator ------------------------------------ [ OK ]    
	    so-dockerregistry ----------------------------- [ OK ]    
	    so-elastalert --------------------------------- [ OK ]    
	    so-elasticsearch ------------------------------ [ OK ]    
	    so-filebeat ----------------------------------- [ OK ]    
	    so-grafana ------------------------------------ [ OK ]    
	    so-idstools ----------------------------------- [ OK ]    
	    so-influxdb ----------------------------------- [ OK ]    
	    so-kibana ------------------------------------- [ OK ]    
	    so-kratos ------------------------------------- [ OK ]    
	    so-logstash ----------------------------------- [ OK ]    
	    so-mysql -------------------------------------- [ OK ]    
	    so-nginx -------------------------------------- [ OK ]    
	    so-playbook ----------------------------------- [ OK ]    
	    so-redis -------------------------------------- [ OK ]    
	    so-sensoroni ---------------------------------- [ OK ]    
	    so-soc ---------------------------------------- [ OK ]    
	    so-soctopus ----------------------------------- [ OK ]    
	    so-steno -------------------------------------- [ OK ]    
	    so-strelka-backend ---------------------------- [ OK ]    
	    so-strelka-coordinator ------------------------ [ OK ]    
	    so-strelka-filestream ------------------------- [ OK ]    
	    so-strelka-frontend --------------------------- [ OK ]    
	    so-strelka-gatekeeper ------------------------- [ OK ]    
	    so-strelka-manager ---------------------------- [ OK ]    
	    so-suricata ----------------------------------- [ OK ]    
	    so-telegraf ----------------------------------- [ OK ]    

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
	
Import Node
-----------

If you're running a Security Onion Import node, then so-status will show ``so-steno``, ``so-suricata``, and ``so-zeek`` as ``DISABLED`` since they are not sniffing live traffic. :ref:`suricata` and :ref:`zeek` will still analyze pcaps normally when running :ref:`so-import-pcap`. :ref:`stenographer` is not used at all in Import mode.
