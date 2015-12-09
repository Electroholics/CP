
#!/bin/bash
#commands to update machine time from the server
date
sudo service ntp stop
sudo ntpd -gq
sudo service ntp start
date
