# data used for sorting algorithms

import random  # Import random module to generate random numbers

# Function to generate an array of random integers
def generate_array(size=15, max_value=10):
    """
    Generates an array of random integers.

    :param size: The size of the array (default is 15).
    :param max_value: The maximum value for the random numbers (default is 10).
    :return: A list of random integers.
    """
    return [int(random.random() * max_value) for _ in range(size)]