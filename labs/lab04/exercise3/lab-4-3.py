hours = int(input())
if hours <= 2:
    parkingFee = 0
else:
    if hours <= 5:
        parkingFee = hours - 2 * 2
    else:
        parkingFee = 3 * 2 + hours - 5 * 3
if parkingFee > 30:
    parkingFee = 30
