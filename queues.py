class queue:
    
    def __init__(self):
        self.items=[]
    def is_empty(self):
        if len(self.items)==0:
            print("queue is empty")
    def peek(self):
        if self.is_empty():
            print("queue is empty")
        print("items in your queue is :\n")
        for i in self.items:
            print(i)
    def enque(self,data):
        self.items.append(data)
    def deque(self):
        self.items.pop(0)

class queue_manager():
    print("1.enqueue\n2.dequeue\n3.peek\n4.exit")
    choice=int(input("enter your choice: "))
    q=queue()
    while choice!=4:
        if choice==1:
            data=input("enter data to be enqueued: ")
            q.enque(data)
        elif choice==2:
            q.deque()
        elif choice==3:
            q.peek()
        else:
            print("invalid choice")
        
        choice=int(input("enter your choice: "))
    print("exited successfully")



        
        


