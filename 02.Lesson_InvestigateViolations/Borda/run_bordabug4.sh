#/bin/sh

certoraRun BordaBug4.sol:Borda --verify Borda:Borda.spec \
--solc solc \
--rule registeredCannotChangeOnceSet \
--msg "$1"
