weight = int(input("Weight(lbs): "))
distance = int(input("Shipping Distance(Miles): "))
expressShipping = (input("Express Shipping(Y/N): "))
cost = 5

if weight > 50 or distance > 2000:
    print("MANUAL REVIEW")

else:
    if weight > 25:
        cost = cost + 12

    if weight > 10:
        cost = cost + 8

    if distance > 500:
        cost = cost + 10
    else:
        cost = cost

    if expressShipping == "Y":
        cost = cost + 15
    else:
        cost = cost

    print("Shipping Cost: " + str(cost))