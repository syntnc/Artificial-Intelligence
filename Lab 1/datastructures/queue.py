'''QUEUE'''

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        '''CHECKS WHETHER QUEUE IS EMPTY'''
        return self.items == []

    def enqueue(self, item):
        '''ENQUEUES AN ITEM'''
        self.items.insert(0, item)

    def dequeue(self):
        '''DEQUEUES AN ITEM'''
        return self.items.pop()

    def size(self):
        '''GIVES SIZE OF QUEUE'''
        return len(self.items)
