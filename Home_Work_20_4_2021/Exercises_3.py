#Write a program to delete the first item from a singly linked list


class Node(object):
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

class LinkedList(object):
    # Defining the head of the linked list
    def __init__(self):
        self.head = None

    # printing the data in the linked list
    def printLinkedList(self):
        temp = self.head
        while(temp):
            print(temp.data, end=' ')
            temp = temp.next

    # deleting an item based on data(or key)
    def delete(self, data):
        temp = self.head
        # if data/key is found in head node itself
        if (temp.next is not None):
            if(temp.data == data):
                self.head = temp.next
                temp = None
                return ""
            else:
                #  else search all the nodes
                while(temp.next != None):
                    if(temp.data == data):
                        break
                    prev = temp          #save current node as previous so that we can go on to next node
                    temp = temp.next

                # node not found
                if temp == None:
                    return ""

                prev.next = temp.next
                return ""


list = LinkedList()
list.head = Node(1) 
node2 = Node(2)
list.head.setNext(node2)
node3 = Node(3)
node2.setNext(node3)

list.printLinkedList()
print("\n--------------------------------------------------------")
list.delete(1)
list.printLinkedList()
print("\n--------------------------------------------------------")