# https://www.careercup.com/question?id=5717797377146880

"""

Given some resources in the form of linked list you have to canceled out all the resources whose sum up to 0(Zero) and return the remaining list.

E.g-->> 6 -6 8 4 -12 9 8 -8

the above example lists which gets canceled :
6 -6
8 4 -12
8 -8
o/p : 9
case 3 : 4 6 -10 8 9 10 -19 10 -18 20 25
O/P : 20 25

"""

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert a node at the beginning of the  LL
    def push(self, newData):
        newNode = Node(newData)
        newNode.next = self.head
        self.head = newNode

    def printList(self):
        node = self.head
        while (node):
            print(str(node.data) + "->", end="")
            node = node.next
        print("END")

    # HINT : use a stack
    def deleteElements(self):
        node = self.head
        while(node and node.data):
            print(node.data)


























