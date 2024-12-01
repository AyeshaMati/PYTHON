# class Student:
#     def __init__(self, name):
#         self.name=name

# s1=Student("aisha")
# del s1
# print(s1) #this will give error bcoz s1 is deleted.

# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no=acc_no
#         self.__acc_pass=acc_pass   #__ makes it private so that it cant be accessed outside class

#     def reset_pass(self):
#         print(self.__acc_pass)    

# acc1=Account("12345", "sfdggr")
# print(acc1.acc_no)    
# print(acc1.reset_pass())   

# class Person:
#     __name="anonymous"

#     def __hello(self):  #private method/func : cant be accessed outside class only internal func can access it
#         print("hello person")

#     def welcome(self):  #this func can call the private method i.e, __hello
#         self.__hello()    

# p1=Person()
# print(p1.welcome()) 

# Inheritance
# class Car:
#     color="black"
#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
        # print("car stopped")

# Single inheritance
# class ToyotaCar(Car):  # can access attr of Car class
    # def __init__(self, name):
    #     self.name=name

# car1=ToyotaCar("Mercedes")
# car2=ToyotaCar("Fortuner")
# print(car1.name)
# print(car1.color) 
# print(car1.start())   #start() can be used here in this class bcoz of inheritance 

# Multi-level inheritance    
# class ToyotaCar(Car):   
#     def __init__(self, brand):
#         self.brand=brand

# class Fortuner(ToyotaCar):  #can access attr of both ToyotaCar and Car class
#     def __init__(self, type):
#         self.type=type

# car1=Fortuner("diesel")
# print(car1.type)
# car1.start()     

# Multiple inheritance
# class A:
#     varA="welcome to class A"

# class B:
#     varB="welcome to class B"

# class C(A, B):
#     varC="welcome to class C"

# c1=C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)

# super method: used to access methods of the parent class 
# class Car:
#     def __init__(self, type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started")

#     @staticmethod
#     def stop():
#         print("car stopped")

# class ToyotaCar(Car):   
#     def __init__(self, name, type):
#         super().__init__(type)  # to access type method of Car(parent) class
#         self.name=name
#         super().start()

# car1=ToyotaCar("prius","electric")
# print(car1.type)

# class method:
# class Person:
#     name="anonymous"

#     # def changeName(self, name):
#     #    self.__class__.name="tom"

#     @classmethod    #to change the attr in class
#     def changeName(cls, name):
#         cls.name=name

# p1=Person()
# p1.changeName("tom")
# print(p1.name)
# print(Person.name)        
 
# Property
# class Student:
#     def __init__(self, phy, chem, math):
#         self.phy=phy
#         self.chem=chem
#         self.math=math
#         # self.percentage=str((self.phy+self.chem+self.math)/3) + "%"

#     # def calcPercentage(self):
#     #         self.percentage=str((self.phy+self.chem+self.math)/3) + "%" 

#     @property
#     def percentage(self):
#          return  str((self.phy+self.chem+self.math)/3) + "%"

# stu1=Student(98,97,96)
# print(stu1.percentage)

# stu1.phy=86   #change the phy marks the calc new %
# # stu1.calcPercentage()
# print(stu1.percentage)

# Polymorphism: operator overloading: when the same operator have diff meaning acc to context
# different meaning of '+' operator
print(1+2) #3
print("aisha" + "mati")  #concatenate
print([1,2,4] + [4,5,6])  #merge the list 

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +", self.img,"j")

    def __add__(self, num2):  # Dunder function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal, newImg)    

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

num3=num1 + num2
num3.showNumber()