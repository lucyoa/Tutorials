#!/bin/sh

solc-select use 0.7.6

certoraRun BordaFixed.sol:Borda --verify Borda:Borda.spec \
--msg "$1"
