# ROS-GUI Overview

![Image of GUI](https://i.imgur.com/52gKZ1h.png)

ROS-GUI is a Capstone project at California University Channel Islands(CSUCI) done by Colin Hinton. The proposal of the project was to simplfy the process for running robots using OptiTrack for the DARPA Swarmathon Challenge and for other useages of the robotics at CSUCI. Below is documentation for the matinance of this project if ever picked up by another student. Detailing how to get set up, what all of the code does, how to use the tool, and possible bugs/issues that may be encounted due to lack of testing as a result of the COVID-19 pandemic.

## Dependencies

* ROS Version - [Kinetic](http://wiki.ros.org/kinetic/Installation)
* Operating System - [Ubuntu 16.4](https://releases.ubuntu.com/16.04/) on [Virtualbox](https://www.virtualbox.org/) 

* Python 2.7.12

## Installation 
1. Setup [Virtualbox](https://www.virtualbox.org/) to Run Ubuntu
1. Follow [This Guide](http://wiki.ros.org/kinetic/Installation) to install ROS Kinetic on your VM(Virtual Machine)
1. Clone [this repo](https://github.com/Cloinville/ros-gui) into your **home/user** directory and run ```sudo install.sh```
    1. After Running a RQT window should apprear similar to the image above
    
## Opening
* To get RQT started up, Run the command ```rqt``` 
* If ROS-GUI does not load, while tabbed into RQT click on **Plugins -> OptiTrack** to load the plugin
![Image of Load](https://i.imgur.com/fs7ifzt.png)

## Features
**Add Robot**

This feature allows users to add as many robots as they are working with to the application. All that is required is the name of the  (found with ```hostname``` on the robot) and and ip address (found with ```ifconfig```) on the robot. It is vital that this data is correct because these values will be used later to ssh into the robots. 

**Load Algorithm**

This feature allows the user to upload algorithms made to run different code on the robots. When the user clicks on the file button, they are prompted to upload a directory. Based on the previous robot code arcitechture, when uploading a new algorithm it expects to fine a folder named "src" containing the source code and a folder named "include" containing dependency files. If in the future robots do not require this structure then this change needs to be reflected in the push_alg.sh file.

**Robot List**

This feature shows all of the robots loaded in from the Add Robot feature. It also has a checkbox next to all of them so that if the user runs the "Push Algorithm onto Robots" or the "Run Algorithm on Robot(s)" commands, it will be clear as to which robots are needed for the execution of such commands.

**Algorithm List**


**Push Code to Robots**


**Run Code on Robots** 

## Code Details

## Possible Bugs To Test with Hardware

