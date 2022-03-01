#!/bin/sh

certoraRun BordaFixed.sol:Borda --verify Borda:Borda.spec \
--msg "$1"
