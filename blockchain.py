
# Initialize blockchain variable
blockchain=[]


def last_blockchain_value():
    '''Get last index value'''
    if len(blockchain)<1:
        return None
    return blockchain[-1]


def add_value(transaction_value:float,last_value:float=[1]):
    '''Append value to blockchain variable
    
    Arguments:
        :transaction_value: transaction_value should be added 
        :last_value: last blockchain transaction (default:1)
    '''
    blockchain.append([last_value,transaction_value])


def get_transaction_value():
    '''Returns the input of the user as a float'''
    tx_amount = float(input('Please enter your transaction amount :'))
    return tx_amount


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block : ')
        print(block)


def get_user_choice():
    choice =input('Please choose :')
    return choice

tx_amount = get_transaction_value()

add_value(tx_amount)

while True:
    print('Please choose\nPress 1 for add new transaction value\nPress 2 for output the blockchain blocks\nPress q for quit')
    user_choice= get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(tx_amount, last_blockchain_value())
    elif user_choice=='2':
        print_blockchain_elements()
    elif user_choice=='q':
        break
    else:
        print('Invalid choice, please pick value from list')


print('Done')

    