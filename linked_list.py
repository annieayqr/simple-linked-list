from node import Node

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Public methods

    def insert(self, value):            # Add value to end of list using recursive
        newNode = Node(value)

        if self.head is None:
            self.head = newNode
        else:
            current = self.head         # C++ style current pointer
            while current.next:         # Traverse to end of the list
                current = current.next  
            current.next = newNode
            newNode.prev = current

    def find(self, value, current = None):  # Find a value
        if current is None:             # First call
            current = self.head         # C++ style current pointer

        if current is None:             # Empty list or end
            return False
        
        if current.value == value:       # Found
            return True

        return self.find(value, current.next)
    
    def delete(self, value):            # Delete a value
        if self.head is None:
            return
        
        current = self.head             # C++ style current pointer

        while current and current.value != value:  
            current = current.next

        if current is None:  # Not found
            return
        
        # Delete the node 
        if current.prev is None and current.next is None:   # Case 1: only node
            self.head = None
        elif current.prev is None:       # Case 2: delete head
            self.head = current.next
            self.head.prev = None
        elif current.next is None:       # Case 3: delete tail
            current.prev.next = None
        else:                            # Case 4: delete middle
            current.prev.next = current.next
            current.next.prev = current.prev
    
    def printList(self):                 # Print all values
        if self.head is None:
            print("List is empty.")
            return
        
        current = self.head              # C++ style current pointer
        print("List: ", end="")
        while current:
            print(current.value, end="")
            current = current.next
        print()