class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def calculate_salary_bonus(self):
        pass

    def save_to_database(self):
        pass


class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

class SalaryCalcultor:
    @staticmethod # same as class method
    def calculate_salary_bonus(employee : Employee): 
        pass


class EmployeeResitory:
    @staticmethod
    def save_to_database(employrr : Employee):
        pass