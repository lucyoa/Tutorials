#!/bin/sh
solc-select use 0.8.6

certoraRun ManagerBug1.sol:Manager --verify Manager:ManagerFullSolution.spec \
--msg "$1"
