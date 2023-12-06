class Employee:
    def __init__(self, first_name, last_name, email, position=None, company=None, salary=None):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.position = position
        self.company = company
        self.salary = salary

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

companyA = Company("Semos", 1, "Doma 123")
companyB = Company("Semos Education", 2, "Doma 1234")

companyA.send_job_offer(employee1, "Software Engineer", 80000)
employee1.accept_offer(companyA, "Software Engineer", 80000)

employee2.reject_offer(companyA)

employee1.leave_company()

companyB.send_job_offer(employee2, "UX Designer", 75000)
