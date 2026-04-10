#!/bin/bash
source venv/bin/activate
#start python video stream
/home/pi/python/mjpeg_server.py &
sleep 5
python3 /home/pi/python/flask/server.py &
#su pi -c "python3 /home/pi/python/flask/server.py &"

#start camera pan and tilt program deamon
/home/pi/python/piservo_pipe.py &

#start camera pan and tilt network deamon
/home/pi/python/network_servo.py &

# line up camera after reboot
echo servo 165 140 >/home/pi/python/FIFO_piservo

