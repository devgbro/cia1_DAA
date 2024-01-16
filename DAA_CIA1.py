#!/usr/bin/env python
# coding: utf-8

# ## DAA CIA 1 

# __Implement the following DS in Python__
# 1. Stack Using Array
# 2. Stack using Linked List
# 3. Queue using Array
# 4. Queue using Linked List
# 5. Priority Queue
# 6. Circular Queue

# In[20]:


#1
class StackArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty")

stack_array = StackArray()
stack_array.push(1)
stack_array.push(2)
stack_array.push(3)

print("Stack using Array:")
print("Peek:", stack_array.peek())
print("Pop:", stack_array.pop())
print("Pop:", stack_array.pop())
print("Pop:", stack_array.pop())


# In[21]:


#2
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class StackLinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if not self.is_empty():
            popped_item = self.head.data
            self.head = self.head.next
            return popped_item
        else:
            print("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.head.data
        else:
            print("Stack is empty")

stack_linked_list = StackLinkedList()
stack_linked_list.push(1)
stack_linked_list.push(2)
stack_linked_list.push(3)

print("Stack using Linked List:")
print("Peek:", stack_linked_list.peek())
print("Pop:", stack_linked_list.pop())
print("Pop:", stack_linked_list.pop())
print("Pop:", stack_linked_list.pop())


# In[23]:


#3
class QueueArray:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            print("Queue is empty")

queue_array = QueueArray()
queue_array.enqueue(1)
queue_array.enqueue(2)
queue_array.enqueue(3)

print("Queue using Array:")
print("Peek:", queue_array.peek())
print("Dequeue:", queue_array.dequeue())
print("Dequeue:", queue_array.dequeue())
print("Dequeue:", queue_array.dequeue())


# In[24]:


#4
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.front.data
            self.front = self.front.next
            if self.front is None:
                self.rear = None
            return removed_item
        else:
            print("Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.front.data
        else:
            print("Queue is empty")

queue_linked_list = QueueLinkedList()
queue_linked_list.enqueue(1)
queue_linked_list.enqueue(2)
queue_linked_list.enqueue(3)

print("Queue using Linked List:")
print("Peek:", queue_linked_list.peek())
print("Dequeue:", queue_linked_list.dequeue())
print("Dequeue:", queue_linked_list.dequeue())
print("Dequeue:", queue_linked_list.dequeue())


# In[25]:


#5
import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def is_empty(self):
        return len(self.heap) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self.heap, (priority, item))

    def dequeue(self):
        if not self.is_empty():
            priority, item = heapq.heappop(self.heap)
            return item
        else:
            print("Priority Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.heap[0][1]
        else:
            print("Priority Queue is empty")

priority_queue = PriorityQueue()
priority_queue.enqueue("Task 1", 3)
priority_queue.enqueue("Task 2", 1)
priority_queue.enqueue("Task 3", 2)

print("Priority Queue:")
print("Peek:", priority_queue.peek())
print("Dequeue:", priority_queue.dequeue())
print("Dequeue:", priority_queue.dequeue())
print("Dequeue:", priority_queue.dequeue())


# In[26]:


#6
class CircularQueue:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.front = self.rear = -1

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        if not self.is_full():
            if self.is_empty():
                self.front = self.rear = 0
            else:
                self.rear = (self.rear + 1) % self.capacity
            self.queue[self.rear] = item
        else:
            print("Circular Queue is full")

    def dequeue(self):
        if not self.is_empty():
            removed_item = self.queue[self.front]
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.capacity
            return removed_item
        else:
            print("Circular Queue is empty")

    def peek(self):
        if not self.is_empty():
            return self.queue[self.front]
        else:
            print("Circular Queue is empty")

circular_queue = CircularQueue(3)
circular_queue.enqueue(1)
circular_queue.enqueue(2)
circular_queue.enqueue(3)

print("Circular Queue:")
print("Peek:", circular_queue.peek())
print("Dequeue:", circular_queue.dequeue())
print("Dequeue:", circular_queue.dequeue())
print("Dequeue:", circular_queue.dequeue())

