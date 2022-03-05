methods {
    deposit()
    withdraw(uint amount)
    collectFees() 
    OwnerDoItsJobAndEarnsFeesToItsClients()
    assetsOf(address user) returns(uint) envfree
    myAddress() returns (address)
    totalSupply() returns (uint256) envfree
    balanceOf(address account) returns (uint256) envfree
    transfer(address recipient, uint256 amount) returns (bool)
    allowanceOf(address owner, address spender) returns (uint256) envfree
    approve(address spender, uint256 amount) returns (bool)
    transferFrom(address sender, address recipient, uint256 amount) returns (bool)
    increase_allowance(address to_user, uint inc_amount)
    decrease_allowance(address from_user, uint dec_amount)

    // helpers
    getTotalFeesEarnedPerShare() envfree;
    getFeesCollectedPerShare(address account) envfree;
}

// check if any users balance is lower or equal to total supply
invariant totalFunds_GE_single_user_balance()
    forall address user. totalSupply() >= balanceOf(user)

// check if sum of all users balances is equal to total supply
ghost sum_of_all_balances() returns uint256 {
    init_state axiom sum_of_all_balances() == 0;
}

hook Sstore balances[KEY address user] uint256 new_balance
    (uint256 old_balance) STORAGE {
        havoc sum_of_all_balances assuming sum_of_all_balances@new() == sum_of_all_balances@old() + new_balance - old_balance;
    }

invariant totalSupply_Equal_to_sum_of_all_balances()
    totalSupply() == sum_of_all_balances()


// check if totalFeesEarnedPerShare can only increase
rule totalFeesEarnedPerShareCanOnlyIncrease(method f) {
    env e;
    calldataarg args;

    uint256 totalFeesEarnedPerShareBefore = getTotalFeesEarnedPerShare();
    f(e, args);
    uint256 totalFeesEarnedPerShareAfter = getTotalFeesEarnedPerShare();

    assert totalFeesEarnedPerShareAfter >= totalFeesEarnedPerShareBefore, "totalFeesEarnerPerShare decreased";
}

// check if accounts[address].feesCollectedPerShare can only increase
rule feesCollectedPerShare(method f, address user) {
    env e;
    calldataarg args;

    uint256 feesCollectedPerShareBefore = getFeesCollectedPerShare(user);
    f(e, args);
    uint256 feesCollectedPerShareAfter = getFeesCollectedPerShare(user);

    assert feesCollectedPerShareAfter >= feesCollectedPerShareBefore, "feesCollectedPerShare decreased";
}

// deposit mints new tokens to msg.sender
rule checkDepositUnitTest(address user) {
    env e;

    uint256 balanceBefore = balanceOf(user);
    deposit(e);
    uint256 balanceAfter = balanceOf(user);

    assert balanceAfter >= balanceBefore, "failed minting tokens";
}

