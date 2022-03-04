#!/bin/sh

solc-select use 0.7.6

certoraRun BankWithLoops.sol:Bank --verify Bank:Loops.spec \
--optimistic_loop \
--loop_iter 2 \
--msg "$1"
