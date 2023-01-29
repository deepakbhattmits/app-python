
from functools import reduce
from json import dumps, loads
# from pickle import dumps, loads
from collections import OrderedDict


from hash_util import hash_block, hash_string_256
# Initialize blockchain variable
MINING_REWAD = 10
genesis_block={
        'previous_hash': '',
        'index':0,
        'transactions':[],
        'proof':100
    }
blockchain=[genesis_block]
open_transactions=[]
owner = 'ABC'
participants ={owner}


def load_data():

    # with open('blockchain.p',mode='rb') as f:
    #     file_contents = loads(f.read())
    #     global blockchain, open_transactions
    #     blockchain= file_contents['chain']
    #     open_transactions =file_contents['ot']
    try:
        with open('blockchain.txt',mode='r') as f:
            file_contents = f.readlines()
            global blockchain, open_transactions
            blockchain = loads(file_contents[0][:-1])
            updated_blockchain=[]
            for block in blockchain:
                updated_block={
                        'previous_hash':block['previous_hash'],
                        'index':block['index'],
                        'proof':block['proof'],
                        'transactions':[OrderedDict([
                            ('sender',tx['sender']),
                            ('recipient',tx['recipient']),
                            ('amount',tx['amount'])]) for tx in block['transactions']]
                    }
                updated_blockchain.append(updated_block)
            blockchain= updated_blockchain
            open_transactions = loads(file_contents[1])

            updated_open_transactions=[]
            for tx in open_transactions:
                updated_open_transaction=OrderedDict([
                            ('sender',tx['sender']),
                            ('recipient',tx['recipient']),
                            ('amount',tx['amount'])]) 
                updated_open_transactions.append(updated_open_transaction)
            open_transactions= updated_open_transactions
    except IOError:
        print('File not found !')
    finally:
        print('Cleanup')

load_data()


def save_data():
    try:    
        with open('blockchain.txt',mode='w') as f:
            f.write(dumps(blockchain))
            f.write('\n')
            f.write(dumps(open_transactions))
        # with open('blockchain.p',mode='wb') as f:
        #     save_data= {
        #         'chain':blockchain,
        #         'ot':open_transactions
        #     }
        #     f.write(dumps(save_data))
    except IOError:
        print('Saving failed !')
    finally:
        print('Cleanup!')


def sender_balance(participant):
    tx_sender=[[tx['amount'] for tx in block['transactions'] if tx['sender']== participant]for block in blockchain]
    open_tx_sender=[tx['amount'] for tx in open_transactions if tx['sender']== participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum,tx_amt: tx_sum+sum(tx_amt) if len(tx_amt)>0 else tx_sum+ 0, tx_sender,0)
    # amount_sent=0
    # for tx in tx_sender:
    #     if len(tx)>0:
    #         amount_sent+=tx[0]
    return amount_sent


def recipient_balance(participant):
    tx_recipient= [[tx['amount'] for tx in block['transactions']if tx['recipient']== participant]for block in blockchain]
    amount_received = reduce(lambda tx_sum,tx_amt: tx_sum+sum(tx_amt) if len(tx_amt)>0 else tx_sum+0, tx_recipient,0)
    # amount_received = 0
    # for tx in tx_recipient:
    #     if len(tx)>0:
    #         amount_received+=tx[0]
    return amount_received

def get_balance(participant):
    sender_bal=sender_balance(participant)
    recipient_bal=recipient_balance(participant)
    total = recipient_bal- sender_bal
    return total

def last_blockchain_value():
    '''Get last index value'''
    if len(blockchain)<1:
        return None
    return blockchain[-1]


# def add_transaction(transaction_value:float,last_value:float=[1]):
#     '''Append value to blockchain variable
    
#     Arguments:
#         :transaction_value: transaction_value should be added 
#         :last_value: last blockchain transaction (default:1)
#     '''
#     if last_value==None:
#         last_value =[1]
#     blockchain.append([last_value,transaction_value])

def verify_transaction(transaction):
    tx_sender_balance= get_balance(transaction['sender'])
    return  tx_sender_balance >= transaction['amount']
     



