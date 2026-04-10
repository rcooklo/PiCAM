#!/bin/bash
#be sure camera is working (rpicam-hello) before running install 
sudo apt update

mv python ../
mv checknetwork.sh ..
mv startscript.sh ..
sudo mv sd /usr/bin/sd
sudo chmod +x /usr/bin/sd
cat profileupdate.txt >> ~/.profile
cd ~
sudo apt install -y python3-pip python3-venv libcap-dev
sudo apt install -y python3-picamera2 python3-libcamera
python -m venv --system-site-packages venv
source venv/bin/activate
pip3 install --upgrade setuptools
pip3 install adafruit-python-shell
#mkdir python
cd python
wget https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/raspi-blinka.py
sudo -E env PATH=$PATH python3 raspi-blinka.py
pip3 install adafruit-circuitpython-pca9685
pip install adafruit-circuitpython-servokit
pip install RPi.GPIO
sudo mknod FIFO_piservo p
sudo chmod 666 FIFO_piservo
pip3 install flask
pip3 install waitress
cd ~
chmod +x startscript.sh 
chmod +x python/flask/*.sh
chmod +x /home/pi/python/mjpeg_server.py
chmod +x /home/pi/python/piservo_pipe.py
chmod +x /home/pi/python/network_servo.py
pversion=`ls /usr/bin/python3.??`
echo $pversion
sudo setcap CAP_NET_BIND_SERVICE=+eip $pversion
## possible additions
#source venv/bin/activate
#cd python
#pip install picamera2
## end additions

