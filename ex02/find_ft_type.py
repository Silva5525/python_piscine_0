
# Define a function that takes any type of object and returns an integer.
# define with Parameter name: "all_thing_is_obj"
# parameter type: "object: any"
# return type: "-> int:"
# without type hints: "def all_thing_is_obj(object):" 
# - would also work but is less clear
def all_thing_is_obj(object: any) -> int:
    # Check if the object is a list
    if type(object) is list:
        print(f"List : {type(object)}")
    
    # Check if the object is a tuple
    # elif stands for "else if"
    elif type(object) is tuple:
        print(f"Tuple : {type(object)}")
    
    # Check if the object is a set
    elif type(object) is set:
        print(f"Set : {type(object)}")
    
    # Check if the object is a dictionary
    elif type(object) is dict:
        print(f"Dict : {type(object)}")
    
    # Check if the object is the string "Brian"
    elif object == "Brian":
        print(f"Brian is in the kitchen : {type(object)}")
    
    # Check if the object is the string "Toto"
    elif object == "Toto":
        print(f"Toto is in the kitchen : {type(object)}")
    
    # If none of the above types match
    else:
        print("Type not found")
    
    # The function always returns 42
    return 42

# This file does not run anything when executed directly.
# It's only meant to be imported and used elsewhere.

# USAGE FOR FAILING TEST:
# python3 find_ft_type.py

# USAGE FOR WORKING TEST:
# python3 tester.py | cat -e
