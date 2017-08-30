import sys
from datastructures.stack import Stack
from datastructures.queue import Queue
from datastructures.hashtable import HashTable

choice = -1

def print_menu(options):
    '''PRINTS THE MENU'''
    print()
    for option in options:
        print(option[1], '\t', option[0])
    print('ENTER CHOICE :', end=' ')

def stack_operations():
    '''USER OPERATIONS OF A STACK IMPLEMENTATION'''
    stack = Stack()
    global choice
    while choice > 0:
        stack_menu = [('MAIN MENU', -1), ('EXIT', 0), \
                    ('PUSH', 1), ('POP', 2), ('PEEK', 3), ('SIZE', 4)]
        print_menu(stack_menu)
        choice = int(input().strip())
        if choice == 1:
            print('ENTER ITEM :', end=' ')
            stack.push(int(input().strip()))
            print('PUSH OPERATION SUCCESSFUL.')
        elif choice == 2:
            if stack.is_empty():
                print('UNDERFLOW')
            else:
                print('POPPED VALUE :', stack.pop())
        elif choice == 3:
            if stack.is_empty():
                print('UNDERFLOW')
            else:
                print('STACK TOP :', stack.peek())
        elif choice == 4:
            print('STACK SIZE :', stack.size())

def queue_operations():
    '''USER OPERATIONS OF A QUEUE IMPLEMENTATION'''
    queue = Queue()
    while choice > 0:
        queue_menu = [('MAIN MENU', -1), ('EXIT', 0), \
                    ('ENQUEUE', 1), ('DEQUEUE', 2), ('FRONT', 3), ('REAR', 4), ('SIZE', 5)]
        print_menu(queue_menu)
        choice = int(input().strip())
        if choice == 1:
            print('ENTER ITEM :', end=' ')
            queue.enqueue(int(input().strip()))
            print('ENQUEUE OPERATION SUCCESSFUL.')
        elif choice == 2:
            if queue.is_empty():
                print('UNDERFLOW')
            else:
                print('DEQUEUED VALUE :', queue.dequeue())
        elif choice == 3:
            if queue.is_empty():
                print('UNDERFLOW')
            else:
                print('FRONT :', queue.front())
        elif choice == 4:
            if queue.is_empty():
                print('UNDERFLOW')
            else:
                print('REAR :', queue.rear())
        elif choice == 5:
            print('QUEUE SIZE :', queue.size())

def hash_table_operations():
    '''USER OPERATIONS OF A HASH TABLE IMPLEMENTATION'''
    table = HashTable()
    global choice
    while choice > 0:
        hash_table_menu = [('MAIN MENU', -1), ('EXIT', 0), \
                    ('PUT', 1), ('GET', 2)]
        choice = int(input().strip())

def main():
    '''MAIN METHOD'''
    global choice
    while choice == -1:
        main_menu = [('EXIT', 0), ('STACK', 1), ('QUEUE', 2), ('HASH TABLE', 3)]
        print_menu(main_menu)
        choice = int(input().strip())
        if choice == 0:
            sys.exit()
        elif choice == 1:
            stack_operations()
        elif choice == 2:
            queue_operations()
        elif choice == 3:
            hash_table_operations()
        else:
            print('INVALID CHOICE')
            choice = -1

if __name__ == '__main__':
    main()
