class Stack:
    def __init__(self):
        self.stack=[]

    def isEmpty(self):
        return self.stack == []

    def push(self,data):
        self.stack.append(data)
    
    def sizeStack(self):
        return len(self.stack)
    
    def pop(self):
        top_of_stack=self.stack[-1]
        del self.stack[-1]
        return top_of_stack
    
    def peek(self):
        return self.stack[-1]

if __name__ == '__main__':
    stack_obj= Stack()
    stack_obj.push(10)
    stack_obj.push(20)
    stack_obj.push(30)
    stack_obj.push(70)
    stack_obj.push(60)
    stack_obj.push(50)
    
    stack_obj.pop()
    print(stack_obj.sizeStack())

    print(stack_obj.peek())

    stack_obj.pop()
    print(stack_obj.sizeStack())
    print(stack_obj.peek())
