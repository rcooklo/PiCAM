#!/bin/bash
ping -c 1 192.168.24.1 >/dev/null
return_code=$?
if [ $return_code -eq 0 ] 
then
    echo "The network is up!"
elif [ $return_code -eq 1 ]
then
    echo "The network is down :("
    sudo systemctl restart NetworkManager.service
fi

