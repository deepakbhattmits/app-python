list =[1,2,3,4,5,6]


def user_choice():
    val = input('Please enter your choice : ')
    return val


print('Please select your choice \nPress 1 for display list \nPress 2 for display greeting message\n Press q for quit')

choice=user_choice()
waiting_for_input =True

while waiting_for_input:
    if choice == '1':
        print(list)
    elif choice == '2':
        print('Hi there!')
    elif choice == 'q':
        waiting_for_input= False
    else:
        print('Invalid input, please pick from list')
print('Done')