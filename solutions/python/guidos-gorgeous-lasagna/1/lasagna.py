"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.


EXPECTED_BAKE_TIME = 40
def bake_time_remaining(act_min):
    """Calculate the elapsed cooking time.
    
    Parameters:
        act_min (int): the actual baking time finished yet
    
    Returns:
        int: The remaining baking time (in minutes).

    This function takes one argument as the actual baking time done yet and to find the remaining baking time the actual baking time is subracted from the expected baking time (constant).
    """
    
    return EXPECTED_BAKE_TIME - act_min
def preparation_time_in_minutes(number_of_layers):
    """Calculation of preparation of the lasanga
    
    Parameters:
        number_of_layers (int) = the total no of layers in the lasanga
    
    Returns:
this function calculates the total minutes to prepare the lasanga based on the no of layers. each layer barely takes 2 minutes to prepare. so that it will return the no of mins for preparatrion by multipling the no of layers with the preparing time for each layer(2 mins)
    """
    TIME_FOR_EACH_LAYER = 2
    return number_of_layers*TIME_FOR_EACH_LAYER
def elapsed_time_in_minutes(number_of_layers,elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time
    
