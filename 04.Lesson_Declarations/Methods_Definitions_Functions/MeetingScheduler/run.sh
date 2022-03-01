#!/bin/sh

certoraRun MeetingSchedulerFixed.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--msg "$1"
