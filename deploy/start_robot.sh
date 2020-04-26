#!/bin/bash
me="$(hostname)" 
#Maybe run command to kill current algorithm
sshpass -p swarmies ssh -o "StrictHostKeyChecking no" ubuntu@$1 "sed -i \"s@src\/.*@src\/$2\.cpp@g\" ~/Minimal-Viable-Forager/src/behaviours/CMakeLists.txt && cd ~/Minimal-Viable-Forager/misc && sudo ./rover_onboard_node_launch_pi.sh $me & echo swarmies"
#sed -i "s@src\/.*@src\/$2\.cpp@g" ~/Minimal-Viable-Forager/src/behaviours/CMakeLists.txt
# Sed statement for debuggin