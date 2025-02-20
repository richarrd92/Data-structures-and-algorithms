# stack implementation with linked list
 
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
        print("Stack contents:")
        while current:
            print(current.data, end=" -> " if current.next else "")  # Only print "->" if there's a next node
        current = current.next
        print("")  # End of stack
    

if __name__ == '__main__':
    # menu driven program
    stack = Stack()
    stack.print_stack()
    stack.push(23)
    stack.print_stack()
    stack.push(23)
    stack.push(23)
    stack.push(23)
    stack.push(23)
    stack.print_stack()
