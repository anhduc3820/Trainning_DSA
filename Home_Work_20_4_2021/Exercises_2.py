#Write a program to search a specific item in a singly linked list and 
# return true if the item is found otherwise return false

class Node:
    # Each node has its data and a pointer that points to next node in the Linked List
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

    # function to set data
    def setData(self, data):
        self.data = data

    # function to get data of a particular node
    def getData(self):
        return self.data

    # function to set next node
    def setNext(self, next):
        self.next = next

    # function to get the next node
    def getNext(self):
        return self.next

class LinkedList:
    # Defining the head of the linked list
    def __init__(self):
        self.head = None

    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next
        
    # iterative search
    def search(self, node, data):
        if node == None:
            return False
        if node.data == data:
            return True
        return self.search(node.getNext(), data)

list = LinkedList()
list.head = Node(1) 
node2 = Node(2)
list.head.setNext(node2)
node3 = Node(3)
node2.setNext(node3)

list.printLinkedList()
print("\n--------------------------------------------------------")
print(list.search(list.head, 2))