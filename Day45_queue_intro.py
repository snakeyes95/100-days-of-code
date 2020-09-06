class Queue:
    def __init__(self):
        self.queue=[]
    
    def isEmpty(self):
        return self.queue == []
    
    def sizeQueue(self):
        return len(self.queue)

    def addqueue(self,data):
        self.queue.append(data)
    
    def delqueue(self):
        first_in = self.queue[0]
        del self.queue[0]
        return first_in

    def peek(self):
        return self.queue[0]

if __name__ == '__main__':
    queue=Queue()
    queue.addqueue(3)
    queue.addqueue(4)
    queue.addqueue(5)
    queue.addqueue(6)

    print(queue.peek())

    queue.delqueue()
    queue.delqueue()

    print(queue.peek())

    print(queue.sizeQueue())
