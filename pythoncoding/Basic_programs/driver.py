from Basic_programs.employee_details import EmployeeDetails

eno = int(input('Emp no: '))
name = input('Emp name: ')
bp = float(input('Basic Pay: '))

employee = EmployeeDetails(eno, name, bp)

print('Emp no: ', employee.empno)
print('Emp name: ', employee.ename)
print('Basic pay: ', employee.basic_pay)
print('Salary: ', employee.calculate_netsal())