class node:
    def __init__(self,item=None,next=None):
        self.next=next
        self.item=item
class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start is None
    def insert_at_start(self,data):
        n=node(data,self.start)
        self.start=n
    def insert_at_last(self,data):
        n=node(data)
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp =temp.next
            temp.next=n
        else:
            self.start=n

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp=temp.next
        return None
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next

    def delete_at_start(self):
        if self.start is not None :
            self.start=self.start.next

    def delete_at_last(self):
        if self.start is None:
            pass
        elif self.start.next is not None:
            self.satrt =None
        else:
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=None
    def delete_item(self,data):
        if self.start is None:
            pass
        elif self.start.next is  None:
            if self.satrt.item == data:
                self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                if temp.next.item ==data:
                    temp.next=temp.next.next
                    break
            temp.next=None
        
        

                         



a=SLL(20)
a.insert_at_start(30)
a.insert_at_start(20)
a.insert_at_last(30)
a.insert_after(a.search(20),25)
a.print_list()



