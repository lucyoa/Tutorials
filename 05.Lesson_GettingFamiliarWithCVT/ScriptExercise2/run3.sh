#!/bin/sh

certoraRun \
../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/MeetingSchedulerFixed.sol:MeetingScheduler \
--verify MeetingScheduler:../../04.Lesson_Declarations/Methods_Definitions_Functions/MeetingScheduler/meetings.spec \
--rule checkPendingToCancelledOrStarted \
--method "startMeeting(uint256)" \
--msg "$1"
