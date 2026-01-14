from linked_list import LinkedList

ll = LinkedList()

ll.insert(10)
ll.insert(20)
ll.insert(30)

print("Linked List Demo:")
ll.printList()
print(f"Found 20? {ll.find(20)}")
print(f"Found 99? {ll.find(99)}")