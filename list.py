def modify_list(arg_list):
    arg_list=arg_list+[60,70,80]
    print('Inside Function', arg_list)

i_list = [10,20,30,40,50]
print('Before calling a function',i_list)
modify_list(i_list)
print('After calling a function',i_list)

fhw= open('example.txt', 'w')
fhw.write('Written some thing')
print(fhw.tell())
print('closed ?', fhw.closed)
fhw.close()
print('after closing the file',fhw.closed)


tuple=(True,False)
print(tuple)
print(type(tuple))


def value(num1):
    list1=[]
    while num1!=0:
        if num1%2==0:
            list1.append(num1)
        else:
            break
        num1-=2
    print(list1)
value(10)



list1=[10,20,30,40,50]
list1.insert(7,25)
print(list1)


def find_sum(a,b):
    try:
        print(a+c)
    except:
        print('Function name error')
    finally:
        print('sum finally')
try:
    find_sum(12,13)
except:
    print('Invocation name error')
finally:
    print('Invocation finally')



set_1 = {1,2,3,4,1,2,4,5,3,8,9,7,10}

for index in range(len(set_1)):
    print(index,end='')


my_list=[0]*5
for index in range(1,5):
    my_list[index]=(index-1)*index
print(my_list)




def sample(value):
    sum1= 0
    for i in value:
        if i%2!=0:
            sum1+=value[i]
        else:
            sum1-=i
    print(sum1)
dict1={1:2,2:4,3:6,5:8}
sample(dict1)

sample_dict={'a':'apple','b':'ball'}
sample_dict.update({'b':'boy','c':'cat'})
print(sample_dict['a'],sample_dict.get('b'),sample_dict.get('c'))