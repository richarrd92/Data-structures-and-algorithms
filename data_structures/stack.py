# stack implementation with Stack
 
class Node:
    # initialize node 
    def __init__(self, data=None, next=None):
        self.data = data 
        self.next = next # pointer to next node

class Stack:
    # initialize stack
    def __init__(self):
        self.top = None # top of stack

    # stack is empty
    def empty(self) -> bool:
        return self.top is None
    
    def push(self, data):
        node = Node(data, self.top)
        self.top = node 

    def print_stack(self):
        if self.empty():
            print("Stack is Empty")
            return

        current = self.top
        print("Stack contents:\n")
        print("---")
        while current:
            print(current.data)
            current = current.next
        print("---")  # End of stack
    
    # Implement other methods and simple algorithms

if __name__ == '__main__':
    # Menu driven program 
    stack = Stack()

    while True:
        print("\n----- Stack Menu -----")
        print("1. Push item")
        print("2. Print Stack")
        print("3. Exit")
        
        choice = input("\nEnter your choice: ")

        if choice == '1':
            data = int(input("Push data on stack: "))
            stack.push(data)
        elif choice == '2':
            stack.print_stack()
        elif choice == '3':
            print("\nExiting program...")
            break
        else:
            print("Invalid choice! Please try again.")

