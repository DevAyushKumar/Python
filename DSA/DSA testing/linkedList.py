class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def count_nodes(head):
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count

node1 = Node(6)
node2 = Node(4)
node3 = Node(3)
node4 = Node(1)
node1.next = node2
node2.next = node3
node3.next = node4