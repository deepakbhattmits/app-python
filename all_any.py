list = [True,True,False]

print('any : ',any(list))

print('all : ',all(list))
print('*'*20)
simple_list=[1,2,3,4,-5,6,7,-8]

print('simple_list check with any and all :',simple_list)

dup_list=[el>0 for el in simple_list]

print('dup_list with boolean :',dup_list)
print('any :',any(dup_list))
print('all :',all(dup_list))