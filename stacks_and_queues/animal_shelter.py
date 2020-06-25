import time
from _datetime import datetime


class Animal:
    def __init__(self, name):
        self.name = name
        self.time_added = datetime.now()


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class AnimalQueue:
    def __init__(self):
        self.dogs_queue = None
        self.cats_queue = None

    def dequeue_any(self):
        if not self.cats_queue and not self.dogs_queue:
            print("NO CATS AND DOGS AT THE MOMENT...")
            return None
        if not self.dogs_queue:
            return self.cats_queue.pop()
        elif not self.cats_queue:
            return self.dogs_queue.pop()
        else:
            if self.dogs_queue.head.data.time_added < self.cats_queue.head.data.time_added:
                return self.dogs_queue.pop()
            else:
                return self.cats_queue.pop()

    def enqueue(self, animal):
        # import pdb; pdb.set_trace()
        if isinstance(animal, Dog):
            if self.dogs_queue:
                self.dogs_queue.insertatend(animal)
            else:
                new_list = LinkedList()
                new_list.insertatend(animal)
                self.dogs_queue = new_list

        if isinstance(animal, Cat):
            if self.cats_queue:
                self.cats_queue.insertatend(animal)
            else:
                new_list = LinkedList()
                new_list.insertatend(animal)
                self.cats_queue = new_list


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next

    def push(self, new_data):
        print("New data:{}".format(str(new_data)))
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head:
            temp = self.head
            self.head = self.head.next
            return temp
        else:
            return None

    def insertafter(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insertatend(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while (last.next):
            last = last.next

        last.next = new_node


if __name__ == "__main__":
    aq = AnimalQueue()
    aq.enqueue(Dog("Meggie"))
    time.sleep(5)
    aq.enqueue(Cat("Milo"))
    time.sleep(5)
    aq.enqueue(Cat("Thor"))
    time.sleep(5)
    aq.enqueue(Dog("Cooper"))
    time.sleep(5)
    aq.enqueue(Cat("Leo"))
    animal = aq.dequeue_any()
    print(animal.data.name)
