# Sequences: Strings, List, Tuples, Dict,
# These are built in Data Structures and Examples

# Indexing Exapmles Below

# String
x = 'frog'
print (x[3])

#lists
x = ['pig', 'cow', 'horse']
print (x[1])

# Tuple
x = ('Orion', 'Micah', 'Nyla')
print (x[0])


#Slicing : Slice out substrings, sublists, subtuples using indexes. [start: end+1: step]

x = 'computer'
print(x[1:4])
print(x[1:6:2])
print(x[3:])
print(x[:5]) #skip the start on this example
print(x[-1]) #negative indexing
print(x[-3:])
print(x[:-2])



# adding and concatenating - combine 2 sequences of the same type by using +

# string
x = 'horse' + 'shoe'
print(x)

# list
y = ['pig', 'cow'] + ['horse']
print(y)

# tuple
z = ('Orion', 'Micah', 'Nyla') + ('Ken',) #important to have a , at the end of the last tuple so it can be considered as one or it will be seen as a lists with ()
print(z)

# multiplying


#string
x = 'bug' * 3
print(x)

# list
y = [8, 5] * 3
print(y)

# tuple
z = (2, 4) * 3
print(z)


# checking membership - test wherther an item is or is not in a sequence. They will give boolean results only.

# string
x = 'bug'
print('u' in x)

#list
y = ['pig', 'cow', 'horse']
print('cow' not in y)

#tuple
z = ('Orion', 'Micah', 'Nyla', 'Ken')
print('Orion' in z)


# iterating- iterating through the items in a sequence. The item name can be any variable. Usually "i" is used

#item
x = [7,8,3]
for item in x:
    print(item)

#index and item - enumerate provides index and item.
y = [7,8,3]
for index, item in enumerate(y):
    print(index, item)


# number of items - count the number of items in a sequence

# string 
x = 'bug'
print(len(x))

# list
y = ['pig', 'cow', 'horse']
print(len(y))

# tuple
z = ('Orion', 'Michah', 'Nyla')
print(len(z))


# minimum - find the min item in seq lexicographically. Alpha or numberic types but they cannot be mixed types.

# string
x = 'bug'
print(min(x))

# list
y = ['pig', 'cow', 'horse']
print(min(y))

# Tuple
z = ('Orion', 'Micah', 'Nyla')
print(min(z))



# maximum - find the max

# string
x = 'bug'
print(max(x))

# list
y = ['pig', 'cow', 'horse']
print(max(y))

# Tuple
z = ('Orion', 'Micah', 'Nyla')
print(max(z))


# Sum - find the sum of the items in numeric seq

# list
y = [2, 4, 5, 6]
print(sum(y))
print(sum(y[-2:]))

# Tuple
z = (50, 4, 7, 19)
print(sum(z))


# sorting - returns a new list of items in sorted order. Does not change the original list. Creates a new list with a sort result.

# string
x = 'bug'
print(sorted(x))

# list
y = ['pig', 'cow', 'horse']
print(sorted(y))

#tuple
z = ('Orion', 'Micah', 'Nyla', 'Ken')
print(sorted(z))


# sorting - sort by second letter.
# Any a key parameter and a lambda function to return the second character. (The word key here is a defined parameter name, k is an arbitrary variable name meaning you can change the variable to what you like.)

z = ('Orion', 'Micah', 'Nyla', 'Ken')
print(sorted(z, key=lambda k: k[1]))


# count(item) returns count of an item

# string
x = 'hippo'
print(x.count('p'))

# list
y = ['pig', 'cow', 'horse', 'cow']
print(y.count('cow'))

# tuple
z = ('Orion', 'Nyla', 'Micah')
print(z.count('Orion'))



# index(item) - returns the index of the 1st occurance of an item

# string
x = 'hippo'
print(x.index('p'))

# list
y = ['pig', 'cow', 'horse', 'cow']
print(y.index('cow'))

# tuple
z = ('Orion', 'Micah', 'Nyla')
print(z.index('Orion'))



# unpacking - unpack the n items of a sequesnce into n variables
x = ['pig', 'cow', 'horse', 'cow']
a, b, c, d = x 
print(a, b, c, d)



'''
Lists 
- general purpose, most widley used, grow and shrink in size as needed , sequence type, SORTABLE
constructors 
- creating a new list
'''

x = list()
y = ['a', 25, 'dog', 8.43]
tuple1 = (10, 20)
z = list(tuple1)


# List Comprehension
a = [m for m in range(8)]
print(a)
b = [i**2 for i in range(10) if i> 4]
print(b)


