list=[1,2,3,4,5,6]
dup_list= list # the list is not copied 
dup_list[0]= 9
# because the refence is copied NOT the value
# [9,2,3,4,5,6]
print(list)


