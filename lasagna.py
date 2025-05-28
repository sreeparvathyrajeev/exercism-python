"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


"""define the constants"""
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2



#TODO: Remove 'pass' and complete the 'bake_time_remaining()' function below.

def bake_time_remaining(elapsed_bake_time):
    """Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`."""
    
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    


#TODO: Define the 'preparation_time_in_minutes()' function below.
# You might also consider defining a 'PREPARATION_TIME' constant.
# You can do that on the line below the 'EXPECTED_BAKE_TIME' constant.
# This will make it easier to do calculations.

def preparation_time_in_minutes(no_of_layers):   
    """calculates the preparation time using no of layers"""
    return PREPARATION_TIME * no_of_layers


#TODO: define the 'elapsed_time_in_minutes()' function below.

def elapsed_time_in_minutes(no_of_layers,elapsed_bake_time):  
    """calculates the total elapsed time"""      
    return (PREPARATION_TIME * no_of_layers)+elapsed_bake_time


# TODO: Remember to go back and add docstrings to all your functions
#  (you can copy and then alter the one from bake_time_remaining.)
