

money_avaliable=int(input("Money owned: ")) #input
cases_bought=int(input("Cases bought: "))   #input
cost_per_case=int(input("Price of case: "))  #input
money_left=money_avaliable-cases_bought*cost_per_case
print("Remaining money: ", money_left)  #output