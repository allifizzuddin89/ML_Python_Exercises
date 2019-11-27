#try : block of code to be attempted, may lead an error
#except : block of code if ther is error in try block
#finally : final block, regarless of error
#why exception handling?
#ans : we may proceed code even if there is error occured

def add(n1, n2):
    print(n1+n2)

add(10, 33)
number1 = 11
#number2 = input("please provide a number: ") #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#add(number1, number2)

try:
    #may have an error
    result = 10 + 8
except:
    print("hey it looks you are not adding correctly")
else:
    print("Excellente!")

print(result)

try:
    f = open('testfile','r') #try to change r to w or w to r, there is error
    f.write("write a test line")
except TypeError: #refer official doc for type of error
    print("There was a type error")
except OSError:
    print("Hey you have an OS error")
except:
    print("All other exception")
finally:
    print("I'm always run")

def ask_for_int():
    try:
        result = int(input("Please provide a number: "))
    except:
        print("Alamak machaaa! That's not a number laaa")
    finally:
        print("End of try/except finally")

ask_for_int()

def ask_for_it():
    while True:
        try:
            result = int(input("Please provide a number: "))
        except:
            print("Almak machaa! Nombor la please...")
            continue
        else:
            print("Yes! Arigato gozaimasu")
            break
        finally:
            print("End of except/try/finally")
            print("I'll always run till the end!!!")

ask_for_it()
