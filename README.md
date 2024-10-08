## Learning Objectives

https://realpython.com/linked-lists-python/#:~:text=Linked%20lists%20are%20an%20ordered,part%20of%20their%20own%20elements.

- The students should be able to understand the concept of linked lists and differentiate between singly and doubly linked lists.
- The students should be able to implement basic operations such as insertion, deletion, and traversal on linked lists using Python.
- The students should be able to analyze the time complexity of linked list operations and compare them with other data structures.


### Linked Lists

Linked lists are just that; lists that derive their order from linkages created from object attributes that point to the next object.

These lists are dependant on keeping track of what it considered to be the "head" and "tail".

- **Head**: The head is the starting point of the list, the one that initiates the chain reaction of finding what comes nexts. As long as you know where the head of the list is, you can find every other element.

- **Tail**: Conversely, the tail is the end of the chain, and keeping track of it, can make adding/appending new items to the chain much easier.

#### Singly Linked Lists:
Singly Linked lists are a one way street, and can only travel down the "next" stream with no way of getting back. Singly linked lists realy on tracking the "Head" even more so because of this.

![Linked-list-image](https://media.geeksforgeeks.org/wp-content/uploads/singly-linkedlist.png)

#### Doubly Linked Lists:
Like their name suggests, doubly linked lists have two linkages between nodes, connecting a node to the 'next' node and the 'previous' node. This allows you to travel forwards and backwards at any point in your list.

![Doubly-Linked-list](https://media.geeksforgeeks.org/wp-content/cdn-uploads/gq/2014/03/DLL1.png)

Browsers histories are examples of Doubly Linked list as you can go back to earlier URL's and then forward to more recent ones

### Why?
So why would we ever use linked lists. In other programming languages there is a stark difference between how lists/arrays and linked-lists are stored. Languages such as Java and C++ require the pre-allocation of memory for arrays, making the dynamic length of a linked-list more desireable as it only takes as much space as it needs. 

However, in python lists are a dynamic structure and their memory usage is very similar to that of a linked list.

In python the advantage that linked-lists have over python lists is that they can be congigured to your needs, for example they can act as a queue removing the front most element in constant time, where this would be a linear operation for a python list.

### Stacks and Queues

#### Stacks: 
Stacks follow the Last In First Out approach (LIFO). Think of a stack of pancakes, the last one placed on the stack, is the first one the comes off. Why? Because it is the most efficient pancake to access. Similarly in python when dealing with a stack, grabbing the last element happens in constant time O(1).

In python, lists act as stacks, because of the .pop() method. When can instantaneously remove and return the last element

#### Queues:
Queues follow the First in First Out approach (FIFO). For this think of a line of people, the first person in line, is the first person served. In python when dealing with a queue grabbing the first element is the most efficient, and happens in constant time O(1)

In python, lists can behave similar to a queue, by doing .pop(0) removing the first element, however this process does not happen in constant time since the following elements, must then be shifted over 1-by-1 to fill in the gaps.

So how can we get a True Queue? Linked-Lists.