numbers = [2, 4, 6, 8, 10]

# returns square of a number
def square(number):
  return number * number

# apply square() function to each item of the numbers list
# map function will take 2 arguments first is the reference of that function what we want to apply and second argument is the iterable like list , tuple etc.
squared_numbers_iterator = map(square, numbers)

# converting to list
squared_numbers = list(squared_numbers_iterator)
print('Numbers are  ' , numbers, 'Square of numbers are ', squared_numbers)

# Output: [4, 16, 36, 64, 100]