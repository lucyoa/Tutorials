methods {
    getPointsOfContender(address contender) returns(uint256) envfree
    hasVoted(address voter) returns(bool) envfree
    getWinner() returns(address, uint256) envfree
    getFullVoterDetails(address voter) returns(uint8 age, bool registered, bool voted, uint256 vote_attempts, bool black_listed) envfree
    getFullContenderDetails(address contender) returns(uint8 age, bool registered, uint256 points) envfree
    registerVoter(uint8 age) returns (bool)
    registerContender(uint8 age) returns (bool)
    vote(address first, address second, address third) returns(bool)
}

rule contendersPointsCanOnlyIncrease(method f, address user) {
    env e;
    calldataarg args;    

    uint8 ageBefore; bool registeredBefore; uint256 pointsBefore;
    ageBefore, registeredBefore, pointsBefore = getFullContenderDetails(user);
    require registeredBefore;

    f(e, args);
    uint256 pointsAfter = getPointsOfContender(user);

    assert pointsAfter >= pointsBefore, "contender's points decreased";
}

rule pointsOfWinnerCanOnlyIncrease(method f) {
    env e;
    calldataarg args;    

    address winnerBefore; uint256 pointsBefore;
    winnerBefore, pointsBefore = getWinner();

    f(e, args);

    address winnerAfter; uint256 pointsAfter;
    winnerAfter, pointsAfter = getWinner();

    assert pointsAfter >= pointsBefore, "failed winner points";
}


rule winnerPointsequalToContenderPoints(method f) {
    env e;
    calldataarg args;    

    address winnerBefore; uint256 pointsBefore;
    winnerBefore, pointsBefore = getWinner();

    uint8 age; bool registered; uint256 points;
    age, registered, points = getFullContenderDetails(winnerBefore);
    require registered;
    require getPointsOfContender(winnerBefore) == pointsBefore;

    f(e, args);

    address winnerAfter; uint256 pointsAfter;
    winnerAfter, pointsAfter = getWinner();
    assert getPointsOfContender(winnerAfter) == pointsAfter, "failed winner points";
}

rule contenderCannotUnregister(method f, address user) {
    env e;
    calldataarg args;

    uint8 ageBefore; bool registeredBefore; uint256 pointsBefore;
    ageBefore, registeredBefore, pointsBefore = getFullContenderDetails(user);
    require registeredBefore;

    f(e, args);

    uint8 ageAfter; bool registeredAfter; uint256 pointsAfter;
    ageAfter, registeredAfter, pointsAfter = getFullContenderDetails(user);

    assert registeredAfter, "failed, unregistered";
}

rule voterCannotUnregister(method f, address user) {
    env e;
    calldataarg args;

    uint8 ageBefore; bool registeredBefore; bool votedBefore; uint256 voteAttemptsBefore; bool blacklistedBefore;
    ageBefore, registeredBefore, votedBefore, voteAttemptsBefore, blacklistedBefore = getFullVoterDetails(user);
    require registeredBefore;

    f(e, args);

    uint8 ageAfter; bool registeredAfter; bool votedAfter; uint256 voteAttemptsAfter; bool blacklistedAfter;
    ageAfter, registeredAfter, votedAfter, voteAttemptsAfter, blacklistedAfter = getFullVoterDetails(user);

    assert registeredAfter, "failed, unregistered";
}
