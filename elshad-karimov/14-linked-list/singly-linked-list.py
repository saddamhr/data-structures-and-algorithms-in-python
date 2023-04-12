'''
Time and space for creating a linkedList
Time & Space = O(1)
'''

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    def interSSL(self, value, location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
    def traverseSLL(self):
        if self.head is None:
            print('The Singly Linked List does not exist')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next
    def searchSSL(self, nodeValue):
        if self.head is Node:
            return "The list does not exist"
        else:
            node = self.head
            while node is not None:
                if node.value == nodeValue:
                    return node.value
                node = node.next
            return "The value does not in the list"
    def deleteNode(self, location):
        if self.head is Node:
            print('The SSL does not exist')
        else:
            if location  == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = None
                    self.tail = node
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next
    def deleteEntireSSL(self):
        if self.head is None:
            print('The SSL does not exist')
        else:
            self.head = None
            self.tail = None






singlyLinkedList = SLinkedList()
singlyLinkedList.interSSL(1, 1)
singlyLinkedList.interSSL(2, 1)
singlyLinkedList.interSSL(3, 1)
singlyLinkedList.interSSL(4, 1)
singlyLinkedList.interSSL(0, 0)
singlyLinkedList.interSSL(0, 4)

print([node.value for node in singlyLinkedList])
# singlyLinkedList.deleteNode(3)
singlyLinkedList.deleteEntireSSL()
print([node.value for node in singlyLinkedList])
# node2 = Node(2)

# singlyLinkedList.head = node1
# singlyLinkedList.head.next = node2
# singlyLinkedList.tail = node2