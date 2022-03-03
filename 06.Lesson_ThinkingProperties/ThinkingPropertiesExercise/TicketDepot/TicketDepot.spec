
rule ticketPriceCannotChange(method f, uint16 eventId) {
    env e;
    calldataarg args;

    address ownerBefore; uint256 ticketPriceBefore; uint256 ticketRemainingBefore;
    ownerBefore, ticketPriceBefore, ticketRemainingBefore = getEvent(e, eventId);

    f(e, args); 

    address ownerAfter; uint256 ticketPriceAfter; uint256 ticketRemainingAfter;
    ownerAfter, ticketPriceAfter, ticketRemainingAfter = getEvent(e, eventId);

    assert ticketPriceBefore == ticketPriceAfter, "ticket price changed"; 
}

rule ticketRemainingOnlyDecrease(method f, uint16 eventId) {
    env e;
    calldataarg args;

    address ownerBefore; uint256 ticketPriceBefore; uint256 ticketRemainingBefore;
    ownerBefore, ticketPriceBefore, ticketRemainingBefore = getEvent(e, eventId);

    f(e, args); 

    address ownerAfter; uint256 ticketPriceAfter; uint256 ticketRemainingAfter;
    ownerAfter, ticketPriceAfter, ticketRemainingAfter = getEvent(e, eventId);

    assert ticketRemainingAfter <= ticketRemainingBefore, "ticket remaining increased"; 
}

rule offeringPriceCannotChange(method f, bytes32 offeringId) {
    env e;
    calldataarg args;

    address ownerBefore; uint256 offerPriceBefore; uint256 offerDeadlineBefore;
    ownerBefore, offerPriceBefore, offerDeadlineBefore = getOffering(e, offeringId);

    f(e, args); 

    address ownerAfter; uint256 offerPriceAfter; uint256 offerDeadlineAfter;
    ownerAfter, offerPriceAfter, offerDeadlineAfter = getOffering(e, offeringId);

    assert offerPriceBefore == offerPriceAfter, "ticket price changed"; 
}

rule offeringDeadlineBiggerThanZero(method f, bytes32 offeringId) {
    env e;
    calldataarg args;

    address ownerBefore; uint256 offerPriceBefore; uint256 offerDeadlineBefore;
    ownerBefore, offerPriceBefore, offerDeadlineBefore = getOffering(e, offeringId);

    require offerDeadlineBefore > 0;

    f(e, args); 

    address ownerAfter; uint256 offerPriceAfter; uint256 offerDeadlineAfter;
    ownerAfter, offerPriceAfter, offerDeadlineAfter = getOffering(e, offeringId);

    assert offerDeadlineAfter > 0, "ticket price changed"; 
}


rule eventIncrease(uint64 ticketPrice, uint16 ticketsAvailable) {
    env e;
    uint256 numEventsBefore = getNumEvents(e);

    createEvent(e, ticketPrice, ticketsAvailable);

    uint256 numEventsAfter = getNumEvents(e);
    assert numEventsAfter == numEventsBefore + 1, "failed to increase num events"; 
}

