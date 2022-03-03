
methods {
	ballAt() returns uint256 envfree
}

invariant neverReachPlayer4() 
	ballAt() != 3 && ballAt() != 4 

rule neverReachPlayer4Rule(method f) {
    env e;
    calldataarg args;

    uint256 ballAtBefore = ballAt();
    require ballAtBefore != 3 && ballAtBefore != 4;

    f(e, args);

    uint256 ballAtAfter = ballAt();
    assert ballAtAfter != 4, "failed, ballat 4";
}
