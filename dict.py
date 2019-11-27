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

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab':8637678}
print(table)
print('Jack:{[Jack]:d}'.format(table))