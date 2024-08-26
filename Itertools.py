# itertools are tools used to work on iterables
# operator library is used for easy arithmetic operations
from itertools import product, permutations, combinations, combinations_with_replacement, accumulate, groupby
from itertools import count, cycle, repeat

# Product: used to do cartesian multiplication of iterables
a = [1, 2, 3]
b = [4, 5]
prod = product(a, b)
prod2 = product(b, a)
print(f'a --> [1, 2, 3]')
print(f'b --> [4, 5]')
print(f'this is the product of a and b {list(prod)}')
print(f'this is the product of b and a {list(prod2)}')
# Permutations: does permutation of the data set, the number inside is the number of digits the permutation will show
perm = permutations(a, 2)
print(f'the permutation of a is {list(perm)}')

# Combinations: make all possible combinations with a specified length
# combination with replacement repeats elements
comb = combinations(a, 2)
combr = combinations_with_replacement(a, 2)
print(f'the combination of a is {list(comb)}')
print(f'the combination with replacement of a is {list(combr)}')

# Accumulate
acc = accumulate(a)
print(f'the accumulate of a is {list(acc)}')

# groupby: used to group iterables based off a key(can be a function)
def lessthanthree(x):
    return x < 3

grouping = groupby(a, key=lessthanthree)
for key, value in grouping:
    print(f'keys --> {key}, values ---> {list(value)}')

# count, cycle, repeat
# count: counts from the argument infinitely until a stop condition
# count: second argument is the step for the counting
for i in count(10, 2):
    print(i)
    if i == 22:
        break
# cycle: goes through the iterable infinitely until a stop condition
for i in cycle(a):
    print(i)
    if i == 2:
        break
# repeat: repeat(1,4): repeats 1, 4 times
for i in repeat(a, 4):
    print(i)
