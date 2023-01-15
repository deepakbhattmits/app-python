file=open('example.txt', mode='r+')
# read whole contents of file
# f_contents=file.readlines()
# print('whole content',f_contents)
# for line in f_content:
#     print(line[:-1])
# else:
#     print('- '*5,'Loop done!','- '*5)

# file.write('Hello this is from python\n')

# read one line from file 

line= file.readline()
while line:
    print(line)
    line=file.readline()
else:
    print('Loop done!')
file.close()


# example by with keyword
with open('example.txt', mode='r+') as f:
# read whole contents of file
# f_contents=file.readlines()
# print('whole content',f_contents)
# for line in f_content:
#     print(line[:-1])
# else:
#     print('- '*5,'Loop done!','- '*5)

# file.write('Hello this is from python\n')

# read one line from file 

    line= f.readline()
    while line:
        print(line)
        line=file.readline()
    else:
        print('Loop done!')