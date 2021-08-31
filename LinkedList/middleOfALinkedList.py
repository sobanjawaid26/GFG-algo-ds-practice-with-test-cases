# https://www.geeksforgeeks.org/write-a-c-function-to-print-the-middle-of-the-linked-list/

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

    def printMiddle(self):
        slow = self.head
        fast = self.head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        print('The middle element is ', slow.data)


# Code execution starts here
if __name__ == '__main__':

    llist = LinkedList()

    for i in range(5, 0, -1):
        llist.push(i)
        llist.printList()
        llist.printMiddle()

