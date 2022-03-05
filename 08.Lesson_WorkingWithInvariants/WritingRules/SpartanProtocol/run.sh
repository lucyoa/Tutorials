#!/bin/sh

solc-select use 0.8.4

certoraRun SpartaProtocolPool.sol:SpartaProtocolPool --verify SpartaProtocolPool:Sparta.spec \
--optimistic_loop \
--msg "$1"

