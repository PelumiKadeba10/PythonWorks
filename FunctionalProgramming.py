# lambda: Creating functions as short as possible
print((lambda x: x * x)(5))


# map and filter: must be converted to list to be printed
# map: takes a function and iterable(e.g. list) as arguments
def add_five(x):
    return x + 5


nums = [11, 22, 33, 44, 55]
result = set(map(add_five, nums))
# Add_five is the function, nums is the list
print(result)

# filter:  filters an iterable by leaving only things that match the condition
nums = [1, 2, 5, 8, 3, 7]
res = list(filter(lambda x: x < 5, nums))
print(res)


# Generators: like lists or tuples, iterable with for loops
def countdown():
    p = 5
    while p > 0:
        yield p
        p -= 1


for i in countdown():
    print(i)

# Exceptions
# using assert keyword
# pp = int(input('Enter your number: '))
# assert (0 >= pp), 'Your number is negative'

# Decorators: provide a way to modify functions using other functions.
def decor(func):
    def wrap():
        print("============")
        print(func)
        print("============")
    return wrap


def print_text():
    print("Hello world!")


decorated = decor(print_text)
decorated();


# Recursion:functions calling themselves
def convert(num):
   if num == 1:
      return num
   return (num % 2 + 10 * convert(num // 2))


inp = int(input())
print(convert(inp))

# args and kwargs
# Using *args as a function parameter enables you to pass an arbitrary number of arguments to that function.
# The arguments are then accessible as the tuple args in the body of the function.
def function(named_arg, *args):
    print(named_arg)
    print(args)

function(1, 2, 3, 4, 5)

# Try and except
try:
    variable = 10
    print(variable + "hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except (ValueError, TypeError):
    print("Error occurred")

try:
  print(1)
  print(1 + "1" == 2)
  print(2)
except TypeError:
  print(3)
else:
  print(4)
