#!/bin/bash

sudo rm -rf /opt/ros/kinetic/share/rqt_mypkg
#Change if package name changes
sudo cp -r ~/ros-gui/ /opt/ros/kinetic/share/
sudo mv /opt/ros/kinetic/share/ros-gui /opt/ros/kinetic/share/rqt_mypkg
sudo cp -r ~/ros-gui/deploy ~
sudo chmod 777 ~/deploy/*
