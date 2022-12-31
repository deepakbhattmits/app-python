list =[1,2,3,4,5,6]


def user_choice():
    val = input('Please enter your choice : ')
    return val


print('Please select your choice ')
print('Press 1 for display list ')
print('Press 2 for display greeting message')
choice=user_choice()
if choice == '1':
    print(list)
elif choice == '2':
    print('Hi there!')
else:
    print('Invalid input, please pick from list')