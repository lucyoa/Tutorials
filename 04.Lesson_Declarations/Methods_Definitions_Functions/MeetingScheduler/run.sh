#!/bin/sh

solc-select use 0.8.7

certoraRun MeetingSchedulerFixed.sol:MeetingScheduler --verify MeetingScheduler:meetings.spec \
--msg "$1"
