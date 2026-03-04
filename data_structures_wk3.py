my_list = []
my_list  = [1, 2, 3]
my_list  = ['a', 2, []]
# print(my_list)

my_list  = [1, 2, 3, 4, 5]
# print(my_list)

# print(my_list [0])
# print(my_list [4])

# print(my_list [-1])
# print(my_list [-5])

my_list [0] = 10

del my_list [0]

# print(my_list)

my_list[0:2] # gives exclusive elements
my_list[-2:]
my_list [0:] # both print the whole sequence
my_list [:] #implicit start and stop index

# print(my_list [0:5:2])

my_list [2:5] = [30, 40, 50]
# print(my_list [2:5])

# addition does not need to be the same length as the range
my_list [2:5] = [30, 40, 50, 60, 70, 80]
# print(my_list)

my_list [2:5] = []
# print(my_list)

new_list = [1, 2, 3]
# print(new_list)

nested_list = [[1, 2, 3], [1, 2, 3]]
# print(nested_list)

my_list  = [1, 2, 3]
my_list.append(4)

# print(my_list)

my_list.extend([5, 6])
# print(my_list)

my_list.insert(1, 100)
# print(my_list)

my_list.remove(100) # Removes first occurence of a value.
# print(my_list)

my_list.pop(4) # Remove item at index
# print(my_list)
my_list.clear() # Reverts to empty list.
# print(my_list)

my_list.extend([1, 1])
my_list.count(1)
# print(my_list)

my_list.sort()
my_list.reverse()
# print(my_list)

# print(len(my_list))


my_list = [1, 2, 3, 4, 5]

# for n in my_list:
#     print(n)

# if 100 in my_list:
#     print('100 in my_list')
# else:
#     print('100 not in my_list')
#
# if 50 in my_list:
#     print('50 in my_list')
# else:
#     print('50 not my_list')

# my_list  = [1, 2, 3, 4, 5]
# my_list  = [n for n in my_list if n > 3]
# my_list  = [n**2 for n in my_list]
#
# new_list = []
# for n in my_list:
#     if n > 3: new_list.append(n)

# string = 'This is a string!'
#
# string[0]
# string[0:5]
#
# print(string)
#
# string.index('is')
# string.replace('a', 'the')
# string.count('i')

d = {}

d = {'apple': 2, 'pear': 3}

d['apple']

d['blueberry'] = 1

d.keys()
d.values()

# print(d)

d.get('apple', 'default')
d.get('grape', 'default')

d.pop('blueberry')

# for k, v in d.items():
    # print(k, v)

{x: x**3 for x in (1, 2, 3)}

{k.upper(): v*2 for k, v in d.items()}

t = (1, 2, 3)
# print(t)

td = {(1,2): 1, (2,3): 2}
# print(td)

def tuple_example():
    return ('apple', 'fruit', 2.99)

fruit, kind, price = tuple_example()

# print(tuple_example())

t = fruit, kind, price
# print(t)

a = set()
a = {1, 2, 3, 4}
a.add(4)
# print(a)

b = {4, 5, 6, 7}
a | b
a & b

# print(a & b)


def list_count(l):
    output = []
    seen = set()

    for n in l:
        if n not in seen:
            seen.add(n)
            n_count = l.count(n)
            output.append((n, n_count))

    return output

l = [1, 2, 2, 3, 4, 4, 5, 1]

print(list_count(l))