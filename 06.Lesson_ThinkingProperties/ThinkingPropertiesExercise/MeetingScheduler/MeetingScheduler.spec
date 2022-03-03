methods {
    getStateById(uint256) envfree;
    getStartTimeById(uint256) envfree;
    getEndTimeById(uint256) envfree;
    getNumOfParticipents(uint256) envfree;
    scheduleMeeting(uint256,uint256,uint256);
    startMeeting(uint256);
    cancelMeeting(uint256);
    endMeeting(uint256);
    joinMeeting(uint256) envfree;
}

rule unitializedToPending(method f, uint256 meetingId) {
    env e;
    calldataarg args;

    uint8 statusBefore = getStateById(meetingId);
    uint256 startTimeBefore = getStartTimeById(meetingId);
    uint256 endTimeBefore = getEndTimeById(meetingId);
    uint256 numOfParticipentsBefore = getNumOfParticipents(meetingId);

    require statusBefore == 0;
    require startTimeBefore == 0;
    require endTimeBefore == 0;
    require numOfParticipentsBefore == 0;
    
    f(e, args);
    
    uint8 statusAfter = getStateById(meetingId);
    uint256 startTimeAfter = getStartTimeById(meetingId);
    uint256 endTimeAfter = getEndTimeById(meetingId);
    uint256 numOfParticipentsAfter = getNumOfParticipents(meetingId);

    assert statusAfter == 1 => 
    (startTimeAfter > 0 && endTimeAfter > 0 && numOfParticipentsAfter == 0), 
    "failed from uninitialized to pending";
}

rule pendingToStartedOrCancelled(method f, uint256 meetingId) {
    env e;
    calldataarg args;

    uint8 statusBefore = getStateById(meetingId);
    uint256 startTimeBefore = getStartTimeById(meetingId);
    uint256 endTimeBefore = getEndTimeById(meetingId);
    uint256 numOfParticipentsBefore = getNumOfParticipents(meetingId);

    require statusBefore == 0;
    require startTimeBefore > 0;
    require endTimeBefore > 0;
    require numOfParticipentsBefore == 0;
    
    f(e, args);
    
    uint8 statusAfter = getStateById(meetingId);
    uint256 startTimeAfter = getStartTimeById(meetingId);
    uint256 endTimeAfter = getEndTimeById(meetingId);
    uint256 numOfParticipentsAfter = getNumOfParticipents(meetingId);

    assert statusAfter == 2 => 
    (startTimeAfter > 0 && endTimeAfter > 0 && numOfParticipentsAfter >= 0), 
    "failed from pending to started";
    assert statusAfter == 4 => 
    (startTimeAfter > 0 && endTimeAfter > 0 && numOfParticipentsAfter == 0), 
    "failed from pending to cancelled";
}

rule startedToEnded(method f, uint256 meetingId) {
    env e;
    calldataarg args;

    uint8 statusBefore = getStateById(meetingId);
    uint256 startTimeBefore = getStartTimeById(meetingId);
    uint256 endTimeBefore = getEndTimeById(meetingId);
    uint256 numOfParticipentsBefore = getNumOfParticipents(meetingId);

    require statusBefore == 2;
    require startTimeBefore > 0;
    require endTimeBefore > 0;
    require numOfParticipentsBefore >= 0;
    
    f(e, args);
    
    uint8 statusAfter = getStateById(meetingId);
    uint256 startTimeAfter = getStartTimeById(meetingId);
    uint256 endTimeAfter = getEndTimeById(meetingId);
    uint256 numOfParticipentsAfter = getNumOfParticipents(meetingId);

    assert statusAfter == 3 => 
    (startTimeAfter > 0 && endTimeAfter > 0 && numOfParticipentsAfter >= 0), 
    "failed from started to ended";
}

rule stateTransitions(method f, uint256 meetingId) {
    env e;
    calldataarg args;

    uint8 stateBefore = getStateById(meetingId);

    f(e, args);

    uint8 stateAfter = getStateById(meetingId);

    assert stateBefore == 0 => (stateAfter == 0 || stateAfter == 1), "failed from uninitialized to pending";
    assert stateBefore == 1 => (stateAfter == 1 || stateAfter == 2 || stateAfter == 4), "failed from pending to started or cancelled";
    assert stateBefore == 2 => (stateAfter == 2 || stateAfter == 3), "failed from started to ended";
}

rule startTimeLowerThanEndTime(method f, uint256 meetingId) {
    env e;
    calldataarg args;

    uint256 startTimeBefore = getStartTimeById(meetingId);
    uint256 endTimeBefore = getEndTimeById(meetingId);

    require startTimeBefore < endTimeBefore;
    f(e, args);

    uint256 startTimeAfter = getStartTimeById(meetingId);
    uint256 endTimeAfter = getEndTimeById(meetingId);

    assert startTimeAfter < endTimeAfter, "start time after end time";
}

rule statusOnlyIncrease(method f, uint256 meetingId) {
    env e;
    calldataarg args;

    uint8 stateBefore = getStateById(meetingId);
    f(e, args);

    uint8 stateAfter = getStateById(meetingId);
    assert stateAfter >= stateBefore, "failed to increase status";
}

rule isNumOfParticipentsIncrease(method f, uint256 meetingId){
    env e;
    calldataarg args;

    uint256 numOfParticipentsBefore = getNumOfParticipents(meetingId); 
    require numOfParticipentsBefore == 0;

    f(e, args);

    uint256 numOfParticipentsAfter = getNumOfParticipents(meetingId); 
    assert numOfParticipentsAfter >= numOfParticipentsBefore, "number of participents decreased";
}
