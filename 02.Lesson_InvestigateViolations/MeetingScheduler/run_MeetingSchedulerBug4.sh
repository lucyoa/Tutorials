#!/bin/sh

certoraRun MeetingSchedulerBug4.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--msg "$1"
