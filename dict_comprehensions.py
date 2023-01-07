# list =[('ABC',29),('XYZ',30),('MNO',31)]
list =[{'name','XYZ'},{'age',30},{'address','NS street'}]

dict_comprehension = {key :value for (key, value) in list}

print('Dictionary Comprehension : ', dict_comprehension)