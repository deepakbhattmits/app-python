from functools import reduce
numbers = [1,2,3,4,5,6]

sum = reduce(lambda sum,list_elm: sum+list_elm, numbers, 0)

print(f'Sum of the list {numbers} is {sum}')
