#!/bin/sh

certoraRun ERC20Bug3.sol:ERC20 --verify ERC20:ERC20.spec \
--rule balanceChangesFromCertainFunctions \
--optimistic_loop \
--msg "$1"
