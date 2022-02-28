#/bin/sh

certoraRun BordaBug2.sol:Borda --verify Borda:Borda.spec \
--solc solc \
--rule onceBlackListedNotOut \
--msg "$1"
