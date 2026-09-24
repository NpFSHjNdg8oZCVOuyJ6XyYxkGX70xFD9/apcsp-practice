age = int(input("Age: "))
movieTime = input("Movie Time (MATINEE/EVENING): ")
movieType =  input("Movie Type (REGULER/PREMIUM):")
ticketNumber = int(input("Amount of Tickets: "))
memberStatus = input("Member? (YES/NO): ")
conditionMet = 1

ticketPrice =  1 * ticketNumber



if movieType == "PREMIUM" and age < 17:
    print("INVALID ORDER")
    conditionMet = 0

if conditionMet == 1:
    
    if age <= 12:
        ticketPrice = 8
    else:
        if age >= 65:
            ticketPrice = 9
        else: 
            if age < 0 or ticketNumber <= 0:
                print("INVALID ORDER")
            else:
                ticketPrice = 12

    if movieType == "PREMIUM":
        ticketPrice = ticketPrice + 5 

    if movieTime == "MATINEE":
        ticketPrice = ticketPrice - 2

    subtotal = ticketPrice * ticketNumber
    finalPrice = subtotal

    if memberStatus == "YES":
        finalprice = ticketPrice * 0.9

    if ticketNumber >= 5:
        finalPrice = ticketPrice * 0.85

    finalPrice = round(ticketPrice, 2)

    print("Price Per Ticket: 0", ticketPrice)
    print("Subtotal: ", subtotal)
    print("Final Price: ", finalPrice)