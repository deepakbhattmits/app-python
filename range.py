list =5
arr = [1,2,3,4,5]

for element in range(list):
    print(element)
else:
    print('*'* 20)



for element in range(len(arr)):
    print('index : ', element, 'value :',arr[element],'\n')
else:
    print('value of arr : ',arr)
    print('-*-'* 20)