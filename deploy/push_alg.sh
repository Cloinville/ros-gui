#!/bin/bash
me="$(hostname)"
sshpass -p swarmies scp -o "StrictHostKeyChecking no" $2/src/* ubuntu@$1:/~/Minimal-Viable-Forager/src/behaviours/src 
sshpass -p swarmies scp -o "StrictHostKeyChecking no" $2/include/* ubuntu@$1:/~/Minimal-Viable-Forager/src/behaviours/include 
#THIS NEEDS TO BE TESTED ON HARDWARE FOR BUGS
#I might have the file path wrong on the robots
#This assumes that when an algorithm is uploaded, its files are in an src and include dir