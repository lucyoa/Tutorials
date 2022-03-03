# Properties for Popsicle

1. **Valid state** nonExistence - balanceOf(user) = 0, feesCollectedPerShare = 0, rewards = 0
2. **Valid state** user - balanceOf(user) > 0 or feesCollectedPerShare > 0 or rewards > 0
3. **State transition** nonExistence => user
4. **Variable transition** totalFeesEarnedPerShare - can only increase
5. **Variable transition** accounts[address].feesCollectedPerShare - can only increase
6. **High-Level Property** balanceOf(user) has to be smaller or equal to totalSupply
7. **Unit test** deposit() => accounts[msg.sender].feesCollectedPerShare increase, accounts[msg.sender].Rewards increase, mints new tokens to msg.sender
8. **Unit test** withdraw(amount) => burns tokens from msg.sender, updates accounts[msg.sender].feesCollectedPerShare, updates accounts[msg.sender].Rewards
9. **Unit test** collectFees() => updates accounts[msg.sender].feesCollectedPerShare, zeroes rewards accounts[msg.sender].Rewards = 0, sends remaining rewards to msg.sender
10. **Unit test** OwnerDoItsJobAndEarnsFeesToItsClients() => increases totalFeesEarnedPerShare
11. **Unit test** assetOf(user) => returns the deserverd rewards

# Prorities

## High Priority
* Properties 1-3 are high priority because they are responsible for counting rewards for the user 
* Property 4 is high priority because its important that suddently fees will not decrease
* Property 5 is high priority because fees collected by the users holds information how much was already claimed
* Property 6 is high priority because tokens should not be artificially created without reflecting its existence in totalSupply

## Low Priority
* Properties 7-11 are low priority because they can be discovered using manual methods
