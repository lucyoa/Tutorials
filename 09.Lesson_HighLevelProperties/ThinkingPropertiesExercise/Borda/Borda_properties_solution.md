# Properties

## Valid States
1. **Valid state** contenderNotRegistered - Contender not registered
2. **Valid state** contenderRegistered - Contender registered
3. **Valid state** voterNotRegistered - Voter not registered
4. **Valid state** voterRegisteredNotVotedNotBlackListed - Voter registered, not voted, not blacklisted
5. **Valid state** voterRegisteredVotedNotBlacklisted - Voter registered, voted, not blacklisted
6. **Valid state** voterRegisteredVoterBlacklisted - Voter registered, voted, blacklisted


## State transition 
7. **State transition** contenderNotRegistered => contenderRegistered
8. **State transition** voterNotRegistered => voterRegisteredNotVotedNotBlackListed
9. **State transition** voterRegisteredNotVotedNotBlackListed => voterRegisteredVotedNotBlacklisted
10. **State transition** voterRegisteredVotedNotBlacklisted => voterRegisteredVoterBlacklisted

## Variable transition
11. **Variable transition** contenders[user].points can only increase
12. **Variable transition** voters[user].vote_attempts can only increase
13. **Variable transition** pointsOfWinner can only increase

## High-Level
14. **High-Level** sum of all voters that voted multiplied by 6 should be equal to sum of points of all contenders
15. **High-Level** winner points are equal to pointsOfWinner
16. **High-Level** voter registered once cannot be unregistered
17. **High-Level** contender regstered once cannot be unregistered

## Unit tests
18. **Unit test** getPointsOfContender(address contender) => returns contener points 
19. **Unit test** hasVoted(address voter) => checks if voter has voted
20. **Unit test** getWinner() => returns winner and winner's points
21. **Unit test** getFullVoterDetails(address voter) => returns voter details 
22. **Unit test** getFullContenderDetails(address contender) => returns contender details
23. **Unit test** registerVoter(uint8 age) => register voter and add it to voters list
24. **Unit test** registerContender(uint8 age) => register contender and add it to contenders list
25. **Unit test** vote(address first, address second, address third) => vote at 3 contenders

# Priorities

## High Priorities
* Properties 1-10 are high priorities because they might lead to some unexpected conditions
* Property 11 is high because it should not be possible for points to decrease
* Property 13 is high because he points of winner should only increase
* Properties 14-17 are high because they are responsible for fair voting

## Medium Priorities
* Property 12 is medium because vote attempts and blacklisting do not have impact hw contract works

## Low Priorities
* Properties 18-25 are low because they can be easily detected by manual review and unit testing


