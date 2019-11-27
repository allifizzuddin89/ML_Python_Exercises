def lis_brg(x,y=[]):
    y.append(x)
    return y

z=lis_brg(134)
print(z)
print(lis_brg(3))
print(lis_brg(90))

#defined function also can be called using keywords arguement

def kakaktua(volt, state = "stiff", action = "lari", type = "malaysian green"):
    print("-- Kakak tua ni takkan ", action, end = '')
    print(" kalau bagi ", volt, "voltan akan merenjatkan. ")
    print("--Lovely plumage, the", type)
    print("-- It's ", state, "!")

kakaktua(1000)
kakaktua(volt = 2000)
kakaktua(volt = 3400, action = "terbangggg")
kakaktua(action = "merangkak", volt = 4520)
kakaktua('iye ke', 'hidup lagi ke', 'lompat katak')
#kakaktua(volt = 5, 'test1') #error sebab positional arguments follow keywords arguement, patut terbalik

#now we test using container, dict, in class
print('\n')
def cheesecake(kekape, *apaje, **kamus ): #*args vs **kargs, non-keywords vs keywords
    print("-- Wanna some ", kekape, "?" )
    print("-- Sorry dah habis semua ", kekape )
    for arg in apaje:
        print(arg)
    print("-" * 40) #separator
    for perkataan in kamus:
        print(perkataan, ":", kamus[perkataan]) #supposedly any arguements after *apaje will be stored in **kamus

#try call

cheesecake("kek keju", "Gila cepat habis ", "Biar betul ko ni ", 
            penjagakedai = "allif izzudin",
            pelanggan = "maryam azzahra",
            namakedai = "kedai cheesecake allif dan keluarga")

#lets test if dict is not used

print('\n')
def cheesecake1(kekape, *apaje, kamus ):
    print("-- Wanna some ", kekape, "?" )
    print("-- Sorry dah habis semua ", kekape )
    for arg in apaje:
        print(arg)
    print("-" * 40)
    for perkataan in kamus:
        print(perkataan, ":", kamus[perkataan]) #supposedly any arguements after *apaje will be stored in **kamus

#try call

#cheesecake1("kek keju", "Gila cepat habis ", "Biar betul ko ni ", 
#            penjagakedai = "allif izzudin",
#            pelanggan = "maryam azzahra",
#            namakedai = "kedai cheesecake allif dan keluarga")
#got error unexpected arguement for penjaga kedai and so on, so if want to use list, better declare it as dict as container

################################################################
#arbitrary arguement list
#arguements are wrapped in tuples


#def test_arg(file, separator, args*):
#    file.write(separator.join(args))


#################################################################
#unpacking arguement lis, reverse engineer
#have to do this due to the arguements had been in the list or tuples, need to be unpacked for a function call require separate positional arguements

print(list(range(3,6))) #normal call with separate arguements
args= [3,6]
print(list(range(*args))) #call with arguements unpacked from a list
#print(list(range(args))) #without *, it gives error

#try use dict
def kakaktua3(volt, state = "stiff", action = "lari", type = "malaysian green"):
    print("-- Kakak tua ni takkan ", action, end = '')
    print(" kalau bagi ", volt, "voltan akan merenjatkan. ")
    print("--Lovely plumage, the", type)
    print("-- It's ", state, "!")

d = {"volt": "ampat juta", "state": "berdarah mencurah", "action": "phewww "}
kakaktua3(**d) #replace the existing arg in kakaktua3(), reverse engineer

###################################################################################
#lambda expression, lambda a, b: a+b
#small anon functions can be created with lambda keywords

def make_incrementor(n):
    return lambda x: x + n

f= make_incrementor(49)
#print(make_incrementor(44))
print(f(0))
print(f(3))

#need more studies in lambda!!!
#ref stackoverflow, lambda is a anon ftn, simplified, lambda par1,par2 : par2+par1
#equivalent to def lambda(par1,par2): return par1+par2

mylist = [3,6,3,2,4,8,23]
mylist2=sorted(mylist, key=lambda x: x%2==0) #  lambda function told sorted to check if this was even or odd before sorting
print(mylist)
print(mylist2)

test_tuples= [('abang', 30),('sayang', 28), ('maryam', 2)]
umur=sorted(test_tuples, key= lambda test2: test2[1]) #sort umur
print(umur)