#/bin/sh

certoraRun BordaBug3.sol:Borda --verify Borda:Borda.spec \
--solc solc \
--msg "$1"
