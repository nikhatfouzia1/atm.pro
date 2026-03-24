class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        print("Node inserted at begining")
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            print("Node inserted as first node")
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        print("Node inserted at end")
    def delete(self,key):
        temp=self.head
        if temp and temp.data==key:
            self.head=temp.next
            temp=None
            print("Node deleted")
            return
        prev=None
        while temp and temp.data!=key:
            prev=temp
            temp=temp.next
        if temp is None:
            print("Value not found")
            return
        prev.next=temp.next
        temp=None
        print("Node deleted")
    def search(self,key):
        temp=self.head
        while temp:
            if temp.data==key:
                print("Element Found")
                return
            temp=temp.next
        print("Element Not Found")
    def display(self):
        temp=self.head
        if temp is None:
            print("List is empty")
            return
        while temp:
            print(temp.data,end=" -> ")
            temp=temp.next
        print("None")
l1=LinkedList()
while True:
    print("\n------LINKED LIST MENU------")
    print("1. Insert at Begining")
    print("2. Insert at End")
    print("3. Delete Node")
    print("4. Search Element")
    print("5. Display List")
    print("6. Exit")
    choice=int(input("Enter your choice:"))
    if choice==1:
        value=int(input("Enter value: "))
        l1.insert_begin(value)
    elif choice==2:
        value=int(input("Enter value: "))
        l1.insert_end(value)
    elif choice==3:
        value=int(input("Enter value to delete: "))
        l1.delete
    elif choice==4:
        value=int(input("Enter value to search: "))
        l1.search(value)
    elif choice==5:
        l1.display()
    elif choice==6:
        print("Program Ended")
    else:
        print("Invalid Option")
    






















            












            
            
