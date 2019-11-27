#Attributes VS Method

class Dog():
    #Class Object atrributes, will be used globally in particular class
    #same for every instance
    species = 'mammal' #everyone knows dog is a mammal

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name
        

    #Method, more like action
    def bark(self, age):
        print("Phewwit...My name is {}".format(self.name))
        print("I'm a {} and {} yrs old  ".format(Dog.species, age)) #or self.species vs age

my_dog = Dog('Lab', 'Sampu')
my_dog.name
my_dog.breed
my_dog.species
my_dog.bark(3) # Method)

class Circle:
    pi = 3.142

    def __init__(self, radius=1):
        self.radius = radius
    
    def get_circumference(self):
        return self.radius * Circle.pi * 2

my_circle = Circle(22)
my_circle.pi
my_circle.radius
my_circle.get_circumference()

print('-'*100)

##################################################################################################################

#INHERITANCE
#inheritance is a class using a class that already been defined

#INHERITANCE
print("INHERITANCE")
class Animal:
    def __init__(self):
        print("Animal is created")
    
    def who_am_i(self):
        print("I'm a kambing")
    
    def makan(self):
        return print("I'm eating leaf and vegies")

binatang = Animal()
#print(Animal())
binatang.makan()
binatang.who_am_i()

print('#'*10)
class Cat(Animal): #Cat inherit Animal

    def __init_(self):
        Animal.__init__(self) #Animal instance in Cat class, also can try use super()
        print("Cat is created")
    
    # def who_am_i(self):
    #     print("I'm now a cat")

    def meow(self):
        print("Meowwwwww...")
    
    def makan(self):
        print("I'm eating tuna") 

mycat = Cat()
mycat.who_am_i()
mycat.makan() #we can see makan result is from Cat() class, not from base class Animal
mycat.meow()

print('-'*100)

############################################################################################################
#POLYMORPHISM
#multiple class object shares the same method name

print("POLYMORPHISM")
class kambing():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says mbekkkk"

class ayam():
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return self.name + " says cuckooo..cuckooo"

serama = ayam('serama')
john_goat = kambing('john_goat')
print(serama.speak())
print(john_goat.speak())

for pet in [serama, john_goat]:
    print(type(pet))
    print(type(pet.speak))
    print(pet.speak())

def pet_speak(pet1):
    print('in pet_speak function is {}'.format(pet1.speak()))

pet_speak(serama)
pet_speak(john_goat)
pet_speak(ayam('coolie'))
pet_speak(kambing('hooolaa'))

print('-'*100)

###############################################################################################
#abstract classes
#a dummy base class, not to be instantiated

print('abstract class')
class Animal1():

    def __init__(self, name):
        self.name = name
    
    def speak(self):
        raise NotImplementedError("Subclass must implement this abstract method")

# myanimal = Animal('budu')
# myanimal.speak()

class Dog1(Animal1):

    def speak(self):
        return self.name + " says mooooo!!"

fido = Dog1("Fido")

print(fido.speak())

##################################################################################
print('-'*100)
print('magic / dunder')

mylist = [1,2,3]
print(len(mylist))

class Sample():
    pass

mysample = Sample()
# len(mysample)
# print(mysample) #print out object memory location, compare to mysample()

class Book:
    def __init__(self, title, author, pages):
        self.author = author
        self.title = title
        self.pages = pages
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return self.pages

    def __del__(self):
        print(" A book object has beend deleted")


a = Book('Price Volume', 'Anna Couling', 21)
print(a)
print(str(a)) #transform a into string, so have to put __str__ method in class Book
#if there is no __str__ in class Book, it will return memory location of the object

print(len(a))
del a #del a from memory, btw why not del(a)?
b #b is not defined, means it has been deleted
