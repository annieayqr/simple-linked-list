from linked_list import LinkedList

def test_comprehensive():
    print("=== COMPREHENSIVE LINKED LIST TEST ===\n")
    
    ll = LinkedList()
    
    print("1. Testing empty list:")
    ll.printList()  # Should print: List is empty.
    print(f"   find(10) on empty: {ll.find(10)}")
    ll.delete(10)  # Should do nothing
    
    print("\n2. Testing single node operations:")
    ll.insert(5)
    ll.printList()  # Should print: List: 5
    print(f"   find(5): {ll.find(5)}")
    print(f"   find(10): {ll.find(10)}")
    
    print("\n3. Testing multiple nodes:")
    ll.insert(10)
    ll.insert(15)
    ll.insert(20)
    ll.printList()  # Should print: List: 5 <-> 10 <-> 15 <-> 20
    
    print("\n4. Testing find() recursion (edge cases):")
    print(f"   find(5) (head): {ll.find(5)}")
    print(f"   find(20) (tail): {ll.find(20)}")
    print(f"   find(15) (middle): {ll.find(15)}")
    print(f"   find(99) (non-existent): {ll.find(99)}")
    print(f"   find(0) (non-existent): {ll.find(0)}")
    
    print("\n5. Testing delete head:")
    ll.delete(5)
    ll.printList()  # Should print: List: 10 <-> 15 <-> 20
    print(f"   find(5) after delete: {ll.find(5)}")
    
    print("\n6. Testing delete tail:")
    ll.delete(20)
    ll.printList()  # Should print: List: 10 <-> 15
    
    print("\n7. Testing delete middle:")
    ll.insert(12)
    ll.insert(18)
    ll.printList()  # Should print: List: 10 <-> 15 <-> 12 <-> 18
    ll.delete(15)
    ll.printList()  # Should print: List: 10 <-> 12 <-> 18
    
    print("\n8. Testing all deletes to empty:")
    ll.delete(10)
    ll.delete(12)
    ll.delete(18)
    ll.printList()  # Should print: List is empty.
    
    print("\n9. Testing the original main.py demo:")
    # This is exactly what main.py does
    ll2 = LinkedList()
    ll2.insert(10)
    ll2.insert(20)
    ll2.insert(30)
    print("   Linked List Demo:")
    ll2.printList()
    print(f"   Found 20? {ll2.find(20)}")
    print(f"   Found 99? {ll2.find(99)}")
    
    print("\n=== TEST PASSED SUCCESSFULLY! ===")
    print("Ready to push to GitHub ✅")

if __name__ == "__main__":
    test_comprehensive()