# delete - delete a list or an item in a list
x = [5, 3, 8, 6]
del(x[1])
print(x)
del(x) # delete entire list

# append - append an item to a list
x = [5, 3, 8, 6]
x.append(7)
print(x)

#extend - append a sequence to a list
x = [5, 3, 8, 6]
y = [12, 13]
x.entend(y)
print(x)

#insert - insert an item at a given index
x = [5, 3, 8, 6]
x.insert(1, 7)
print(x)
x.insert(1, ['a', 'm'])
print(x)


#pop - pops last item off the list and return list
x = [5, 3, 8, 6]
x.pop() # pop off the 6
print(x)
print(x.pop())

#remove - remove the first instance of a list
x = [5, 3, 8, 6, 3]
x.remove(3)
print(x)

#reverse - reverse the order of the list. It is an in-place sort, meaning it changes the original list.
x = [5, 3, 8, 6]
x.reverse()
print(x)

# sort - sort the list in place
# Note: sorted(x) retrns a new sorted list without changing the original list x.
#       x.sort() puts the item of x in sorttd order (sorts in place)

x = [5, 3, 8, 6]
x.sort()
print(x)

# reverse-sort: sort items descending.
# use reverse=True parameter to the sort function.
x = [5, 3, 8, 6]
x.sort(reverse=True)
print(x)


'''
Tuples 
- Immutable (can't add/change)
- Useful for fixed data
- Faster than Lists
- Sequence Type

Constructors - creating new tuples.
'''

x = ()
x = (1, 2, 3) #parenthesis is optional
x = 1, 2, 3
x = 2, # the comma tells python it's a tuple
print(x, type(x))

list1 = [2, 4, 6]
x = tuple(list1)
print(x, type(x))

# Tuples are immutable, but member objects are mutable. If you have a list inside the tuple, then you can change the list.
x = (1,2,3)
# del(x[1]) # fails
# x[1] = 8  # fails
print(x)

y = ([1, 2], 3) #a tuple where the first item is a list
del(y[0][1])    #del the 2
print(y)        #the list within the tuple is mutable

y += (4, )      # concatenating two tuples work
print(y)


'''
Sets
- Store non-duplicate items
- Very fast access VS lists
- Math Set operations (Union, Intersect)
- Sets are Unordered meaning you cannot sort a set.

Constructors: creating new sets
'''

x = {3, 5, 3, 5} #filter out the duplcates in sets
print(x)

y = set()
print(y)

list1 = [2, 3, 4]
z = set(list1)


# Set operations
x = {3, 5, 3, 5}
print(x)
x.add(7)
print(x)

x.remove(3)
print(x)

# get length of a set x
print(len(x))

# Check membership in x
print(5 in x)

# pop random item from set x
print(x.pop(), x)

# delete all items from set x
x.clear()
print(x)

'''
Mathematical set operations
- Intersection (AND): set1 & set2
- union (OR): set1 | set2
- symmetric difference (XOR): set1 ^ set2 difference (in set1 but not set2): set` - set2
- subset (Set2 contains set1): set1 <= set2
- superset (set1 contains set2): set1 >= set2 
'''

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 & s2) #intersection
print(s1 | s2) # Union
print(s1 ^ s2) #exclusive OR
print(s1 - s2) #minus
print(s1 <= s2) # not subset
print(s1 >= s2) # not a superset



'''
Dictionaries (dict)
- Key/Value Pairs
- Associative array, like java HashMap
- Dicts are unordered
'''

# Three ways of creating the same dictionary

x = {'pork': 25.3, 'beef': 33.8, 'chicken': 22.7}
print(x)
x = dict([('pork', 25.3), ('beef', 33.8), ('chicken', 22.7)]) # tuples passed into the dictionary constructor.
print(x)
x = dict(pork=25.3, beef=33.8, chicken=22.7)
print(x)


# Dict operations
# Noticedd that 'Shrimp" isn't in the dict

x['shrimp']= 38.2  #add or update
print(x)

# delete an item
del(x['shirimp'])
print(x)

# get length of dict x
print (len(x))

# delete all items from dict x
x.clear()
print(x)

# delete dict x
del(x)

#Accessing keys and values in a dict - not compatible within Python 2
y = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
print(y.keys())
print(y.values())
print(y.items()) # key-value pairs

# check membership in y_keys (ony looks in keys, not values)
print('beef' in y)

# check membership in y_keys (only looks in keys, not values)
print('beef' in y)

# Check membership in y_values
print('clams' in y.values())


#Iterating a dict - note, items are in random order
# k and v are just variables. You can use any variables of your choice.
for key in y:
    print(key, y[key])

for k, v in y.items():
    print(k, v)








