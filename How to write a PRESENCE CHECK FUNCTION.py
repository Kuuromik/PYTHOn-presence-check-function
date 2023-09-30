#Creating the presenecheck function which compares the length of the "name" variable to 0
def presencecheck(a):
    while len(a)==0:
        a = input("Please enter your name: ")
    return a

name =  input("What is your name: ")
#name is now being checked to see if the user has input text
name = presencecheck(name)
print(name)
