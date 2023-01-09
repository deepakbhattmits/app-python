# function declration
def pow(a:int,b:int):
    """Function will takes 2 arguments both should be integer"""
    output= 'Output of',a,'**',b,'=', a**b
    return output

# call function
print(pow(2,3))

# unpacking arguments with *
def unlimited_arg(*args):
    print('Arguments are :', args)
    for el in args:
        print(el)
    else:
        print('**'*20)

unlimited_arg(1,2,3,4)



list =[1,2,3,4,5]

print("List have {}, {}, {} and {}".format(*list))



obj ={'name':'ABC','age': 20, 'address':'BLR'}
print("Hi I\'m {name} I\'m {age} years old I\'m going fr trip to {address} ".format(**obj))

def unlimited_dict_args(**args):
    print('unlimited_dict_args :',args)
    # for k,v in args.items():
    #     print(k,v)
    # else:
    #     print('Done!')
    return ">>>>Hi I\'m {name} I\'m {age} years old I\'m going fr trip to {address} ".format(**args)


print(unlimited_dict_args(name='ABC',age=20,address='BLR'))