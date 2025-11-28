class pqueue:
    def __init__(self):
        self.list=[]
    def is_empty(self):
        return len(self.list)==0
    def enqueue(self,data,priority):
        index=0
        while len(self.list)>0 and self.list[index][1]>=priority:
            index+=1
        self.list.insert(index,data,priority)
    def dequeue(self):
        if self.is_empty():
            print("priority queue is empty")
            return
        data=self.list.pop(0)
        print(f'element dequeued is: {data[0]} with priority {data[1]}')
    def display(self):
        if self.is_empty():
            print("priority queue is empty")
            return
        print("priority queue elements are:")
        for item in self.list:
            print(f'element: {item[0]} with priority {item[1]}')

class pqueue_manager:
    pq=pqueue()
    while True:
        print("1.enqueue\n2.dequeue\n3.display\n4.exit")
        choice=int(input("enter your choice: "))
        if choice==1:
            data=input("enter data to be enqueued: ")
            priority=int(input("enter priority of the data: "))
            pq.enqueue(data,priority)
        elif choice==2:
            pq.dequeue()
        elif choice==3:
            pq.display()
        elif choice==4:
            print("exiting")
            break
        else:
            print("invalid choice")

    
