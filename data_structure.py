simple_list =[1,2,3,4]
simple_list.extend([5,6,7,8])
print(simple_list)

d= {'name':'ABC','age':50}
print(d.items())
for k,v in d.items():
    print(k,v)
d_list_comp= [(k,v) for (k,v) in d.items()]
print('d_list_comp', d_list_comp)
print('d_indexing', d['name'])
print('Dict_unpacking : ')
k,v= d.items()
print(k,v)

t='a','s','d'

print(t.index('s'))
s= {'ABC','CDE','FGH'}

