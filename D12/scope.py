# scope is a boundary to access a variable or function
# it is a way to control the visibility of variables and functions
# it is a mechanism to prevent name conflicts
# it is a mechanism how to defined variable for accessibility
# # scope can be global or local
# global scope is the outermost scope
# global scope is defined by the module or the script
# local scope is the innermost scope
# local scope is defined by a function or a block of code
# local scope is accessible only within the function or block of code
# global scope is accessible from anywhere in the module or script
z= "global variable value"
def outer_function():
    x="outre function value"
    print("Outer function:", x)
    # print("Inner function:", y) // can not access y here, it is not defined in this scope
    def inner_function():
        y = "inner function value"
        print("global :", z)
        # print("Inner function:", y) # can access y here, it is defined in this scope
        print("Outer function:", x)
    
    inner_function()
outer_function()
print("global :", z)
# print("outex :", x)// can not access x here, it is not defined in this scope
# print("outex :", y)// can not access y here, it is not defined in this scope

# modifying global variable
global_var = 1
def modify_global():
    global global_var
    global_var+= 2
    print("Modified global variable:", global_var)
modify_global()
# to modify a global variable inside a function, we need to use the global keyword


# the difference between constant and global scope is that
# constant is a value that does not change, while global scope is a boundary to access a variable or function
# constant is a value that is defined at the module level and can be accessed from anywhere in the module
# global scope is a boundary to access a variable or function that is defined at the module level
#  and constant is declared by capitalizing the variable name as a convention
PI = 3.14  # constant
