
"""Simulation stasting parameters
The amount of individuals at the any time the simulation"""

def input_positive_integer(ask_for_what):
    """Query the user to input a positive integer.
    
    If the given number was negative, the user is prompted to try again
    
    Arg:
        ask for what:
            A tesxt that will indicate what the user should input the value for.
            It will be used for constructing the prompt the user sees
            when asked for inpur
    Returns:
        A positive integer number as given by user input.
    
    """
    prompt = "please enter the size of the " + ask_for_what + ": "
    input_is_valid = None  # I don't know yet
    while not input_is_valid:
        user_input = input(prompt)
        input_as_int = int(user_input)
        input_is_valid = input_as_int >= 0
        if not input_is_valid:
            print("Please enter a positive number")
    return input_as_int        
    