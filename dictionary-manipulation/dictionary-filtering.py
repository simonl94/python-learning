from typing import Dict
employee_salary: Dict[str, int] = {
    "John": 85000,  "Paul": 100000, "Peter": 75000, "Samantha": 135000, "Sam": 50000}


def filter_employee_salary(employees: Dict[str, int]) -> Dict[str, int]:
    return {key: value for key, value in employees.items() if value > 80000}


employee_salary = filter_employee_salary(employee_salary)
employee_names = ", ".join(employee_salary.keys())
print("The following employees have more than a $85,000 salary: ",
      employee_names)
