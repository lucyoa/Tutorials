#!/bin/sh

solc-select use 0.8.6

certoraRun BallGame.sol:BallGame --verify BallGame:BallGameSolution.spec \
--msg "$1"
