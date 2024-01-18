# from collections import namedtuple
# mentor=namedtuple("mentor", ["name", "age", "group"])
# new_tuple=mentor("Ilyosbek", "24", "fn7")
# print(getattr(new_tuple, "name"))
# print(new_tuple._replace(age=27))

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        new_data = Node(data)
        current=self.head
        
        while current.next!=None:
            current=current.next
        current.next=new_data
        
    def show(self):
        current=self.head
        

        while current.next!=None:
            current=current.next
            print(current.data)

            
        
data=LinkedList()
data.append(5)
data.append(7)

print(data.show())