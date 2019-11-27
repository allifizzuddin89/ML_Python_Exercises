# import first_module
# print("second module's name is : {}".format(__name__))

# print('-'*90)

###########################################################################

#this method of importing will not 
import first_module #it does not print main() in the first module due to __name__ is not __main__

print("second module's name is {}".format(__name__))
first_module.main() #we have to call specifically the function from first module
