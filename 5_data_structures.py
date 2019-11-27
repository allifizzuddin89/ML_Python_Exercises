#list.append()
#list.extend(iterable)
#list.insert(i,x)
#list.remove(i,x), use del list[x:y] to delete slices
#list.pop([j]) remove the last item
#list.clear() remove all item equal to del a[:]
#list.index(x[start[,end]]) return zero-based index in the list of the first item whose value equals to x
#list.count(x) return the number of times, x appear in the list
#list.reverse() reverse the element of the list in place
#list.copy() return a shallow copy of the list, equal to a[:]
#list.sort() equal to sorted(list, key=, reverse=)
#EXAMPLES below

fruits = ['durian', 'betik', 'epal', 'betik', 'manggis', 'mangga', 'pelam', 'pisang']
fruits.append('cempedak')
print(fruits)
x = fruits.count('epal')
print(x)
x = fruits.count('banana')
print(x)
y = fruits.index('betik',2) #indexing betik a starting position 2
print(y)
z = fruits.index('betik')
print(z)
a = fruits.extend("nangka")
print(fruits)
fruits.remove('n')
print(fruits)
#fruits.pop(9:13)
#print(fruits)
del fruits[9:14]
print(fruits)
fruits.sort(reverse=True)
print(fruits)

b= sorted(fruits, key=len)
print(b)
c= fruits.count('betik')
print(c)
print(b.pop())
print(b.pop(1))
print('-'*80)
##############################################################################
#using list as stack, last in ; first out

fruits.append('jagung')
print(fruits)
print(fruits.pop())

###############################################################################
#using list as que, first in ; first out

fruits.insert(0, 'keladi')
print(fruits)
del fruits[0]
print(fruits)

#this method is slow, list is not efficient doing this bcoz all other elements have to shift by one
#so we use collections.deque

from collections import deque
baris = deque(fruits) #syntax deque([list])
print(baris.popleft())
print('-'*80)
######################################################################################
#List comprehension creates concise way to create list

squares= []
for d in range(10):
    squares.append(d**2)

print(squares)

#OR simply;
print('-'*80)
#use map if use lambda and list
# r = map(func, seq), example using map, takes 2 arg
square1 = list(map(lambda e: e**2, range(10))) # lambda arguement_list : expression , lambda must be used with map() or filter() or reduce()
print(square1)

#OR simply;
print('-'*80)
square2 = [f**2 for f in range(10)]
print(square2)

#another example of list comprehension
print('-'*80)
g= [(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y]
#print([(x,y) for x in [1,2,3] for y in [3,1,4] if x!= y])
print("g = {}".format(g))

#similar to ;

g = []
for x in [1,2,3]:
    for y in [3,1,4]:
        if x!=y:
            g.append((x,y))

print(g)

#################################################################################

print('\n','-'*80)
#use for, if with tuples

vec = [-4, -2, 0, 2, 4]
vec2 = [x*2 for x in vec] #create a new list with doubled vec
print('vec = ',vec2)
#print('vec = {}'.format(vec))

#filter the list, + only
vec3 = [x for x in vec2 if x>=0]
print(vec3)

#absolute ftn on vec2
vec4 = [abs(x) for x in vec]
print(vec4)

####################################################################################
print('\n','-'*80)

#call a method on each element
buahsegar = ['  pisang', 'durian  ', 'manggis  ']
buahsegar1 = [buah.strip() for buah in buahsegar] #strip spaces end and start
print(buahsegar)
print(buahsegar1)

####################################################################################
print('\n','-'*80)

#create tuples
tupel=[(x, y) for x in range(6) for y in range(3)]
print(tupel)

##################################################################################
print('\n','-'*80)

#nested list comprehension

matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]

#transpose the matrix
matrix_t = [[row[i] for row in matrix] for i in range(4)]
#print(matrix[1])
print('matrix is')
print(matrix)
print('matrix_t is')
print(matrix_t)

