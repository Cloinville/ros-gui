#!/bin/bash
me="$(hostname)"
sshpass -p swarmies ssh -o "StrictHostKeyChecking no" ubuntu@$1 "cd ~/Minimal-Viable-Forager/misc && sudo ./rover_onboard_node_launch_pi.sh $me & echo swarmies"
