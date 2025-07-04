# function with parameter and argument
# parameter is a variable that pass to funtion definition from functiom call
# arguments is the actual value pass to taht parameter
def greet(name1,name2,name3):
    print(f"Hello {name1} from {name2}")
    print(f"Hello {name3} from {name2}  ")
    print(f"So, Hello {name1} From {name2}")
    print("...............................")


greet("alamir","python","angela") #this is position argument because the argument pass is match exactly with the position of parameter in function def inition
greet("python","angela","alamir")# has different output from above
#    but there is also a keyword argument that the argument is pass based on key ="value format and the position is does not matter"
print("#################################")
def greet(name,location):
    print(f"hello {name}")
    print(f"what is the weather at {location}")

greet(name="alamirew",location="Addis")#same with below code 
greet(location="Addis",name="alamirew")# same with above code