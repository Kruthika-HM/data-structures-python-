class circular_queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size    #initialising a fixed size array in python
        self.front = -1
        self.rear = -1  
    def is_empty(self):
        return self.front == -1 and self.rear == -1
    def is_full(self):
        return (self.rear + 1) % self.size == self.front
    def enqueue(self, data):
        if self.is_full():
            print("Queue is full")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = data
        print(f"element enqueued is: {data}")
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        data = self.queue[self.front]
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.size
        print(f"element dequeued is: {data}")
        return data
    def display(self):
        if self.is_empty():
            print("Queue is empty")
            return
        i = self.front
        print("Queue elements are:")
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.size
        print()
class queue_manager:
    cq = circular_queue(5)
    while True:
        print("1. Enqueue\n2. Dequeue\n3. Display\n4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            data = input("Enter data to be enqueued: ")
            cq.enqueue(data)
        elif choice == 2:
            cq.dequeue()
        elif choice == 3:
            cq.display()
        elif choice == 4:
            print("Exiting")
            break
        else:
            print("Invalid choice")
    