def add_transaction(recipient, sender=owner, amount=1.0):
        '''Append value to blockchain variable
    
    Arguments:
        :sender: The sender of coins(default:owner)
        :recipient: The recipient of coins
        :amount: The amont of coins sent with the transaction (default:1)
    '''
        # transaction={
        #     'sender':sender,
        #     'recipient':recipient,
        #     'amount':amount
        #     }
        transaction= OrderedDict([('sender',sender),('recipient',recipient),('amount',amount)])
        if verify_transaction(transaction):
            open_transactions.append(transaction)
            participants.add(sender)
            participants.add(recipient)
            save_data()
            return True
        else:
            return False





def valid_proof(transaction, last_hash, proof):
    guess = (str(transaction)+str(last_hash)+ str(proof)).encode()
    guess_hash=hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2]=="00"

def proof_of_work():
    last_block= blockchain[-1]
    last_hash= hash_block(last_block)
    proof=0
    while not valid_proof(open_transactions, last_hash, proof):
        proof+=1
    return proof

def mine_block():
    last_block= blockchain[-1]

    hashed_block=hash_block(last_block)
    proof= proof_of_work()
    # reward_transaction={
    #     'sender':'MINIG',
    #     'recipient':owner,
    #     'amount':MINING_REWAD
    # }
    reward_transaction = OrderedDict([( 'sender','MINIG'),('recipient',owner),('amount',MINING_REWAD)])
    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)

    block={
        'previous_hash': hashed_block,
        'index':len(blockchain),
        'transactions':copied_transaction,
        'proof':proof
    }
    blockchain.append(block)
    return True


def get_transaction_value():
    '''Returns the input of the user as a float'''
    tx_recipient = input('Enter recipient of the transaction : ')
    tx_amount = float(input('Enter your transaction amount : '))
    return tx_recipient,tx_amount


def print_blockchain_participants():
    print(participants)

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
    for(index, block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index -1]):
            return False
        if not valid_proof(block['transactions'][:-1],block['previous_hash'],block['proof']):
            print('Proof of work is invalid')
            return False
    return True

def verify_transactions():
   return all([verify_transaction(tx) for tx in open_transactions])


# def verify_chain():
#     is_valid= True
#     for block_index in range(len(blockchain)):
#         if block_index ==0:
#             continue
#         elif blockchain[block_index][0]==blockchain[block_index -1]:
#             is_valid= True
#         else:
#             is_valid = False
#             break
#     block_index = 0
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
    # return is_valid


waiting_for_input =True
while waiting_for_input:
    print('Please choose\nPress 1 for add new transaction value\nPress 2 for mine block\nPress 3 for output the blockchain blocks\nPress 4 to output participants\nPress 5 to check transaction validity\nPress h to manipulate chain\nPress q for quit')
    user_choice= get_user_choice()
    if user_choice == '1':
        # tx_amount = get_transaction_value()
        # add_transaction(tx_amount, last_blockchain_value())
        tx_data = get_transaction_value()
        recipient,amount = tx_data
        if add_transaction(recipient, amount=amount):
            print('Transaction Added!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice=='2':
        if mine_block():
            open_transactions= []
            save_data()
    elif user_choice=='3':
        print_blockchain_elements()
    elif user_choice=='4':
        print_blockchain_participants()
    elif user_choice=='5':
        if verify_transactions(): 
            print('All transaction are valid')
        else:
            print('There are invalid transaction')
    elif user_choice=='h':
        if len(blockchain)>= 1:
            blockchain[0]= {
        'previous_hash': '',
        'index':0,
        'transactions':[{'sender':'ABC','recipient':'CDE', 'amount':1000}]
    }
    elif user_choice=='q':
        waiting_for_input=False
    else:
        print('Invalid choice, please pick value from list')
    if not verify_chain():
        print('Invalid blockchain')
        break
    remaining_balance= 'Balance of {} : {:6.2f}'.format('Max' , get_balance('ABC'))
    print(remaining_balance)

print('Done')

    