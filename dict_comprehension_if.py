list= [('A',29),('B',30),('C',31)]
dict = {key:value for (key,value) in  list if key == 'B' and value>=30}
print('Dict list : ',dict)