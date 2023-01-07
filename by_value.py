list=[1,2,3,4,5,6]
dup_list= list[:] # this returns a new list 
dup_list[0]= 9
# because the refence is copied NOT the value
# [1,2,3,4,5,6]

print(list)


