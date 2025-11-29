class Node:
    def __init__(self,newData):
        self.data = newData
        self.next = None

def createList(s):
    if not s:
        return None
    
    head = Node(s[0])
    tail = head

    for i in range(1,len(s)):
        newNode = Node(s[i])
        tail.next = newNode
        tail = newNode

    return head

def reverseList(head):
    curr = head
    prev = None

    while curr is not None:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

def printList(node):
    while node is not None:
        print(node.data, end = "")
        print("--", end = "")
        node = node.next
    print()

def main():
    String = input("Enter the Elements of the List:\n")
    string = String.split()
    head = createList(string)

    print("The old list: \n")
    printList(head)

    r_head = reverseList(head)
    print("The reversed list:\n")
    printList(r_head)

main()