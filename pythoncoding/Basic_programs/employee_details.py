class EmployeeDetails:

    def __init__(self, empno, ename, basic_pay):
        self.empno = empno
        self.ename = ename
        self.basic_pay = basic_pay
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

        def calculate_allowance(self):
            return (self.basic_pa * self.da / 100) + \
                (self.basic_pay * self.hra / 100)

        def calculate_deduction(self):
            return (self.basic_pay * self.pf / 100)

        def calculate_netsal(self):
            return self.basic_pay + self.calculate_allowance() - self.calculate_deduction()