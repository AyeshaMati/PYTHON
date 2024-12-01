# info={
#     "key":"value",
#     "name":"aisha",
#     "learning":"coding",
#     "age":"22",
#     "is_adult":"True",
#     "subjects": ["python","C","Java"],
#     "tuple":("dict","set")
# }
# print(info)
# print(info["name"])
# print(info["age"])
# print(info["subjects"])
# info["name"]="hajra"
# info["surname"]="mati"  # dict is mutable i.e can change
# print(info)

# # null dict
# null_dict={}
# null_dict["name"]="Python"
# print(null_dict)

# nested dictionary
# student={
#     "name":"abdul",
#     "sub":{
#     "phy":97,
#      "chem":98,
#      "maths":90,

#  }
# }
# print(student)
# print(student["sub"]["chem"]) #only print chem marks

# dict methods
# print(student.keys()) #only print outer keys: name & sub
# print(student.values()) #print values
# print(list(student.keys())) # type cast intto list
# print(len(list(student.keys())))  #length of list
# print(student.items())
# pairs=list(student.items()) # return pairs
# print(pairs[0])
# print(student["name2"]) # error
# print(student.get("name2"))  #print none : used for finding key
# student.update({"city":"delhi"}) # update the dict
# print(student) 

#practice{}
# dict={
# "cat":"a small animal",
# "table":("a furniture", "list of facts")
# }
# print(dict)

marks={}
x=int(input("enter phy:"))
marks.update({"phy":x})
y=int(input("enter chem:"))
marks.update({"chem":y})
print(marks)






