#  File: Employee.py
#  Name: Samanvitha Nukala


############################################################

#  Employee class acts as a superclass or parent class for other sub classes
#  first function initializes the class
#  uses ** kwargs to pass any number of variables without having declared the variables

class Employee:

    def __init__(self, **kwargs):
        pass
        self.name = kwargs['name']
        self.id = kwargs['id']
        self.salary = kwargs.get('salary')

    def salary(self):
        return self.salary

    def name(self):
        pass
        return self.name

    def id(self):
        pass
        return self.id

    def __str__(self):
        pass
        return f'Employee\n{self.name}, {self.id}, {self.salary}'

############################################################

#  Permanent Employee class acts as a subclass to the Employee parent class
#  first function initializes the class and adds benefits
#  cal_salary function is used to calculate salary based on benefits

class Permanent_Employee(Employee):

    def __init__(self, **kwargs):
        pass
        Employee.__init__(self, **kwargs)
        self.benefits = kwargs.get('benefits', [])

    def cal_salary(self):
        pass

        base_salary = self.salary

        if 'health_insurance' in self.benefits and 'retirement' not in self.benefits:
            updated_salary = (base_salary * 0.9)
        if 'retirement' in self.benefits and 'health_insurance' not in self.benefits:
            updated_salary = (base_salary * 0.8)
        if 'retirement' in self.benefits and 'health_insurance' in self.benefits:
            updated_salary = (base_salary * 0.7)

        return float(updated_salary)

    def benefits(self):
        pass
        return self.benefit

    def __str__(self):
        pass
        return f'Permanent_Employee\n{self.name}, {self.id}, {self.salary}, {self.benefits}'

############################################################

#  Manager class acts as a subclass to the Employee parent class
#  first function initializes the class and adds benefits
#  cal_salary function is used to calculate salary based on bonus

class Manager(Employee):
    
    def __init__(self, **kwargs):
        
        Employee.__init__(self, **kwargs)
        self.bonus = kwargs['bonus']

    def cal_salary(self):
        
        self.salary = self.salary + self.bonus
        return float(self.salary)

    def bonus(self):
    
        return self.benefits

    def __str__(self):
        
        return f'Manager\n{self.name}, {self.id}, {self.salary}, {self.bonus}'


############################################################

#  Temporary Employee class acts as a subclass to the Employee parent class
#  first function initializes the class and adds hours
#  cal_salary function is used to calculate salary based on hours

class Temporary_Employee(Employee):
    
    def __init__(self, **kwargs):
        
        Employee.__init__(self, **kwargs)
        self.hours = kwargs['hours']

    def cal_salary(self):
        
        self.salary = (self.salary * self.hours)
        return float(self.salary)

    def __str__(self):
        
        return f'Temporary_Employee\n{self.name}, {self.id}, {self.salary}, {self.hours}'


############################################################

#  Consultant class acts as a subclass to the Temporary Employee class
#  first function initializes the class and adds trips
#  cal_salary function is used to calculate salary based on hours and trips taken

class Consultant(Temporary_Employee):
    def __init__(self, **kwargs):
        pass
        Temporary_Employee.__init__(self, **kwargs)
        self.travel = kwargs['travel']

    def cal_salary(self):
        pass
        self.salary = (self.salary * self.hours) + (self.travel * 1000)

        return float(self.salary)

    def __str__(self):
        pass
        return f'Consultant\n{self.name}, {self.id}, {self.salary}, {self.hours}, {self.travel}'


############################################################
    
#  Consultant Manager class acts as a subclass to the Consultant and Manager classes
#  cal_salary function is used to calculate salary based on hours, trips taken, and bonus

class Consultant_Manager(Consultant, Manager):
    def __init__(self, **kwargs):
        
        Manager.__init__(self, **kwargs)
        Consultant.__init__(self, **kwargs)

    def cal_salary(self):
        
        self.salary = ((self.salary * self.hours) + (self.travel * 1000) + self.bonus)
        return float(self.salary)

    def __str__(self):
        
        return f'Consultant_Manager\n{self.name}, {self.id}, {self.salary}, {self.hours}, {self.travel}, Consultant_Manager\n{self.name}, {self.id}, {self.salary}, {self.bonus}'


def main():
    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100, hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary())

    print("Sam's Salary is:", sam.cal_salary())

    print("John's Salary is:", john.cal_salary())

    print("Charlotte's Salary is:", charlotte.cal_salary())

    print("Matt's Salary is:", matt.cal_salary())


if __name__ == "__main__":
    main()
