
# Initialize blockchain variable
blockchain=[]


def last_blockchain_value():
    '''Get last index value'''
    if len(blockchain)<1:
        return None
    return blockchain[-1]


def add_transaction(transaction_value:float,last_value:float=[1]):
    '''Append value to blockchain variable
    
    Arguments:
        :transaction_value: transaction_value should be added 
        :last_value: last blockchain transaction (default:1)
    '''
    if last_value==None:
        last_value =[1]
    blockchain.append([last_value,transaction_value])


def get_transaction_value():
    '''Returns the input of the user as a float'''
    tx_amount = float(input('Please enter your transaction amount :'))
    return tx_amount


def print_blockchain_elements():
    for block in blockchain:
        print('Outputting block : ')
        print(block)
    else:
        print('*'*20)
        print('Final blockchain : \n',blockchain)


def get_user_choice():
    choice =input('Please choose :')
    return choice

def verify_chain():
    is_valid= True
    for block_index in range(len(blockchain)):
        if block_index ==0:
            continue
        elif blockchain[block_index][0]==blockchain[block_index -1]:
            is_valid= True
        else:
            is_valid = False
            break
    # block_index = 0
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index+=1
    #         continue
    #     elif block[0]==blockchain[block_index -1]:
    #         is_valid= True
    #     else:
    #         is_valid = False
    #         break
    #     block_index+=1
    return is_valid
waiting_for_input =True
while waiting_for_input:
    print('Please choose\nPress 1 for add new transaction value\nPress 2 for output the blockchain blocks\nPress h to manipulate chain\nPress q for quit')
    user_choice= get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, last_blockchain_value())
    elif user_choice=='2':
        print_blockchain_elements()
    elif user_choice=='h':
        if len(blockchain)>= 1:
            blockchain[0]= [2]
    elif user_choice=='q':
        waiting_for_input=False
    else:
        print('Invalid choice, please pick value from list')
    if not verify_chain():
        print('Invalid blockchain')
        break

print('Done')

    