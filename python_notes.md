# Python 

### Common Built-In Functions
- **`isdigit()`**: Returns `True` if the character is a digit.
- **`str()`**: Converts to a string.
- **`reversed()`**: Reverses a variable but returns an iterator object.
- **`[::-1]`**: Reverses using slicing.
- **`sys.maxsize`**: smallest possible int. Must import sys

---

### Lists
- **List Initialization**: `x = []` (zero-indexed and mutable).
- **Storing References**: Lists store references, not copies.
- **Copying Lists**: 
  - `y = x[:]` creates a copy of `x`—changes to `x` do not affect `y`.
- **Pop Operations**: 
  - `x.pop()` removes the last item (e.g., `5`) and prints it.
  - `x.pop(index)` removes the value at the given index.
- **Accessing List Elements**: `x[index]` accesses the value at the given index.

---

### Tuples
- **Tuple Initialization**: `x = ()` (uses parentheses).
- **Immutability**: Tuples are immutable—cannot be changed.
- **No Append/Remove**: Cannot append, remove, or change values in a tuple.

---

### For Loop
- **Syntax**: 
  - `for i in range(stop)`
  - `for i in range(start, stop)`
  - `for i in range(start, stop, increment/step)`

---

### While Loop
- **Basic Syntax**: `while (condition)`

---

### Slice Operator
- **Syntax**: `x[start:stop:step]`, `x[start:]`, `x[:stop]`
- **Description**: Picks a section of a data structure (e.g., list). Can also reverse the list with `x[::-1]`.

---

### Set
- **Equivalent**: Like an unordered set in C++.
- **Properties**: Removes duplicates and stores elements unordered.
- **Operations**: Supports union, intersection, and difference.
- **Syntax**: 
  - `print(element in set)`

---

### Dictionary
- **Equivalent**: Like an unordered map in C++.
- **Initialization**: `x = {key: value}`
- **Adding/Accessing Values**: 
  - `x[key] = value`
  - `x.keys()` to print keys.
  - `x.values()` to print values.
- **Removing Values**: 
  - `del x[key]` or `del x[value]`

---

### Comprehensions
- **List Comprehension**: 
  - `x = [i for i in range(5)]`
  - `x = [i for i in range(5) for j in range(5)]`

---

### Functions
- **Define a Function**: 
  - `def func():`
- **Return Values**: Functions can return any value or object.

---

### Additional Functions
- **`dir()`**: Lists all functions of a data type.
  - Example: `print(dir(str))`
- **`help()`**: Provides documentation on functions.
  - Example: `print(help(str.upper))`

---

### String Formatting
- **Old-style Formatting**: 
  - `message = "Hello %s" % user_input`
- **f-Strings**: 
  - `message = f"Hello {user_input}"`

---

### Iterator Concatenation
- **Joining Elements**: Use `"".join(list_or_tuple)` to join the strings in a list or tuple.

---

### Arguments
- **Variadic Arguments**: 
  - `def mean(*args)` returns a tuple.
- **Keyword Arguments**: 
  - `def mean(**kwargs)` returns a dictionary.

---

### Files
- **Reading a File**:
  - `my_file = open("file.txt")` (File must be in the same directory).
  - `print(my_file.read())`
- **Closing a File**: Always close files after use to erase content from RAM.
  - `my_file.close()`
- **With Statement**: Handles opening and closing of files automatically.
  - ```python
    with open("my_file.txt") as my_file:
        content = my_file.read()
        print(content)
    ```
- **Writing to a File**: 
  - ```python
    with open("my_file.txt", "w") as my_file:
        my_file.write("snail")
    ```
- **Append to a File**: 
  - ```python
    with open("file.txt", "a+") as my_file: 
        my_file.write("\nthis text is appended")
        my_file.seek(0)  # returns cursor to 0
        print(my_file.read())
    ```

---
