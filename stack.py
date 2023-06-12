class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedListStack():
    def __init__(self):   #초기화
        self.head = None
        
    def push(self, data): #data push
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def pop(self):        #data pop
        pop_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            pop_object = self.head.data
            self.head = self.head.next
        return pop_object
    
    def top(self):    #stack's top
        top_object = None
        if self.isEmpty():
            print("Stack is Empty")
        else:
            top_object = self.head.data            
        return top_object
    
    def isEmpty(self):    #check isempty
        is_empty = False
        if self.head is None:
            is_empty = True
        return is_empty
