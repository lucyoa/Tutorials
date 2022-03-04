#!/bin/sh 

certoraRun Loops.sol:Loops --verify Loops:LoopsUnrolling.spec \
--loop_iter 10 \
--msg "$1"
