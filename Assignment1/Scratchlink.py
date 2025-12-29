class Node:
    def __init__(ll, data):
        ll.data = data
        ll.next = None  


class LinkedList:
    def __init__(ll):
        ll.head = None  

    
    def append(ll, data):
        new_node = Node(data)
        if not ll.head:
            ll.head = new_node
            return
        last = ll.head
        while last.next:
            last = last.next
        last.next = new_node

    
    def print(ll):
        current = ll.head
        while current:
            print(current.data, end=" - ")
            current = current.next
        print("end")


ll = LinkedList()
ll.append(80)
ll.append(90)
ll.append(100)

ll.print()  