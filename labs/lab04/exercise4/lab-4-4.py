weight = int(input())
if weight == 0:
    ticketPrice = ticketPrice - 10
else:
    if weight <= 15:
        ticketPrice = ticketPrice + 0
    else:
        ticketPrice = weight - 15 * 4
print(totalPrice)
