class Employee:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    
    def calc_paycheck(self):
        return self.salary/52

class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weeklyHr, HrRate):
        super().__init__(fname, lname)
        self.weeklyHr = weeklyHr
        self.HrRate = HrRate
    
    def calc_paycheck(self):
        return self.weeklyHr*self.HrRate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, salesNum, comRate):
        super().__init__(fname, lname, salary)
        self.salesNum = salesNum
        self.comRate = comRate

    def calc_paycheck(self):
        regSalary = super().calc_paycheck()
        totalCommssion = self.salesNum*self.comRate
        return regSalary+totalCommssion
