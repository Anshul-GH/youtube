# instance methods: methods that make use of the self parameter to access and modify the instance attributes of the class
# static methods: not tied up to any instance and do not need the self parameter to be passed

class Employee:
    def employee_details(self):
        self.name = 'Ben'

    @staticmethod
    def welcome_message():
        print('Welcome to our organization!')


if __name__ == '__main__':
    employee = Employee()
    employee.employee_details()
    print(employee.name)
    employee.welcome_message()
    # Employee.welcome_message(employee)
