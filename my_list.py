# an emty list
my_list = []
# append elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)
# inserting an element
my_list.insert(1, 15) # insert 15 at index 1
# extending the list 
my_list.extend([50, 60, 70]) # extend with multiple elements
#remove the last element
my_list.pop() # removes 70
# sort in assending order
my_list.sort()
# find and print index of an element
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)