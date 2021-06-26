# Objective: Check if the employees have met their weekly sales targets.

class Employee:
    sales_made_this_week = 6
    name = 'Mark'
    designation = 'Sales Executive'
    number_of_working_hours = 40

    def has_achieved_target(self):
        target_sale = 5
        if self.sales_made_this_week >= target_sale:
            print("Target has been achieved!")
        else:
            print("Target has not been achieved.")


if __name__ == '__main__':
    employee_one = Employee()
    employee_one.has_achieved_target()
    print("Name: ", employee_one.name)

    employee_two = Employee()
    employee_two.has_achieved_target()
    print("Name: ", employee_two.name)
