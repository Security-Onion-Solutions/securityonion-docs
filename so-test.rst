.. _so-test:

so-test
============

``so-test`` will run ``so-tcpreplay`` to replay some pcap samples to your sniffing interface. 

.. warning::

  You will need to have Internet access in order to download the pcap samples. Also, if you have a distributed deployment, make sure you run ``so-tcpreplay`` on the manager first to download the necessary Docker image.

::

  so-test
  Replay functionality not enabled; attempting to enable now (may require Internet access)...

  Pulling so-tcpreplay image
  =========================================================================
  Starting tcpreplay...

  This could take a while if another Salt job is running. 
  Run this command with --force to stop all Salt jobs before proceeding.
  =========================================================================
  local:
  ----------
            ID: so-tcpreplay
      Function: docker_container.running
        Result: True
       Comment: Created container 'so-tcpreplay'
       Started: 15:55:48.390107
      Duration: 1460.452 ms
       Changes:   
                ----------
                container_id:
                    ----------
                    added:
                        f035103cd8bf43134b56d4b19d77a0ae9e7c09fcb54ef6da67cf89bef5fc4019
                state:
                    ----------
                    new:
                        running
                    old:
                        None

  Summary for local
  ------------
  Succeeded: 1 (changed=1)
  Failed:    0
  ------------
  Total states run:     1
  Total run time:   1.460 s
  Replaying PCAP(s) at 10 Mbps on interface bond0...
  Actual: 111557 packets (12981286 bytes) sent in 10.38 seconds
  Rated: 1249997.6 Bps, 9.99 Mbps, 10742.07 pps
  Flows: 4102 flows, 394.99 fps, 2074477 flow packets, 45106 non-flow
  Statistics for network device: bond0
    Successful packets:        55304
    Failed packets:            444
    Truncated packets:         0
    Retried packets (ENOBUFS): 0
    Retried packets (EAGAIN):  0
  Replay completed. Warnings shown above are typically expected.
