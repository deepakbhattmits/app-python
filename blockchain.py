
# Initialize blockchain variable
blockchain=[]


def last_blockchain_value():
    '''Get last index value'''
    return blockchain[-1]


def add_value(transaction_value:float,last_value:float=[1]):
    '''Append value to blockchain variable
    
    Arguments:
        :transaction_value: transaction_value should be added 
        :last_value: last blockchain transaction (default:1)
    '''
    blockchain.append([last_value,transaction_value])

def get_input():
    '''Returns the input of the user as a float'''
    tx_amount = float(input('Please enter your transaction amount :'))
    return tx_amount


tx_amount = get_input()

add_value(tx_amount)


tx_amount = get_input()
add_value(tx_amount, last_blockchain_value())


tx_amount = get_input()
add_value(tx_amount, last_blockchain_value())


tx_amount = get_input()
add_value(tx_amount, last_blockchain_value())


print(blockchain)