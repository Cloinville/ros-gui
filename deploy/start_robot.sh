#!/bin/bash
echo "$1"
me="$(hostname)"
echo "$me"

sshpass -p swarmies ssh -o "StrictHostKeyChecking no" ubuntu@$1 "cd ~/Minimal-Viable-Forager/misc && sudo ./rover_onboard_node_launch_pi.sh $me & echo swarmies"
