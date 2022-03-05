# Properties

## Valid states
1. **Valid state** Uninitialized
2. **Valid state** Initialized

## States transitions
3. **State transition** Uninitialized => Initialized

## Variables transitions
4. **Variable transition** add_liquidity() increases totalSupply and balanceOf(user) 
5. **Varaible transition** remove_liquidity(uint256) decreases totalSupply and balanceOf(user)


## High-Level
6. **High-Level** sum of all balances is equal to totalSupply
7. **High-Level** balance of any user is lower or equal to totalSupply

## Unit tests
8. **Unit test** init_pool() => initializes pool by settinig balances and total supply
9. **Unit test** add_liqiuidity() => adds liquidity to the pool and mints LP tokens
10. **Unit test** remove_liquidity(uint LP_tokens) => removes liquidity from the pool and burns LP tokens
11. **Unit test** swaps(address from_token) => swaps from_token to the second token
12. **Unit test** getContractAddress => returns contract address
13. **Unit test** getToken0DepositAddress() => returns token0 address
14. **Unit test** getToken1DepositAddress() => returns token1 address
15. **Unit test** sync() => updates token0Amount and token1Amount balances

# Priorities

## High Priority
* Properties 1-3 are high priority because issues with initializatin might lead to unexpected behaviour
* Properties 4-5 are high priority because break them might lead to loss of funds 
* Properties 6-7 are high priority because they might lead to withdraws of additional funds

## Medium Priority

## Low Priority
* Properties 8-15 are low priority because they might be easily detected by manual review r unit testing. 
