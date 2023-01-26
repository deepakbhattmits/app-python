def modify_list(arg_list):
    global i_list
    arg_list
    arg_list=arg_list+[60,70,80]
    print('Inside Function', arg_list)
# ***************************************************************************
i_list = [10,20,30,40,50]
print('Before calling a function',i_list)
modify_list(i_list)
print('After calling a function',i_list)
# Before calling a function [10, 20, 30, 40, 50]
# Inside Function [10, 20, 30, 40, 50, 60, 70, 80]
# After calling a function [10, 20, 30, 40, 50]

# ***************************************************************************
fhw= open('example.txt', 'w')
fhw.write('Written some thing')
#this will tell us how many characters present in the file
print(fhw.tell())
# closed is boolean flag this will tell us file is closed or not well file will close with close() method
print('closed ?', fhw.closed)
fhw.close()
print('after closing the file',fhw.closed)

# ***************************************************************************
# by default tupple will take second argument empty
# if we add second place then we can see type of tuple
tuple=(1)
tuple1 =(1,True)
print(tuple)
# <class 'int'>
print(type(tuple))

# tuple example
print(tuple1)
# <class 'tuple'>
print(type(tuple1))





# ***************************************************************************
def value(num1):
    list1=[]
    while num1!=0:
        if num1%2==0:
            list1.append(num1)
        else:
            break
        num1-=2
    print(list1)
    #[10,8,6,4,2]
value(10)


# ***************************************************************************

list1=[10,20,30,40,50]
list1.insert(7,25)
# [10,20,30,40,50,25]
print(list1)


# ***************************************************************************
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

# Function name error
# sum finally
# Invocation finally

# ***************************************************************************
set_1 = {1,2,3,4,1,2,4,5,3,8,9,7,10}
# set will remove duplicate entry from list 
print(set_1)
for index in range(len(set_1)):
    print('-',index,end='\n')


# ***************************************************************************
my_list=[0]*5
print('[0]*5 : ',my_list)
# range will accept 2 arguments start, end it will create array of list [start-1,......,end-1]
for index in range(1,5):
    my_list[index]=(index-1)*index

# [0,0,2,6,12]
print(my_list)


# ***************************************************************************


def sample(value):
    sum1= 0
    for i in value:
        if i%2!=0:
            sum1+=value[i]
        else:
            sum1-=i
    print(sum1)#14
dict1={1:2,2:4,3:6,5:8}
sample(dict1)


# ***************************************************************************

sample_dict={'a':'apple','b':'ball'}
sample_dict.update({'b':'boy','c':'cat'})
# apple boy cat
print(sample_dict['a'],sample_dict.get('b'),sample_dict.get('c'))

# ***************************************************************************