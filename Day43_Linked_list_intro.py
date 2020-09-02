class Node():
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class Linked_list():
    def __init__(self):
        self.head=None
        self.size=0

    def insert_Start(self,data):
        self.size=self.size+1
        newNode=Node(data)

        if not self.head:
            self.head=newNode
        else:
            newNode.nextNode=self.head
            self.head=newNode

    def listSize(self):
        return self.size

    def insert_End(self,data):
        self.size=self.size+1
        newNode=Node(data)
        currentHead=self.head
        while currentHead.nextNode is not None:
            currentHead=currentHead.nextNode
        currentHead.nextNode=newNode
    
    def removeNode(self,data):
        if self.head is None:
            return 'sorry'
        self.size=self.size - 1 
        currentHead=self.head
        previousNode = None

        while currentHead.data != data:
            previousNode=currentHead
            currentHead=currentHead.nextNode
        
        if previousNode is None:
            self.head=currentHead.nextNode
        else:
            previousNode.nextNode=currentHead.nextNode


    def list_Traversal(self):
        currentHead=self.head
        print('---------------------------------------------------------------------------------------')
        while currentHead.nextNode is not None:
            print(f'{currentHead.data}')
            currentHead=currentHead.nextNode
        print(currentHead.data)
        print('---------------------------------------------------------------------------------------')


if __name__ == '__main__':
    linkedList=Linked_list()
    linkedList.insert_Start(1)
    linkedList.insert_Start(2)
    linkedList.insert_End(4)
    linkedList.insert_Start(3)
    
    print(linkedList.listSize())

    linkedList.list_Traversal()

    linkedList.removeNode(1)

    linkedList.list_Traversal()
