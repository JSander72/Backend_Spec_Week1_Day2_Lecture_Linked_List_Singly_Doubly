
class Node:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    # alist.append("Monday") => adds monday node to the list
    def append(self, data):
        new_node = Node(data) #creating an node with the data passed in

        if self.head == None: #The list is empty
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    
    def traverse(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

    # alist.pop() => removes and returns the last node in the list
    def pop(self):
        if self.tail == None:
            return "Cant pop from empty list"
        else:
            popped = self.tail
            self.tail = popped.prev
            self.tail.next = None
            return popped.data
        
    def insert(self, idx, data):

        new_node = Node(data)
        current = self.head
        count = 1
        while count < idx:
            current = current.next
            count += 1

        new_node.next = current.next
        new_node.prev = current
        current.next = new_node
        new_node.next.prev = new_node
alist = LinkedList()

alist.append("plain pancake")
alist.append("blueberry pancake")
alist.append("chocolate chip pancake")

alist.traverse()

print('~'*50)

alist.pop()
alist.traverse()