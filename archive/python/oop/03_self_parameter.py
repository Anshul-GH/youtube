class Employee:
    def employee_details(self):
        self.name = 'Ram'
        self.age = 30
    
    def print_empl_details(self):
        print('Name: ', self.name)
        print('Age: ', self.age)



if __name__ == "__main__":
    employee = Employee()
    
    employee.employee_details()
    employee.print_empl_details()
    # Employee.employee_details(employee)
