name='ABC'
age=20

formatted_str = "I am "+name+" and I am "+str(age)+" year old."

formatted_str_function = "I am {} and I am {} year old.".format(name,age)

formatted_str_function_index = "I am {0} and I am {1} year old. I really am named {0}".format(name,age)

formatted_str_function_reference = "I am {name} and I am {years} year old. I really am named {name}".format(name=name,years=age)
print(formatted_str)
print(formatted_str_function)
print(formatted_str_function_index)

print(formatted_str_function_reference)
funds = 123.9754
print('Funds : {}'.format(funds))#Funds : 123.9754
print('Funds : {:f}'.format(funds))#Funds : 123.975400
print('Funds : {:.1f}'.format(funds))#Funds : 124.0
print('Funds : {:10.1f}'.format(funds))#Funds :      124.0
print('Funds : {:>10.1f}'.format(funds))#Funds :      124.0 > align funds right 
print('Funds : {:<10.1f}'.format(funds))#Funds :124.0 < align funds left
print('Funds : {:^10.1f}'.format(funds))#Funds :   124.0 ^ align funds center
print('Funds : {:*^10.1f}'.format(funds))#Funds :   124.0 fill * symbol in empty space ^ align funds center