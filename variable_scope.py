# Global variable
name='Deepak'


def get_name():
    # global name
    name =input('Please enter your name :')
    return name 

# this will print local variable value
print(get_name())


# this will print global variable value
print(name)