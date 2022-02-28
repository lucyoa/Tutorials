#!/bin/sh

certoraRun MeetingSchedulerBug1.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--msg "$1"
