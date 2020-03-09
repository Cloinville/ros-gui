#!/bin/bash
echo "$1"
me="$(whoami)"
echo "$me"
# ssh ubuntu@$1 "cd ~/Minimal-Viable-Forager 
# && sudo ./rover_onboard_node_launch_pi.sh $me"