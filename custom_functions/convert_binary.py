# returns list in reverse
def convert_binary_reverse(n: int) -> list:
    remainder = n%2 # stores the remainder
    binary_arr = [remainder]

    division_result = n // 2 # integer division
    if division_result == 0:
        return [remainder]
    
    return binary_arr + convert_binary_reverse(division_result)


# returns list of binary digits in order
def convert_binary(n: int) -> list:
    if n == 0:
        return [0]
    if n == 1:
        return [1]
    
    return convert_binary(n // 2) + [n % 2] # concatenation of both lists 

x = int(input("Enter integer: "))
print(convert_binary(x))
