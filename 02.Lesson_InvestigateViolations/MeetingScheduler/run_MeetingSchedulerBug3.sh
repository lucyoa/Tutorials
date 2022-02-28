#!/bin/sh

certoraRun MeetingSchedulerBug3.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--msg "$1"
