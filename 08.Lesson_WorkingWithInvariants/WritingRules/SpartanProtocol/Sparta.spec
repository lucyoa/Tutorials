methods {
    init_pool()
    add_liquidity() returns (uint)
    remove_liquidity(uint LP_tokens)
    swap(address from_token)
    getContractAddress() returns (address)
    getToken0DepositAddress() returns (address)
    getToken1DepositAddress() returns (address)
    sync()

    myAddress() returns (address)
    totalSupply() returns (uint256) envfree
    balanceOf(address account) returns (uint256) envfree
    transfer(address recipient, uint256 amount) returns (bool)
    getAllowance(address owner, address spender) returns (uint256) envfree
    approve(address spender, uint256 amount) returns (bool)
    transferFrom(address sender, address recipient, uint256 amount) returns (bool)
    increase_allowance(address to_user, uint inc_amount)
    decrease_allowance(address from_user, uint dec_amount)
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


rule totalSupplyIncreaseAfterAddLiquidity() {
    env e;
    uint256 totalSupplyBefore = totalSupply();
    uint256 units = add_liquidity(e);
    uint256 totalSupplyAfter = totalSupply();

    assert totalSupplyBefore + units == totalSupplyAfter, "failed to increase totalSupply";
}

rule totalSupplyDecreaseAfterRemoveLiquidity(uint256 units) {
    env e;
    uint256 totalSupplyBefore = totalSupply();
    remove_liquidity(e, units);
    uint256 totalSupplyAfter = totalSupply();

    assert totalSupplyBefore - units == totalSupplyAfter, "failed to decrease totalSupply";
}


rule lpTokenIncreaseAfterAddLiquidity() {
    env e;
    uint256 balanceBefore = balanceOf(e.msg.sender);
    uint256 units = add_liquidity(e);
    uint256 balanceAfter = balanceOf(e.msg.sender);

    assert balanceBefore + units == balanceAfter, "failed to increase lpTokens add liquidity";
}

rule lpTokenDecreaseAfterRemoveLiquidity(uint256 units) {
    env e;

    uint256 balanceBefore = balanceOf(e.msg.sender);
    remove_liquidity(e, units);
    uint256 balanceAfter = balanceOf(e.msg.sender);

    assert balanceBefore - units == balanceAfter, "failed to decrease lpTokens remove liquidity";
}

