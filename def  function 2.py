# def function inside or outside or global & local

global_var = "This is a Global variable"             # outside the function defined

def life_time():
    """This is a function to find life_time of Global & local variable"""
  
    local_var = "This is a Local Variable"            # inside the function defined
    print(local_var)
    print(global_var)
  
life_time()

Output:
        This is a Local Variable
        This is a Global variable
global_var
        This is a Global Variable
local_var
    Error:- under the function defined                 # do not print outside the function
