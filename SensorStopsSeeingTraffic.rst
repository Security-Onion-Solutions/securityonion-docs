Sensor Stops Seeing Traffic
===========================

| Just like in everything, there's always more than one way to do it!
| 
| Here are a few options:
| 

Wazuh
-----

| Wazuh checks your sniffing interfaces every 10 minutes. If no packets
  have been received within that 10 minute window, then Wazuh will
  generate an alert. This alert can be found in Sguil, Squert, and
  Kibana. If you'd like Wazuh to email you, then configure it for email
  as shown here:
| `<Email#how-do-i-configure-ossec-to-send-emails>`__

Bro
---

| Bro will automatically email you when it stops seeing traffic on an interface. All you have to do is configure Bro per the `Email <Email>`__ page.
