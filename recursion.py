# Recursion: when a fuction calls itself repeatedly
# def show(n):
#     if(n==0): #base case
#         return
#     print(n)
#     show(n-1)

# show(5)

# # factorial 
# def fact(n):
#     if(n==1 or n==0):
#      return 1
#     return n*fact(n-1)
   
# print(fact(4))

#Practice
# # sum of first n natural num
# def calc_sum(n):
#    if(n==0):
#       return 0
#    return calc_sum(n-1)+n
# sum=calc_sum(5)   
# print(sum)

def print_list(list, idx=0):
   if (idx==len(list)):
     return
   print(list[idx])
   print_list(list, idx+1)
fruits=["mango", "apple", "litchi"]   
print_list(fruits)