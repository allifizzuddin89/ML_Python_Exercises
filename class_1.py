mylist = [1,3,5]
print(mylist)
myset = set('aab')
print(myset)
type(mylist)
type(myset)
print('myset is {0} and mylist is {1}'.format(myset,mylist))

#class is user defined object
#we create instance in class
#instance is particular object in class

# class Sample():#in Python use camel casing for class name, snake casing for variable name
#      pass

# my_sample = Sample()
# print(type(my_sample))

class Dog():
    #init will be called everytime instances of the class is written
    def __init__(self, mybreed, name, spots ): #breed is attribute of the object, self is important to connect to instances of the class
        #self.attribute_name
        self.breed = mybreed
        self.name = name
        self.spots = spots

my_dog = Dog(mybreed='huskie', name= 'Sampu', spots=False)
type(my_dog) #if print this, it shows an instance of Dog()
print(type(my_dog))
print(my_dog.breed) #breed instead of mybreed, self.attribute, self=my_dog, attribute=breed, refer class Dog()
print(my_dog.name)
print(my_dog.spots)
