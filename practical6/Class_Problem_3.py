class Employee:
    def __init__(self,name,last_name,monthly_salary):
        self.name=name
        self.last_name=last_name
        self.__monthly_salary=monthly_salary
    def getFullName(self):
        return self.name,self.last_name
    def annualSalary(self):
        annual_Salary=self.__monthly_salary*12
        if annual_Salary>100:
            print("High")
        else:
            print("Low")

Samvel=Employee("Samvel","Alexanyan",5)
Ruben=Employee("Ruben","Hayrapetyan",10)

Samvel.annualSalary()
Ruben.annualSalary()