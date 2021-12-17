# class attributes: attributes that are common to all the instances of the class.
# instance attributes: attributes that are specific to each individual instances of the class

class Employee:
    # class attribute
    name = 'Dummy'
    number_of_working_hours = 40

if __name__ == "__main__":
    employee_one = Employee()
    # instance attribute
    employee_one.name = 'Ashok'
    print(employee_one.number_of_working_hours)
    print(employee_one.name)

    employee_two = Employee()
    # instance attribute
    employee_two.name = 'Arun'
    print(employee_two.number_of_working_hours)
    print(employee_two.name)
    