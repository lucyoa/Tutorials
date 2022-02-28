#!/bin/sh

certoraRun MeetingSchedulerBug2.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--rule checkPendingToCancelledOrStarted \
--msg "$1"
