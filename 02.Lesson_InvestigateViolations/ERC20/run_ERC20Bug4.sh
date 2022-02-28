#!/bin/sh

certoraRun ERC20Bug4.sol:ERC20 --verify ERC20:ERC20.spec \
--rule integrityOfTransferFrom \
--optimistic_loop \
--msg "$1"
