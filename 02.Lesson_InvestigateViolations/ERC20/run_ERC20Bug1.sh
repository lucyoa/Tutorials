#!/bin/sh

certoraRun ERC20Bug1.sol:ERC20 --verify ERC20:ERC20.spec \
--optimistic_loop \
--rule integrityOfIncreaseAllowance \
--msg "$1"
