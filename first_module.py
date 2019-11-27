# print('first module name is : {}'.format(__name__))
# print('-'*90)

################################################################

print("this always be run")

def main():
    print("the first module's name is {}".format(__name__))
    print("first module main method")

if __name__ == '__main__':
    main()