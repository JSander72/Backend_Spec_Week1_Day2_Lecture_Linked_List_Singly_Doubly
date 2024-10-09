line = "~" *50


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None

    # alist.enqueue("Monday") => a Monday node to the list
    def enqueue(self, data):
        new_node = Node(data)
        if self.head == None: #My list is empty if head is None
            self.head = new_node #New node becomes the head
            self.tail = new_node #and also the tail
        else:
            self.tail.next = new_node #Finds the end of the list (Tail), and adds the new node after
            self.tail = new_node #Assigns the Tail responsibility to the new_node

    # alist.traverse() => prints all the data stored in the linked list
    def traverse(self):
        current = self.head
        while current:
            print(current.data) #print data for the current node
            current = current.next #current node becomes the next node in the chain

    # alist.dequeue => remove and return the node at the front of the list
    def dequeue(self):
        if self.head == None:
            return "cant dequeue from an empty list"
        else:
            removed = self.head
            self.head = removed.next
            return removed.data




songs = Queue()

songs.enqueue("Vanilla and Light - Tommy Newport")
songs.enqueue("Free Bird")
songs.enqueue("Must be Me")
songs.enqueue("Sandman")
songs.enqueue("Sip(alcohol)")
songs.enqueue("Under the Bridge")

songs.traverse()

print(line)

songs.dequeue()

songs.traverse()
 