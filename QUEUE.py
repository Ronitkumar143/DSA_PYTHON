# implementation of queue using linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.front=self.rear=None

    def isEMpty(self):
        return self.front==None

    # functiom=n to add element in queue
    def EnQueue(self,item):
        temp=Node(item)
        if self.rear==None:
            self.front=self.rear=temp
            return
        self.rear.next=temp
        self.rear=temp

    # Method to remove an item from queue
    def DeQueue(self):
        if self.isEmpty():
            return
        temp = self.front
        self.front = temp.next

        if (self.front == None):
            self.rear = None

if __name__=='__main__':
    q=Queue()
    q.EnQueue(10)
    q.EnQueue(25)
    q.EnQueue(89)
    q.EnQueue(15)
    print(Queue)
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))