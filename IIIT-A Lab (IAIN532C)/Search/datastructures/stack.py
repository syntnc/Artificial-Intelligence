'''STACK'''

class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        '''CHECKS WHETHER STACK IS EMPTY'''
        return self.items == []

    def push(self, item):
        '''PUSHES AN ITEM'''
        self.items.append(item)

    def pop(self):
        '''POPS AN ITEM'''
        return self.items.pop()

    def peek(self):
        '''PEEKS AT THE TOP OF STACK'''
        return self.items[len(self.items) - 1]

    def size(self):
        '''GIVES SIZE OF STACK'''
        return len(self.items)
