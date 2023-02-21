class Car:
    #using constructor
    def __init__(self,name="hyundai",fuel="CNG"):
        self.name = name
        self.fuel = fuel



    def mileage(self):     ##methods
        print("the car gives mileage of 40",self.name)

car1 = Car('maruti','petrol')
# car1.name = 'maruti'
# car1.fuel = 'petrol'

print("Car name is",car1.name,"It runs using",car1.fuel)
car1.mileage()

#abstraction, encapsulation, inheritance, polymorphism

#base /parent / super - properties
#child class / sub class /  derived class - inherit properties of parent class
# code reuseability

#single inheritance
class vehicle():
    def v_info(self):
        print("vehicle class")

class car(vehicle):
    def c_info(self):
        print("car class")

car1 = car()
print(car1.v_info())

#multiple inheritance

class person():
    def p_info(self,name,age):
        self.name = name
        self.age = age
        print("Name is",self.name,"age is ",self.age)


class company():
    def c_info(self,c_name,location):
        self.c_name = c_name
        self.location = location
        print("company name is",self.c_name,"located in ",self.location)

class emp(person,company):
    def emp_info(self,department,salary):
        self.department = department
        self.salary = salary
        print("works in",self.department,"earns salary of",self.salary)

ep1 = emp()
ep1.p_info()
ep1.c_info()
ep1.emp_info()

#multilevel inheritance - A =parent class  B = child class of A, C = child class of B
#hiearchical inheritance - A = parent class B = child clas of A, C = child class of A , D = child class of A
#hybrid - A=p class, B=c class of A, C = c class of A, D = c class of both B and C

