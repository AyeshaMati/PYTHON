# marks=[93.5, 98.5, 34.6, 45.7, 99.6]   # list: can change (mutable)
# print(marks)
# print(type(marks))
# print(marks[1])

# student=["aisha", 46, "BGP"]
# student[0]="sara"  #change the list
# print(student)

# # Slicing
# marks=[83, 91, 76, 61, 48]
# print(marks[1:4])
# print(marks[-4:-2])

# list methods

# list=[2, 1, 3]
# list.append(4) #adds element
# print(list)

# list.sort() #sort in ascending order
# print(list)

# list.sort(reverse=True) #sort in descending order
# print(list)

# list.reverse() #reverse the list
# print(list)

# list.insert(1, 5) #inserting 5 at index 1
# print(list)

# list=[2, 1, 3, 1]
# # list.remove(1)  #remove first occurence of element
# # print(list) 

# list.pop(2)  #pop element at index 2
# print(list)

# Take 3 movies name from user
# movies=[]
# # movies.append(input("Enter 1st movie:")) can be used like this also
# mov=input("Enter 1st movie:")
# movies.append(mov)
# mov=input("Enter 2nd movie:")
# movies.append(mov)
# mov=input("Enter 3rd movie:")
# movies.append(mov)
# print(movies)

# checks if a list contain palindrome
list1=[1,2,1]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()
if(copy_list1==list1):
    print("palindrome")
else:
    print("not palindrome")