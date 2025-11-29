class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def mergeSortedLists(l1, l2):
    # 1. Create a "Dummy" node to act as the starting point.
    # This saves us from writing complex checks for the Head node.
    dummy = Node(-1) 
    tail = dummy

    # 2. Iterate while BOTH lists have data
    while l1 is not None and l2 is not None:
        
        # 3. Compare the data
        if l1.data <= l2.data:
            tail.next = l1      # Attach l1 node
            l1 = l1.next        # Move l1 pointer
        else:
            tail.next = l2      # Attach l2 node
            l2 = l2.next        # Move l2 pointer
            
        # 4. Advance the tail
        tail = tail.next

    # 5. Attach the remaining part (if any list is not finished)
    if l1 is not None:
        tail.next = l1
    elif l2 is not None:
        tail.next = l2

    # 6. Return dummy.next (The actual head of the merged list)
    return dummy.next

# --- Helper Functions for Input/Output ---
def createList(elements):
    if not elements: return None
    head = Node(elements[0])
    tail = head
    for i in range(1, len(elements)):
        tail.next = Node(elements[i])
        tail = tail.next
    return head

def printList(node):
    while node:
        print(f"{node.data}", end="")
        if node.next: print(" -> ", end="")
        node = node.next
    print()

def main():
    # Input List 1
    in1 = input("Enter sorted elements for List 1 (e.g., 1 3 5): ")
    list1 = createList(list(map(int, in1.split())))

    # Input List 2
    in2 = input("Enter sorted elements for List 2 (e.g., 2 4 6): ")
    list2 = createList(list(map(int, in2.split())))

    print("\nMerging...")
    merged_head = mergeSortedLists(list1, list2)
    
    print("Result: ")
    printList(merged_head)

if __name__ == "__main__":
    main()