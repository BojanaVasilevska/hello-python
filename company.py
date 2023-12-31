class Employee:
    def __init__(self, first_name, last_name, email, position=None, company=None, salary=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary
        self.leave_balance = {
            'annual_leave': 15,
            'special_circumstances_leave': 5,
            'maternity_leave': 12,
            'sick_days_leave': 10
        }

    def accept_offer(self, company, position, salary):
        if not self.company:
            print(f"{self.first_name} {self.last_name} receives a job offer from {company.name} for the position of {position} with a salary of {salary}.")
            self.position = position
            self.salary = salary
            self.company = company
            company.hire(self, position, salary)
        else:
            print(f"{self.first_name} {self.last_name} is already employed at {self.company.name}.")

    def reject_offer(self, company):
        if not self.company:
            print(f"{self.first_name} {self.last_name} rejects the job offer from {company.name}.")
        else:
            print(f"{self.first_name} {self.last_name} cannot reject the offer. Already employed at {self.company.name}.")

    def leave_company(self):
        if self.company:
            print(f"{self.first_name} {self.last_name} leaves {self.company.name}.")
            self.position = None
            self.salary = None
            self.company = None
        else:
            print(f"{self.first_name} {self.last_name} cannot leave a company. Not currently employed.")

    def days_off(self, leave_type, days):
        if leave_type in self.leave_balance and self.leave_balance[leave_type] >= days:
            print(f"{self.first_name} {self.last_name} has been granted {days} days of {leave_type} leave.")
            self.leave_balance[leave_type] -= days
        else:
            print(f"{self.first_name} {self.last_name} does not have enough {leave_type} leave balance.")

    def promotion(self, new_position, new_salary):
        print(f"{self.first_name} {self.last_name} has been promoted to {new_position} with a new salary of {new_salary}.")
        self.position = new_position
        self.salary = new_salary


class Company:
    def __init__(self, name, company_id, address):
        self.name = name
        self.company_id = company_id
        self.address = address
        self.employees = []

    def hire(self, employee, position, salary):
        self.employees.append(employee)

    def send_job_offer(self, employee, position, salary):
        print(f"{self.name} sends a job offer to {employee.first_name} {employee.last_name}.")
        employee.accept_offer(self, position, salary)


employee1 = Employee("Bojana", "Vasilevska", "bojanavasilevska@gmail.com")
employee2 = Employee("Cica", "Maca", "cicamaca@gmail.com")
employee3 = Employee("Maca", "Cica", "macacica@gmail.com")

companyA = Company("Semos", 1, "Doma 123")
companyB = Company("Semos Education", 2, "Doma 1234")

companyA.send_job_offer(employee1, "Software Engineer", 80000)
employee1.accept_offer(companyA, "Software Engineer", 80000)

companyA.send_job_offer(employee2, "Data Scientist", 90000)
employee2.reject_offer(companyA)

employee1.leave_company()

companyB.send_job_offer(employee2, "UX Designer", 75000)

valid_salaries_companyA = [employee.salary for employee in companyA.employees if employee.salary is not None]
valid_salaries_companyB = [employee.salary for employee in companyB.employees if employee.salary is not None]

avg_salary_companyA = sum(valid_salaries_companyA) / len(valid_salaries_companyA) if valid_salaries_companyA else 0
avg_salary_companyB = sum(valid_salaries_companyB) / len(valid_salaries_companyB) if valid_salaries_companyB else 0


print(f"Average salary cost for {companyA.name}: ${avg_salary_companyA:.2f}")
print(f"Average salary cost for {companyB.name}: ${avg_salary_companyB:.2f}")

print(vars(employee1))
print(vars(employee2))
print(vars(employee3))

employee1.days_off('annual_leave', 5)
employee2.days_off('sick_days_leave', 3)

employee3.promotion("Senior UX Designer", 90000)