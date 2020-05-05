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
* To get RQT started up Run ```roscore``` in another window or application, then Run the command ```rqt``` 
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

This feature shows all of the algorithms loaded in from the Add Algorithm feature. It also has a checkbox next to all of them so that if the user runs the "Push Algorithm onto Robots" or the "Run Algorithm on Robot(s)" commands, it will be clear as to which algorithms are needed for the execution of such commands.

**Push Code to Robots**

This feature will take the selected robots and algorithms and load the specefied algorithms onto the speficied robots. This process is done by using ssh into the robot and then copying over the new files uploaded with the algorithm feature.

**Run Code on Robots** 

This feature will take the one algorithm you have selected and attempt to run that algorithm on the robot. This is explained in more detail below, but will recompile the code on the robot so that it runs the specified algorithm.

## Code Details

**Deploy**

This folder contains all of the files that are visable outside of the repository, these files exist on their on in the case where you do not need the repo on the machine but only the deployed version of the code and these files to opperate everything. 

**-Algorithms.txt** stores the file locations of all uploaded algorithm folders

**-Robots.txt** stores name and ip address of all submitted robots
 
**-push_alg.sh** script used to ssh into robot and upload code under behaviors package
   
**-start_robot.sh** script used to ssh into robot to change current algorithm to new one and run robot


**Resources**

This folder is required for RQT to function, it contains the **MyPlugin.ui** file which is required for the python to be able to build any of the QT elements. For any front end changes if a new field is going to be added, or if any text is going to be modified, this is where those changes must be made. 

**src/rqt_-mypkg/my_module.py**

This is the core file for this entire project. All functions that run in the background are controlled in this file. If an icon needs to be added/changed then this is the file to modify. All functions that run the backend need to be added/apended here. 

**refresh.sh**

This file is to be run after after you make changes to the repo code. When RQT runs it does not read the code in the repo but a directory in /opt. Because of this, this script moves your current code over to that directory and removes the old version of your code. This must be ran after any changes are made to see these changes on RQT. 

## Possible Bugs To Test with Hardware

## TODO List for Future Developer

