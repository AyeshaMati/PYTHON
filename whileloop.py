# while True:    #infinte loop
    # print("hello")

# count=1
# while count<=5:
#     print("hello")
#     count+=1 

#print nos from 1 to 5 and 5 to 1
# i=1
# i=5
# # while i<=5:
# while i>=1:
#     print(i)
#     i-=1

#practice
# n=int(input("enter number"))
# i=1
# while i<=10:
#     print(n*i) # table of any num
#     # print(3*i) # table of 3
#     i+=1

# num=[1,4,9,16,25,36,49,64,81,100]
# without loop
# print(num[0])
# print(num[1])
# print(num[2])
# print(num[3])
# using loop
# traversing
# idx=0
# while idx<len(num): 
#    print(num[idx]) #gives values at index
#    print(idx) #gives index
#    idx+=1

# num=(1,4,9,16,25,36,49,64,81,100)
# x=36
# idx=0
# while idx<len(num):
#    if(num[idx]==x):
#       print("found at index", idx) 
# #    print(num[idx]) #gives values at index
# #    print(idx) #gives index
#    idx+=1

 # break
# i=1
# while i<=5:
#       print(i)
#       if(i==3):
#          break
#       i+=1

# continue
# i=0
# while i<=5:
#     if(i==3):
#         i+=1
#         continue  #skip the iteration i.e 3 wont print
#     print(i) 
#     i+=1

# i=1
# while i<=10:
#     if(i%2==0):
#         i+=1
#         continue
#     print(i)
#     i+=1

#sum of first n natural number
# n=7
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
# print("total sum :", sum)

#factorial of first n number
n=5
fact=1
i=1
while i<=n:
    fact*=i
    i+=1
print("factorial is:", fact)    

