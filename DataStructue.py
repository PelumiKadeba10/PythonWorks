# These contain usages of some concepts and structures
# Dictionary --> 19 - 31
# Sets --> 33 - 44
# Strings --> 46 - 85
# Collections --> 87 - 102
# Other Data-types ---> 104 - 142
import sys
from typing import Dict
from timeit import default_timer as timer
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

my_list = []
my_tuple = 'hello'
print(sys.getsizeof(my_list))
print(sys.getsizeof(my_tuple))

# Dictionary
my_dict = {'name': 'Pulumi', 'age': 30, 'city': 'Lagos'}
my_dict2 = my_dict.copy()
# pop-item removes the last element in  the dictionary
my_dict.popitem()
print(my_dict)
# pop takes keys as arguments and removes that key
my_dict.pop('name')
print(my_dict)
for value in my_dict2.values():
    print(value)
for key, value in my_dict2.items():
    print(key, ':', value)

# Sets are unordered, mutable and have no duplicates
myset = {1, 2, 3, 4, 2}
print(myset)
myset2 = myset.copy()
print(myset2)
print(type(myset2))
odd = {1, 3, 5, 7}
even = {2, 4, 6, 8}
prime = {2, 3, 5, 7}
u = odd.union(even)
i = odd.intersection(even)
print(u, 'and', i)

# strings are ordered, immutable and used for text representation
my_string = " Hello World"
print(my_string[0])
# Reversing a string
print(my_string[::1])
# removing space before and after a string but nt touching the string itself
my_string2 = my_string.strip()
print(my_string2)
# splitting a string: uses argument to split the string
lpp = my_string2.split()
print(lpp)
# Joining a string: uses argument to join the list
lpp2 = ''.join(lpp)
print(lpp2)
# to check how long a program runs for
# test1
start = timer()
print(['a'] * 6)
stop = timer()
print('test 1 time:', stop - start)
# test2
start = timer()
lisd = ['a'] * 6
print(lisd)
stop = timer()
print('test 2 time:', stop - start)
# Format string with %: (%s --> strings), (%d --> integers), (%f --> floats(6 digits))
# .xf is for x decimal places
name = "Pelumi"
out = "my name is %s" % name
print(out)
num = 22 / 7
print('p is %d' % num)
print('p is %f' % num)
print('p is %.10f' % num)
# Formatting string using format()
print('my name is {}'.format(out))
print('pi is {:.2f} and {}'.format(num, out))
# Formatting string using f-string...__float__ converts num to a float
print(f'pi is {num.__float__()} and {out}')

# Collections:Counter, namedtuple, OrderedDict, defaultdict, deque
# To use, you must import as stated at the beginning
# Counters count the element in the data type as dictionaries, uses all dictionary methods
a = 'aaaaaabbbbbbsssss'
print(Counter(a))
# to get most common element: 1 as argument shows the most common element, 2 displays the most common and next common
b = Counter(a)
print(b.most_common(1))
print(b.most_common(2))
print(b.most_common(3))
# to display which common element
# [x][y] x is the common element key, y is the value..[1][0] shows the key of the 2nd most common element
print(b.most_common()[1][0])
# show all the elements in string 'a' as a list
print(list(b.elements()))

# namedtuple: resemblance to classes and unions in C, can be multi-dimensional
# 2 dimensional namedtuple
point = namedtuple('point', 'x,y')
pt1 = point(4, 10)
print(pt1)
# to print values for x and y on a line
print(pt1.x, pt1.y)
# 3 dimensional namedtuple
ppoint = namedtuple('ppoint', 'x,y,z')
ppt1 = ppoint(2, 25, -1)
print(ppt1.x, ppt1.y, ppt1.z)

# OrderedDict: always follows the order in which it was created
ordered_dict = {'name': 'peulumi', 'age': '30', 'level': 300}
print(ordered_dict)

# defaultdict: returns the argument(int,float,list,set) if the key doesn't exist
d = defaultdict(dict)
d['a'] = 1
d['b'] = 2
print(d['c'])

# deque: double-ended queue, used to add or remove elements
f = deque()
f.append(1)
f.append(2)
# appendleft adds argument to the left
f.appendleft(3)
# pop removes last elements
f.pop()
f.popleft()
f.clear()
f.extend([1, 2, 3])
f.extendleft([7, 8, 9])
print(f)
# rotate index determines the element to be moved counting from the back
f.rotate(1)
# to display it as a list
print(list(f))
