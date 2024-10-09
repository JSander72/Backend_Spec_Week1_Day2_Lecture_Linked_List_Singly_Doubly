class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


head = Node("Monday")
node2 = Node("Tuesday")
node3 = Node("Wednesday")

head.next = node2

head.next.next = node3
print(head.next.next.data)