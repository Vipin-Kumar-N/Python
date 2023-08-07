owned = float(input("Money you owe : "))
apr = float(input("Apr (Annual percentage rate) : "))
payment = float(input("monthly payoff : "))
months = int(input("How many months result need to see: "))

monthlyRate = apr/100/12
for i in range(months):
    intrestPaid = owned*monthlyRate
    owned += intrestPaid
    owned -= payment

    if (owned-payment < 0):
        print('Last Payment is : ',owned)
        print("You paid of Loan in", i+1,'Months')
        break

    print('Paid',payment,'of which',intrestPaid,'was intrest', end=' ')
    print("Now i owe",owned)