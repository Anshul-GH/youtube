class Employee:
    def __init__(self, inp_name):
        self.name = inp_name

    # def create_employee(self):
    #     self.name = 'Mark'

    def display_employee(self):
        print('Name: ', self.name)


if __name__ == '__main__':
    employee_one = Employee('Mark')
    # employee_one.create_employee()
    employee_one.display_employee()

    employee_two = Employee('Harry')
    # employee_two.create_employee()
    employee_two.display_employee()
