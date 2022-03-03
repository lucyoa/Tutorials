# Properties for MeetingScheduler

1. **Valid state** - Uninitialized => startTime = 0, endTime = 0, numOfParticipents = 0, organizer = 0, status = 0
2. **Valid state** - Pending => startTime > 0, endTime > 0, numOfParticipents = 0, organizer != 0, status = 1
3. **Valid state** - Started => startTime > 0, endTime > 0, numOfParticipents >= 0, organizer != 0, status = 2
4. **Valid state** - Ended => startTime > 0, endTime > 0, numOfParticipents >= 0, organizer != 0, status = 3
5. **Valid state** - Cancelled => startTime > 0, endTime > 0, numOfParticipents = 0, organizer != 0, status = 1
6. **State transition** - Uninitialized => Pending
7. **State transition** - Pending => Started or Cancelled
8. **State transition** - Started => Ended	
9. **Variable transition** - meetings[id].numOfParticipents can only increase
10. **Variable transition** - meetings[id].startTime < meetings[id].endTime
11. **Variable transition** - meetings[id].status can only increase (uint8)
12. **High-level** - No way to to end or cancel meeting if it already started status == STARTED and now < endTime 
13. **Unit test** - scheduleMeeting(id, startTime, endTime) => creates meeting with: startTime, endTime, numberOfParticipents = 0, organizer != 0, status = pending	
14. **Unit test** - startMeeting(meetingId) => sets meeting status to started
15. **Unit test** - cancelMeeting(meetingId) => sets meeting status to cancelled
16. **Unit test** - endMeeting(meetingId) => sets meeting status to ended
17. **Unit test** - joinMeeting(meetinId) => increases the numbOfParticipents

# Prioritizing
## High Priority:
* Properties 1-8 have direct impact on the flow of interaction with the contract. That might lead to some weird unpredicted states. 
* Priority 10 is high priority because it might lead to some denial of service cases


## Medium Priority
* Property 9 is low because it doesn't have direct impact on the contract

## Low Priority
* Property 11 is low because its already being partially checked by properties 1-8
* Property 12 is low because it is already being partially checked by properties 1-8
* Properties 13-17 are low priority since there are simpler ways of checking correctnes of its working
