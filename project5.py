"""
Author: Mekkhi Adkins
Course: CSC 212 - Data Structures
Assignment: Project 5 - Stack and Qeues
Description: Implement a Stack game using stacks and a queue.
"""
#                    !! SAME STACK CLASS FROM PROJECT4 (with new methods added) !!
# Creating the blueprint for the stack objects
class Stack:
    """Represent a stack using a Python list."""

    # constructor that runs when a stack object is created
    def __init__(self):
        """Create an empty stack."""
        # the double underscore discourages accidental access from outisde the class
        self.__items = []

    # creating a method that accepts an item to add to the stack
    # modified for this project:
    # true means the number was added, false means the stack was full so nothing was added
    def push(self, item):
        """Add an item if the stack is not full."""
        if self.is_full():
            return False
        self.__items.append(item)
        return True

    def pop(self):
        """ Removes and return the top of the stack, which represents the last value added. """
        return self.__items.pop()

    # method to check whether stack is empty
    def is_empty(self):
        """Return True if the stack is empty."""
        # counts how many items inside the list, checks if that count is 0
        return len(self.__items) == 0

    # method to count the items in our stack and returns that number 
    def size(self):
        """Reutrn the number of items in the stack. """
        return len(self.__items)
    
    # method for checking the top of the stack
    # it is similar to pop(), but unlike that method it does not change the stack afterward
    def peek(self):
        """Return the top item without removing it."""
        # checking if the stack has any items
        if self.is_empty():
            return None
        # accesses the last item in the list, sends that item back without removing it 
        return self.__items[-1]
    
    # method that checks whether the stack is full
    def is_full(self):
        """Return True when the stack contains three items."""
        # counts numbers currently stored
        # checks whether there are 3 or more numbers and returns true of false
        return len(self.__items) >= 3




stack1 = Stack()

print(stack1.push(1))
print(stack1.push(2))
print(stack1.push(3))
print(stack1.push(4))

print(stack1.size())
print(stack1.peek())
