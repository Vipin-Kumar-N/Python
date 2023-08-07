expense = [10,33.2,68,668,36.5,655.5,5]
cal = 0
total = sum(expense)
for x in expense:
    cal += x
print("Your Expense : $",cal, sep ='')
print(total)
inputnumber = int(input("No.of inputs : "))
for i in range(inputnumber):
    expense.append(float(input("Enter Expense : ")))
print(expense)