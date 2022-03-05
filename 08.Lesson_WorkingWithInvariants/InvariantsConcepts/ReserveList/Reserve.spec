methods {
    getTokenAtIndex(uint256 index) returns (address) envfree
    getIdOfToken(address token) returns (uint256) envfree
    getReserveCount() returns (uint256) envfree
    addReserve(address token, address stableToken, address varToken, uint256 fee)  envfree
    removeReserve(address token) envfree
}

// Both lists are correlated - If we use the id of a token in reserves to retrieve a token in underlyingList, we get the same toke.
invariant listsAreCorrelated(uint256 tokenId)
    getTokenAtIndex(tokenId) != 0 => tokenId == getIdOfToken(getTokenAtIndex(tokenId))

// There should not be a token saved at an index greater or equal to reserve counter.
invariant noTokenAtIndexGreaterThanReserveCounter(uint256 tokenId)
    tokenId >= getReserveCount() => getTokenAtIndex(tokenId) == 0

// Id of assets is injective (i.e. different tokens should have distinct ids).
invariant assetsIsInjective(address token1, address token2)
    token1 != token2 && getTokenAtIndex(getIdOfToken(token1)) == token1 && getTokenAtIndex(getIdOfToken(token2)) == token2 => getIdOfToken(token1) != getIdOfToken(token2)

//  Independency of tokens in list - removing one token from the list doesn't affect other tokens.
rule independencyOfTokens(address token1, address token2) {

    require token1 != 0;
    require getTokenAtIndex(getIdOfToken(token1)) == token1;

    require token2 != 0;
    require getTokenAtIndex(getIdOfToken(token2)) == token2;

    removeReserve(token1);

    assert getTokenAtIndex(getIdOfToken(token2)) == token2, "failed independency of tokens";
}

// Each non-view function changes reservesCount by 1.
rule changesReserveCountByOne(method f) {
    uint256 countBefore = getReserveCount();

    calldataarg arg;
    env e;
    f(e, arg);

    uint256 countAfter = getReserveCount();

    assert f.selector == addReserve(address,address,address,uint256).selector => countBefore + 1 == countAfter, "failed addReserve";
    assert f.selector == removeReserve(address).selector => countBefore - 1 == countAfter, "failed removeReserve";
}


