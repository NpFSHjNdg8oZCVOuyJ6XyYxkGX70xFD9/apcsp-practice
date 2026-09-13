money_avaliable =  int(input("How much money do you have: "))
cases_buying = int(input("How many cases are you buying: "))
case_cost = int(input("How much do the cases cost: "))

total_cost = cases_buying * case_cost
money_left = money_avaliable - total_cost

print("Total cost of cases: " + str(total_cost))
print("Money left after buying cases: " + str(money_left))