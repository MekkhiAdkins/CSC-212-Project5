"""
Author: Mekkhi Adkins
Course: CSC 212 - Data Structures
Assignment: Project 5 - Stack and Qeues
Description: Implement a Stack game using stacks and a queue.
"""

import random

#                    !! SAME STACK CLASS FROM PROJECT4 (with new methods added) !!
# Creating the blueprint for the stack objects
#LIFO
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
    
    # method for making things printable
    def __str__(self):
        """Return the stack contents from bottom to top."""
        return str(self.__items)   

# *********************************************************************************************

#FIFO
# creating blueprint for queue objects
class Queue:
    """Represent a queue using a Python list."""

    # inistalizes the empty lsit
    def __init__(self):
        """Create an empty queue."""
        self.__items = []
    
    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.__items.append(item)

    def dequeue(self):
        """Remove and return the front item of the queue."""
        # removes and returns item at index 0 (FIFO)
        return self.__items.pop(0)

    # checks whether thr queue contains any numbers
    def is_empty(self):
        """Return True if the queue is empty."""
        return len(self.__items) == 0

    def size(self):
        """Return the number of items in the queue."""
        return len(self.__items)

    # this allows us to write printable statements
    def __str__(self):
        """Return the queue contents as a string."""
        return str(self.__items)
    
# *********************************************************************************************

# defining a function to create the starting queue
def create_queue():
    """Create a queue of 15 random numbers between 1 and 5."""
    # creating empty queue object
    numbers_queue = Queue()

    # repeats the following code 15 times
    for count in range(15):
        # random integer between 1-5 inclusively
        number = random.randint(1, 5)
        # adding the generated number to the back of the queue, using the enqueue method we created
        numbers_queue.enqueue(number)
    # returning the completed queue object
    return numbers_queue

# *********************************************************************************************

# defining a fuction that creates the game stacks
def create_stacks():
    """Create three empty stacks for the Stackr game."""
    # creating a dictionary
    # a,b and c are the keys followed by the stacks which are the values 
    stacks = {
        "a": Stack(),
        "b": Stack(),
        "c": Stack()
    }
    # retunrs the dictionary containing all 3 stacks 
    return stacks

# creating a function that recieves our queue and dictionary of stacks
# this fuction will be called after every move during gameplay 
def display_status(numbers_queue, stacks):
    """Display the current queue and three stacks."""
    # displays the current queue
    print("Queue:", numbers_queue)
    # accessing the 3 different stacks from the dictionary
    print("a:", stacks["a"])
    print("b:", stacks["b"])
    print("c:", stacks["c"])
    print() #just making the output easier to read


game_queue = create_queue()
game_stacks = create_stacks()

display_status(game_queue, game_stacks)
game_stacks["a"].push(2)
game_stacks["b"].push(5)
game_stacks["a"].push(3)

display_status(game_queue, game_stacks)
