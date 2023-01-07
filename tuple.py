# A tuple is a built-in data structure in Python that is an ordered collection of objects. Unlike lists, tuples come with limited functionality.

# The primary differing characteristic between lists and tuples is mutability. Lists are mutable, whereas tuples are immutable. 
# this is the use case of person name, age, here we can omit flower braces

tuple_without_braces ='Deepak',29
print('',tuple_without_braces)

#  if we want to use flower braces lets say we want to send only onw value then we can use ()
tuple_with_braces = ('Puji ', )
print(tuple_with_braces)

list_comp = [el for el in tuple_with_braces ]
print(' list comp : ',list_comp)
for el in tuple_with_braces:
    print(el)
else:
    print('Done loop')
tuple_for_indexing=('ABC','XYZ','MNB')
print(' Indexing: ',tuple_for_indexing[0])
a,b,c = tuple_for_indexing
print('Unpacking : \n')
print('a', a)
print('b', b)
print('c', c)