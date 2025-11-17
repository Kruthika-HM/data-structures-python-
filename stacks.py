class STACK:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        if len(self.items)==0:
            print("stack is empty")
    def push(self,data):
        self.items.append(data)
    def pop(self):
        if self.is_empty():
            print("stack is empty")
        print("popped item is :",self.items[-1])
        self.items.pop(-1)
       
    def display(self):
        if self.is_empty():
            print("list is empty")
        for i in self.items:
            print(i)
    
class stack_checker():
    S=STACK()
    print("1.push\n 2.pop \n 3.display \n 4.exit")
    choice=int(input("enter your choice: "))
    while choice!=4:
        if choice==1:
            data=input("enter data to be pushed: ")
            S.push(data)
        elif choice==2:
            S.pop()
        elif choice==3:
            S.display()
        else:
            print("invalid choice")
        choice=int(input("enter your choice: "))
    
    print("exited successfully")
