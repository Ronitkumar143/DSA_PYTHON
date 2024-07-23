# create a node class
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

# Create class of link list
class Linklist:
    def __init__(self):
        self.head=None

# Method to add element
    def insertBegin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            return
        else:
            new_node.next=self.head
            self.head=new_node

# Method to add element at any index
    def insertIndex(self,data,index):
        new_node=Node(data)
        current_node=self.head
        postion=0
        if postion==index:
            self.insertBegin(data)
        else:
            while(current_node!=None and postion+1!=index):
                postion=postion+1
                current_node=current_node.next

            if current_node!=None:
                new_node.next=current_node.next
                current_node.next=new_node
            else:
                print("index not present")

# method to remove node at any index
    def remove_at_any_index(self,index):
        if self.head==None:
            return
        current_node=self.head
        postion=0
        if postion==index:
            self.remove_first_node()
        else:
            while(current_node!=None and postion+1!=index):
                postion = postion+1
                current_node=current_node.next
            if current_node!=None:
                current_node.next=current_node.next.next
            else:
                print("index not present")

# print the size of linked list
    def size(self):
        size=0
        if(self.head):
            current_node=self.head
            while(current_node):
                size=size+1
                current_node=current_node.next
            return size
        else:
            return 0

# print method for linked list
    def printll(self):
        current_node=self.head
        while(current_node):
            print(current_node.data)
            current_node=current_node.next

# ADD NODES TO LINK LIST
list=Linklist()
list.insertBegin('R')
list.insertBegin('O')
list.insertBegin('N')
list.insertBegin('I')
list.insertBegin('T')
list.insertIndex("Tan",1)
list.insertIndex("ing",2)
list.remove_at_any_index(2)

print("Node data: ",list.printll())
print("Size of linked list: ",list.size())