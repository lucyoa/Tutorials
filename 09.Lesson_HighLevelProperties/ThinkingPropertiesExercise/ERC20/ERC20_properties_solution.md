# Properties

## Valid states
N/A

## State transitions
N/A

## Variable transitions
1. **Variable transition** decimals is constant
2. **Variable transition** name is constant
3. **Variable transition** symbol is constant
4. **Variable transition** balance can be changed only through transfer and transferFrom

## High-Level
5. **High-Level** sum of all balances is equal to totalSupply 
6. **High-Level** balance of any user is lower or equal to totalSupply

## Unit tests
7. **Unit test** name() => returns name of the token
8. **Unit test** symbol() => returns symbol of the token
9. **Unit test** decimals() => returns decimals of the token
10. **Unit test** totalSupply() => returns total supply of the token
11. **Unit test** balanceOf(address account) => returns balance of the account
12. **Unit test** transfer(address recipient, uint256 amount) => transfers amount of tokens from msg.sender to recipient
13. **Unit test** allowance(address owner, address spender) => returns allowance for spending owner's tokens by the spender
14. **Unit test** approve(address spender, uint256 amount) => approves spending amount of msg.sender's tokens by the spender
15. **Unit test** transferFrom(address sender, address recipient, uint256 amount) => transfer amount of tokens from sender to the recipient, decreases allowance
16. **Unit test** increaseAllowance(address spender, uint256 addedValue) => increases allowance of spending msg.sender's tokens by spender by addedValue
17. **Unit test** decreaseAllowance(address spender, uint256 subtractedValue) => decreases allowance of spending msg.sender's tokens by spender by subtractedValue

# Priorities

## High Priority
* Properties 1-3 are high priorities because breaking them might lead to unexpected behaviour
* Property 4 is high priority because balance should change only when transfer or transferFrom happening
* Properties 5-6 are high priority because breaking them might lead to unexpected behavour

## Medium Priority

## Low Priority
* Properties 7-17 are low priority because they can be easily detected by manual review an unit testing.
