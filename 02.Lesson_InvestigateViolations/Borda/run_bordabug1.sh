#/bin/sh

certoraRun BordaBug1.sol:Borda --verify Borda:Borda.spec \
--rule correctPointsIncreaseToContenders \
--solc solc \
--msg "$1"
