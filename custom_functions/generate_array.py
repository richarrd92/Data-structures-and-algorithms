import random # generate random numbers

# Generate array of random integers
def generate_array(size=15, max_value=10):
    return [int(random.random() * max_value) for _ in range(size)]
