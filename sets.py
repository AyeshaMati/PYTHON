# collection={1,2,3,4, "hello", "world", "world"}  #unordered and ignore duplicate values
# print(collection)
# print(type(collection))
# print(len(collection))

# collection={} #empty dict not set
# collection=set() #empty set
# print(type(collection))

# # Set methods
# #set are mutable but the elements of set is immutable
# collection=set()
# collection.add(1) #add value
# collection.add(2) 
# collection.add("apnacollege")
# collection.add((1,2,3))
# # collection.add([1,2,3])  # lists are mutable gives error
# # collection.remove(1) #remove value
# collection.clear()
# print(len(collection))

# collection={"hello", "world", "apnacollege", "python"}
# print(collection.pop()) # pop any random value
# print(collection.pop())

# set1={1,2,3}
# set2={2,3,4}
# # print(set1.union(set2)) # union
# print(set1.intersection(set2))  #intersection
# print(set1)
# print(set2)

# #practice
#  subjects={
# "java", "python", "C++", "python", "javascipt", "java", "python", "java", "C++", "C"
# }
#  print(subjects)
#  print(len(subjects))

#  values={9, 9.0} 
#  values={9, "9.0"} 
#  print(values)

values={
  ("float", 9.0),    # adding tuples in set
  ("int", 9)
 }
print(values)