# num=[1,2,3,4]
# for val in num:
#     print(val) 

# str="aisha mati"
# for char in str:
#     print(char)
# else:
#     print("end")

num=[1,4,9,16,25,36,49,64,81,100,49]
x=49
idx=0
for el in num:
    if(el==x):
        print("number found at idx",idx)
        break  # found only 1st 49 and break
    idx+=1

#practice
 #factorial of a number
n=5
fact=1
for i in range(1,n+1):
     
     fact*=i
print("factorial is :", fact)    
