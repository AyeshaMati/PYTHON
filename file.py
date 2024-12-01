# reading a file
# f=open("demo.txt", "rt") 
# # data=f.read(5) # reads only 5 letters
# line1=f.readline() #reads one line at a time
# line2=f.readline()
# # print(data)
# print(line1) 
# print(line2)
# # print(type(data))
# f.close()

# writing a file: this will change the data in demo.txt file
# f=open("demo.txt", "w")
# f.write("I want to learn Python today")
# f.close()

# #append: add the data to the file
# f=open("demo.txt", "a")
# f.write("\nThen I will move to DSA")
# f.close()

# overwrite
# f=open("demo.txt", "r+")
# f.write("you")
# print(f.read()) # read after the pointer reaches after over write
# f.close()    

# f=open("demo.txt", "w+")  #truncate the whole data
# print(f.read())
# f.write("abc")
# f.close()

# "with" syntax
# with open("demo.txt", "r") as f: # with keyword automatically closes the file
#     data=f.read()
#     print(data)

# with open("demo.txt", "w") as f:
#       f.write("new data")

# creating a file
# f=open("sample.txt","w")
# f.close()     

# Deleting a file
# import os 
# os.remove("sample.txt") 

# practice
# with open("practice.txt", "w") as f:
#      f.write("we are learning Python\n")
#      f.write("using java\n like programming in java")   

# with open("practice.txt", "r") as f:  
#    data=f.read()
# new_data=data.replace("java","Python")
# print(new_data)      

# with open("practice.txt", "w") as f:  # over write
#     f.write(new_data)
# def check_for_word():  #find the word
#   word="learning"
#   with open("practice.txt", "r") as f:  
#     data=f.read()
#     if(word in data):
#       print("found")
#     else:
#       print("not found") 

# check_for_word() 
    
# def check_for_line():  #at which line the word exists
#   word="learning"
#   data=True
# #   line_no=1
#   with open("practice.txt", "r") as f:
#      while data:
#        data=f.readline()
#        if(word in data):
#          print(line_no)
#          return
#        line_no+=1 

#   return -1  
# print(check_for_line())

count=0
with open("practice.txt", "r") as f:
  data=f.read()
  print(data) 

  # num=""
  # for i in range(len(data)):
  #   if(data[i]==","):
  #     print(num)
  #     num=""
  #   else:
      # num+=data[i]
  num=data.split(",") # numbers in a list
  for val in num:
    if(int(val)%2==0):
      count+=1
  print(count)

  