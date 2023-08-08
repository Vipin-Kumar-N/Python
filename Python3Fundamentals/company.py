from employee import Employee, SalaryEmployee, HourlyEmployee,CommissionEmployee

class Company:
    def __init__(self):
        self.employees = []
    
    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display(self):
        print("Current Employees : ")
        for i in self.employees:
            print(i.fname,i.lname)
            print('--------------')

    def pay_employee(self):
        print('Paying Employees...')
        for i in self.employees:
            print("Paying ",i.fname,i.lname)
            print(f'Amount {i.calc_paycheck():,.2f}')
            print("--------------")

def main():
    mycompany = Company()

    employee1 = SalaryEmployee('Sarah','George',50000)
    mycompany.add_employee(employee1)
    employee2 = HourlyEmployee('Vipin','Kumar',25,50)
    mycompany.add_employee(employee2)
    employee3 = CommissionEmployee('Vipin','Kumar',30000,5,200)
    mycompany.add_employee(employee3)

    print(mycompany.employees)
    mycompany.display()
    mycompany.pay_employee()

main()