# creating class
# class Student:
#     name="sara"

# s1=Student() #object
# # print(s1)
# print(s1.name)

# s2=Student()
# print(s2.name)

# class Car:
#     color="blue"
#     brand="Merccedes"
# car1=Car()
# print(car1.color)
# print(car1.brand)

# class Student:
    # # default constructor
#     # def __init__(self):
#     #              pass
#     college="ABC"  #same for every student
#     name="anonymous"  #class attribute
#     # parametrized constructor
#     def __init__(self,name,marks): # Constructor: python by default create it if we dont create it
#         self.name=name      # obj attribute > class attribute
#         self.marks=marks    # self is a reference to the current instance of a class
#         print("adding new student in database")
# s1=Student("hajra", 97)
# print(s1.name,s1.marks)
# s2=Student("sara", 89)
# print(s2.name,s2.marks)
# # print(s2.college)
# print(Student.college)

# Methods: function that belongs to object
# class Student:
#     def __init__(self,name,marks):
#         self.name=name      
#         self.marks=marks    
#     def welcome(self):  #method
#             print("welcome students")
#     def get_marks(self):  #method
#          return self.marks
# s1=Student("hajra", 97)
# s1.welcome()
# print(s1.get_marks())

#practice
# class Student:
#    def __init__(self,name,marks):
#        self.name=name      
#        self.marks=marks 
#    def get_avg(self):
#        sum=0
#        for val in self.marks:
#            sum+=val

#        print("hi",self.name,"avg score is:",sum/3)
# s1=Student("tony stark", [98,99,97])
# s1.get_avg() 
# s1.name="tom"
# s1.get_avg() 

class Account:
    def __init__(self, bal, acc):
        self.balance=bal
        self.account_no=acc

    #debit
    def debit(self, amount):
        self.balance-=amount
        print("Rs.",amount, "was debited ")
        print("total balance:", self.get_balance())

    #credit
    def credit(self, amount):
        self.balance+=amount
        print("Rs.", amount, "was credited ")  
        print("total balance:", self.get_balance())       

    def get_balance(self): 
        return self.balance   
           
acc1=Account(10000, 12345)
# print(acc1.balance)        
# print(acc1.account_no)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)

# Static methods: dont use self parameter(work at class level)
# class Student:
#    def __init__(self,name,marks):
#        self.name=name      
#        self.marks=marks 
#    @staticmethod  #decorator 
#    def hello():
#        print("hello")    
#    def get_avg(self):
#        sum=0
#        for val in self.marks:
#            sum+=val

#        print("hi",self.name,"avg score is:",sum/3)
# s1=Student("tony stark", [98,99,97])
# s1.get_avg() 
# s1.name="tom"
# s1.get_avg() 
# s1.hello()
      
# # Abstraction: hiding the implementation details of a class and only showing the essential features to the user
# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started...") 

# car1=Car()
# car1.start()           

# Encapsulation: wrapping data and function into a single unit(object)





