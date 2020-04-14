#!/bin/bash

sudo apt-get install ros-kinetic-rqt ros-kinetic-rqt-common-plugins
sudo apt-get update
sudo apt-get dist-upgrade

sudo apt-get install sshpass

./refresh.sh

rqt --force-discover
