# Salary readjustment in porcent

employee_salary = float(input('What is the salary?'))


salary_increase = float(input('Increase of?'))


result_of_increase = employee_salary + (employee_salary * salary_increase / 100)

print(result_of_increase)



salary_decrease = float(input('Decrease of?'))


result_of_decrease = employee_salary - (employee_salary * salary_decrease / 100)
print(result_of_decrease)
