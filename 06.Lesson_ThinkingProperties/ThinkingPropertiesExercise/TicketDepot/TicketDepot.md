# Properties for TicketDepot

1. **Valid state** Event - NonExistence => eventsMap returns all 0
2. **Valid state** Event - Created => eventsMap returns owner != 0, ticketPrice >= 0, ticketsRemaining >= 0
3. **Valid state** Offering - NonExistence => offerings returns all 0
4. **Valid state** Offering - Created => offerings returns buyer != 0, price >= 0, deadline > 0
5. **State transition** Event NonExistence => Created
6. **State transition** Offering NonExistence => Created
7. **State transition** Offering Created => NonExistence
8. **Variable transition** eventsMap[id].ticketPrice cannot change
9. **Variable transition** eventsMap[id].ticketRemaining can only decrease
10. **Variable transition** offering[id].price cannot change
11. **Variable transition** offering[id].deadline > 0
12. **Unit test** ticketDepot(transactionFee) => updates transactionFee, owner, and set numEvents to 0
13. **Unit test** createEvent(ticketPrice, ticketAvailable) => creates new event with owner set to tx.origin, ticketPrice, and ticketsRemaining
14. **Unit test** buyNewTicket(eventId, attendee) => buys new ticket by adding attendee to eventsMap[id].attendees and transfers ticket payment to event owner, and transactionFee to owner 
15. **Unit test** offerTicket(eventId, ticketId, price, buyer, offerWindow) => offer ticket to reselt for eventId, with ticketId, price wth the deadline from now to offerWindow
16. **Unit test** buyOfferedTicket(eventId, ticketId, newAttendee) => buy offered ticket for eventId with ticketId, paying the offer price

## Priorities

## High Priority
* Properties 1-7 are high are high priority because they prove that the valid states and their transitions are correctly implemented
* Property 8 is high priority because its important that the price will not change accross the whole life of th event
* Property 9 is high priority because the supply of tickets shouldnt increase
* Property 10 is high priority because price should not change for the offering
* Property 11 is high priority because deadline set to 0 might lead to denial of service condition

## Low Priority
* Priorities 12-16 are low priorities because the vulnerabilities can be easily discovered with manual review
