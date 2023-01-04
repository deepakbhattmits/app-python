simple_list =[1,2,3,4]

dup_list = [el*2 for el in simple_list if el%2==0]

print('duplicate list ',dup_list)

xs = [22, 13, 45, 50, 98, 69, 43, 44, 1]
xl= [x+1 if x%2==0 else x+5 for x in xs]
# [27, 18, 46, 51, 99, 70, 48, 49, 6]
print(xl)



a = 'q', 'r'
b = ('q')


# Iterate over a. If y not in b, print y.
# I want to see ['q'] printed.
eliminated0 = [ y for y in a if y in b ]
print('Eliminated : ', eliminated0)

# Iterate over a. If y not in b, print y.
# I want to see ['r'] printed.
eliminated1 = [ y for y in a if y not in b ]
print('Eliminated : ', eliminated1)

  