#using built-in function zip()

print('\n','using zip()')
print(list(zip(*matrix)))

########################################################################################

print('\n','-'*80)

#revise on tuples.

t = 1234, 5678, 'haiawak'
print(t[0])
print(t)

#nest tuples

u = t, (1,2,3,4,5,6)
print('u = ', u)
print('u[1] = ', u[1])
print('u[0] = ', u[0])

#note :
#tuples are immutable
#list are mutable
# if, 1234, 5678, 'haiawak' = t, is called sequence unpacking
# tuples packing vs sequence unpacking

######################################################################################
print('\n','-'*80)

#Data type SETS
#set()
#set is a unordered collection with no duplicate elements
#set support mathermatical operations like uniion, intersection, symmetric difference
# can use set() or {}

bakul = {'epal', 'oren', 'epal', 'pear', 'epal', 'pisang'}
print(bakul) #duplicates is removed
print('oren' in bakul) #fast membership testing
print('banana' in bakul)

#demonstrate set operation on unique letters from two words


a = set('abracadabra')
b = set('alacazam')
print(a) #unique letters in a
print(b) # unique letters in b
print(a-b) # letters in a but not in b
print(a | b) #Lettes in a or b or both
print(a & b) # Letters in both a and b
print(a ^ b) # Letters in a or b but not both

#set comprehension use {}, list comprehension use[]

a = {x for x in 'abracadabra' if x not in 'abc'} #set comprehension
print(a)

################################################################################################
#5.5 dictionaries
#dictionaries are indexed by keys
#unlike list/sequence, indexed by range of numbers
#dict are a set of key : value pairs
#dict is immutable

print('\n','-'*80)

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127 #add guido
print(tel)

print(tel['jack'])
#print(tel['4139']) cannot call value pair, key error

del(tel['sape']) #del operation
print(tel)

tel['irv'] = 4127
print(list(tel)) #list tel w/o key value

print(sorted(tel)) #sort by alphabetical order

print('guido' in tel) #check using in keyword
print('jack' not in tel)

#dict() constructor builds dictionaries directly from sequence of key-value pairs

print(dict([('sape', 4139),('guido', 4127),('jack', 4098)]))

#dict comprehension, create from arbitrary key and value expression

print({x: x**2 for x in (2, 4, 3)})

#when the key is simple string, easier to specify using keywords arguement

print(dict(sape=4139, guido=4127, jack=4098))


#######################################################################################
#5.6 looping technique

print('\n','-'*80)

#looping through dictionaries
#key and value can be retrieved at the same time using the items() method

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k,v)

#loopimg through sequence
#the position index and value can be retrieved using enumerate()

for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i,v)

#loop one or more sequence at the same time, the entries can be paired with the zip() function

questions = ['name', 'quest', 'favourite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('what is your {}? It is {}'.format(q,a))

#loop a sequence in reverse order, use reversed()

for i in reversed(range(1,10,2)):
    print(i)

#loop a sequence in sorted order, use sorted()

basket = ['epal', 'nangka', 'pisang', 'pear', 'cempedak', 'tembikai']

for p in sorted(set(basket)):
    print(p)

#sometimes it is easier and safer to duplicate the list while looping

import math
raw_data = [56.2, float('Nan'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)

print(filtered_data)

#########################################################################################
print('\n','-'*80)

#More on conditions

#comparison operator if
#while
#not in
#in
#=,<, >, ==, <=, >=, can be chained, e.g. a < b = c, a is less than b and b equals to c
#boolean operator ; and, or, not
#boolean operator is lower priorities compare to comparison operator
#not is the highest among boolean op, or is lowest
#e.g A and not B or C equals to (A and (not B) or C), left to right

##########################################################################################
print('\n','-'*80)

#Comparing sequences
#lexicographical order ; first two until exhausted
#same type
#e.g. ;

(1, 2, 3) < (1, 2, 4)
'ABC'< 'pascal'< 'C'< 'Python'

