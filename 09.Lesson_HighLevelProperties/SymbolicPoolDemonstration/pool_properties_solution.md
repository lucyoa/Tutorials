# Properties

## Valid states
N/A 

## States transitions
N/A

## Variables transitions
1. **Variable transition** deposit() causes totalSupply and balanceOf(user) to increase
2. **Variable transition** withdraw() causes totalSupply and balanceOf(user) to decrease
3. **Variable transition** feeRate is constant and cannot be changed
4. **Variable transition** decimals is constant
5. **Variable transition** name is constant
6. **Variable transition** symbol is constant

## High-Level
7. **High-Level** sum of all balances is equal to totalSupply
8. **High-Level** balance of any user is lower or equal to totalSupply

## Unit tests
9. **Unit test** sharesToAmount(unt256 shares) => returns shares to specific amount
10. **Unit test** amountToShares(uint256 amount) => returns amount to specific shares
11. **Unit test** deposit(uint256 amount) => deposit amount of assets and mint shares
12. **Unit test** withdraw(uint256 shares) => withdraw amount of asset and burn shares
13. **Unit test** flashLoan(address receiverAddress, uiint256 amount) => performs flashloan and executes external executeOperation functon
14. **Unit test** calcPremium => returns calculated premium
15. **Unit test** name() => returns name of the token
16. **Unit test** symbol() => returns symbol of the token
17. **Unit test** decimals() => returns decimals of the token
18. **Unit test** totalSupply() => returns total supply of the token
19. **Unit test** balanceOf(address account) => returns balance of the account
20. **Unit test** transfer(address recipient, uint256 amount) => transfers amount of tokens from msg.sender to recipient
21. **Unit test** allowance(address owner, address spender) => returns allowance for spending owner's tokens by the spender
22. **Unit test** approve(address spender, uint256 amount) => approves spending amount of msg.sender's tokens by the spender
23. **Unit test** transferFrom(address sender, address recipient, uint256 amount) => transfer amount of tokens from sender to the recipient, decreases allowance
24. **Unit test** increaseAllowance(address spender, uint256 addedValue) => increases allowance of spending msg.sender's tokens by spender by addedValue
25. **Unit test** decreaseAllowance(address spender, uint256 subtractedValue) => decreases allowance of spending msg.sender's tokens by spender by subtractedValue

# Priorities

## High Priority
* Priorities 1-2 are high priorities because the balance should increase/decrease based on deposit/transfers
* Priority 3 is high priority because its important for the fee not too change across usage of the contract
* Properties 4-6 are high priorities because breaking them might lead to unexpected behavio
* Properties 7 and 8 are high priorities because breaking them might lead to unexpected behaviour 

## Medium Priority
* Properties 5-6 are high priority because breaking them might lead to unexpected behavour

## Low Priority
* Properties 9-25 are low priority because they can be easily detected by manual review an unit testing


