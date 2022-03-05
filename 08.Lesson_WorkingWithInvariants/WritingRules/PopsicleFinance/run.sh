#!/bin/sh

solc-select use 0.8.4

certoraRun popsicle.sol:PopsicleFinance --verify PopsicleFinance:popsicle.spec \
--optimistic_loop \
--msg "$1"

