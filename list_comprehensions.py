# List comprehension is an elegant way to define and create lists based on existing lists.
# List comprehension is generally more compact and faster than normal functions and loops for creating list. 

simple_list = [1,2,3,4,5,6]

doubled_list =[]

for element in simple_list:

    doubled_list.append(element*2)
else:

    print('**'*20)

    print('Doubled List : ',doubled_list)

# using list comprehension

simple_list_comprehensions = [1,2,3,4,5,6]

doubled_list_comprehensions =[]

doubled_list_comprehensions=[el*2 for el in simple_list_comprehensions]

print('list comprehensions : ',doubled_list_comprehensions)

# using list comprehension with join

simple_list_comprehensions = [1,2,3,4,5,6]

doubled_list_comprehensions =[]

doubled_list_comprehensions='-'.join([str(el*2) for el in simple_list_comprehensions])

print('list comprehensions with join : ',doubled_list_comprehensions)

