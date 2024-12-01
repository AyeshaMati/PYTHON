# #def func_name(parameter1, parameter2)
# def calc_sum(a,b):
#     sum=a+b
#     print(sum)
#     return sum
# calc_sum(5,10)
# calc_sum(16,80)
# calc_sum(64,23)
#   return a+b
# sum=calc_sum(123,987) #function call
# print(sum)
    
# def print_hello():
#     print("Hello")

# print_hello()
# print_hello()
# print_hello()  

# #avg of 2 number
# def avg_num(a,b):
#     return (a+b)/2
# average=avg_num(4,9)
# print(average)

# # Built in functions
# print("apnacollege", end=" ") #sep=" "
# # print("shradhamaam") #end="\n"

# # User defined function
# # def cal_prod(a=1,b=2): # assigning default args
# def cal_prod(a,b=2): # this is valid
# # def cal_prod(a=1,b) #this is not valid 
#     print(a*b)
#     return a*b
# # cal_prod()
# cal_prod(3)

#practice
# cities=["delhi","gurgaon","noida","pune","mumbai","chennai"]
# heroes=["thor","ironman","captain america","shaktiman"]

# def print_len(list):
#     print(len(list))

# def print_list(list):
#     for item in list:
#         print(item, end=" ")  # to print items in same line  
# # print_len(cities)
# # print_len(heroes)
# print_list(heroes)         

# #factorial
# def calc_fact(n):
#     fact=1
#     for i in range(1,n+1):
#        fact*=i
#     print(fact)

# calc_fact(6)    

#convert usd to inr
# def converter(usd_val):
#     inr_val=usd_val*83
#     print(usd_val, "USD",inr_val, "INR")

# converter(100)

#func for even odd
def even_odd(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")
even_odd(4)   
even_odd(5)     
       
