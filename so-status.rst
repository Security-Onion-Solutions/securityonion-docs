.. _so-status:

so-status
=========

To check the status of Security Onion services, run ``sudo so-status``:

::

	Checking Docker status

	    Docker ---------------------------------------- [ OK ]    

	Checking container statuses

	    so-aptcacherng -------------------------------- [ OK ]    
	    so-cortex ------------------------------------- [ OK ]    
	    so-curator ------------------------------------ [ OK ]    
	    so-dockerregistry ----------------------------- [ OK ]    
	    so-elastalert --------------------------------- [ OK ]    
	    so-elasticsearch ------------------------------ [ OK ]    
	    so-filebeat ----------------------------------- [ OK ]    
	    so-fleet -------------------------------------- [ OK ]    
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
	    so-thehive ------------------------------------ [ OK ]    
	    so-thehive-es --------------------------------- [ OK ]    
	    so-wazuh -------------------------------------- [ OK ] 

so-status reads the list of enabled services from ``/opt/so/conf/so-status/so-status.conf`` and checks the status of each. If you ever disable a service, you may need to remove it from that file.

If you're running Security Onion in Import Mode, then so-status will show ``so-steno``, ``so-suricata``, and ``so-zeek`` as ``DISABLED`` since they are not sniffing live traffic. They will still function normally when running :ref:`so-import-pcap`.
