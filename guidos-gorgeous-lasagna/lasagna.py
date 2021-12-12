
EXPECTED_BAKE_TIME = 40

PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int baking time already elapsed.
    :return: int remaining bake time derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """
    return EXPECTED_BAKE_TIME - elapsed_bake_time
    

def preparation_time_in_minutes(number_of_layers):
    """
    param: number_of_layers
    return: int 
    
    description: takes in number of layers of lasagna and 
    returns the number of minutes of preparation time
    """
    return PREPARATION_TIME * number_of_layers

def elapsed_time_in_minutes(number_of_layers , elapsed_bake_time):
    """
    param: number_of_layers and elapsed_bake_time
    return: int
    
    description: returns the elapsed time in minutes
    """
    return (number_of_layers * PREPARATION_TIME) + elapsed_bake_time
