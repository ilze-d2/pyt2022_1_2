def computesalary(hours, rate):
    return (hours * rate)

hours_worked =45
overtime_hours = 5

if hours_worked > 40 :
    overtime_hours = hours_worked - 40
    regular_hours = 40
else : regular_hours = hours_worked

total_salary = computesalary (regular_hours, 10) + computesalary (overtime_hours, 17.5)
print ('Total salary is ${:,.2f}'. format (total_salary))