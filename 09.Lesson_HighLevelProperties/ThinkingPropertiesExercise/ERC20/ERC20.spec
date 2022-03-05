methods {
    name() returns (string memory) envfree
    symbol() returns (string memory) envfree
    decimals() returns (uint8) envfree

    totalSupply() returns (uint256) envfree
    balanceOf(address account) returns (uint256) envfree
    allowance(address owner, address spender) returns (uint256) envfree

    transfer(address recipient, uint256 amount) returns (bool)
    transferFrom(address sender, address recipient, uint256 amount) returns (bool)
    approve(address spender, uint256 amount) returns (bool)

    increaseAllowance(address spender, uint256 addedValue) returns (bool)
    decreaseAllowance(address spender, uint256 subtractedValue) returns (bool)
}


// check if any users balance is lower or equal to total supply
invariant totalFunds_GE_single_user_balance()
    forall address user. totalSupply() >= balanceOf(user)

// check if sum of all users balances is equal to total supply
ghost sum_of_all_balances() returns uint256 {
    init_state axiom sum_of_all_balances() == 0;
}

hook Sstore _balances[KEY address user] uint256 new_balance
    (uint256 old_balance) STORAGE {
        havoc sum_of_all_balances assuming sum_of_all_balances@new() == sum_of_all_balances@old() + new_balance - old_balance;
    }

invariant totalSupply_Equal_to_sum_of_all_balances()
    totalSupply() == sum_of_all_balances()

// check if transfer works
rule transferTest(address recipient, uint256 amount) {
	env e;
	uint256 balanceSenderBefore = balanceOf(e.msg.sender);
	uint256 balanceRecipientBefore = balanceOf(recipient);

	transfer(e, recipient, amount);

	uint256 balanceSenderAfter = balanceOf(e.msg.sender);
	uint256 balanceRecipientAfter = balanceOf(recipient);

	assert balanceRecipientBefore + balanceSenderBefore == balanceSenderAfter + balanceRecipientAfter, "failed to transfer correct amount";
}


// check if transferFrom works
rule transferFromAllowanceDecrease(address owner, address recipient, uint256 amount) {
	env e;
    // require owner != recipient; 

	uint256 allowanceBefore = allowance(owner, e.msg.sender);

	transferFrom(e, owner, recipient, amount);

	uint256 allowanceAfter = allowance(owner, e.msg.sender);
    
	assert allowanceBefore >= allowanceAfter, "failed, allowance increased";
}


rule increaseAllowanceTest(address spender, uint256 amount) {
	env e;
	uint256 allowanceBefore = allowance(e.msg.sender, spender);
	increaseAllowance(e, spender, amount);
	uint256 allowanceAfter = allowance(e.msg.sender, spender);

	assert amount > 0 => (allowanceAfter > allowanceBefore), "failed allowance did not increase";
}

rule decreaseAllowanceTest(address spender, uint256 amount) {
	env e;
	uint256 allowanceBefore = allowance(e.msg.sender, spender);
	decreaseAllowance(e, spender, amount);
	uint256 allowanceAfter = allowance(e.msg.sender, spender);

	assert amount > 0 => (allowanceAfter < allowanceBefore), "failed allowance did not increase";
}


