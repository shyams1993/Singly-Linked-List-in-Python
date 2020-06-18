class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist():
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        return str(self.__dict__)

    def append(self,data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else:
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        return self

    def printer(self):
        currentNode = self.head
        lis = []
        while currentNode != None:
            lis.append(currentNode.data)
            currentNode = currentNode.next
        return lis
    
    def prepend(self,data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

    def insert(self,index,data):
        newNode = Node(data)
        currentNode = self.head
        i = 0
        if index == 0:
            self.prepend(newNode.data)
        elif index == self.length:
            self.append(newNode.data)
        else:
            while i < self.length:
                if i == index-1:
                    newNode.next = currentNode.next
                    currentNode.next = newNode
                    self.length += 1
                    break
                currentNode = currentNode.next
                i+=1
    
    def remove(self,index):
        currentNode = self.head
        i = 0
        while i < self.length:
            if index == 0:
                self.head = currentNode.next
                self.length-=1
                break
            if i == index - 1:
                if currentNode.next == self.tail:
                    currentNode.next = None
                    self.tail = currentNode
                    self.length-=1
                    break
                currentNode.next = currentNode.next.next
                self.length-=1
                break
            i+=1
            currentNode = currentNode.next

    def reverse(self):
        first = self.head
        self.tail = self.head
        second = first.next
        while second != None:
            third = second.next
            second.next = first
            first = second
            second = third
        self.head.next = None
        self.head = first


m = Linkedlist()
m.append(100)
m.append(101)
m.append(102)
m.prepend(99)
m.insert(0,97)
m.insert(5,104)
# m.reverse()
m.remove(5)
m.remove(4)
m.remove(3)
print(m.printer())
print(m.tail.data)
print(m)
