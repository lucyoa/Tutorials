#!/bin/sh

certoraRun ERC20Bug2.sol:ERC20 --verify ERC20:ERC20.spec \
--rule integrityOfTransfer \
--optimistic_loop \
--msg "$1"
