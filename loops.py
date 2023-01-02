#Initializing list variable
list=[1,2,3,4,5]
products=[]


def get_input():
    '''Ask for user enter any product '''
    val = input('Please enter your product : ')
    return  val

# using for loop
for element in list:
    print(element,'->',get_input())
else:
    print('-' * 20)