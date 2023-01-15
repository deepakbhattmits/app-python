from hashlib import sha256

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

format_string_f= f'I am {name} and I\'m {age} years old'

format_string_f_with_float= f'I am {name} and I\'m {age:.2f} years old'
print('format_string_f : ', format_string_f)
print('format_string_f_with_float : ', format_string_f_with_float)
person = {'name': 'Eric', 'age': 74}
print("Hello, {name}. You are {age}.".format(** person))

list =[1,2,3,4,5]

print("List have {}, {}, {} and {}".format(*list))

hashed_var= sha256(name.encode()).hexdigest()
print("hashed_var : ",hashed_var)

