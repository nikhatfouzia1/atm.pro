queue=[]  
def enqueue():
    x=int(input("Enter element to enqueue:"))
    queue.append(x)
    print(x,"inserted into queue")
def dequeue():
    if len(queue)==0:
        print("Queue is empty")
    else:
        removed_element=queue.pop(0)
        print(removed_element,"removed from queue")
def front():
    if len(queue)==0:
        print("queue is Empty")
    else:
        print("Front element is:",queue[0])
def search():
    if len(queue)==0:
        print("Queue is empty")
    else:
        key=int(input("Enter element to search: "))
        if key in queue:
            print(key,"found in queue at position",queue.index(key))
        else:
            print(key, "not found in queue")
def display():
    if len(queue)==0:
        print("Queue is Empty")
    else:
        print("Queue elements (front to rear):")
        for i in range(len(queue)):
            print(queue[i])
def length():
    print("Number of elements in queue:",len(queue))
while True:
    print("\n----queue operations----")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Front")
    print("4. Search")
    print("5. Display")
    print("6. Length")
    print("7. Exit")
    choice=int(input("Enter choice:"))
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        front()
    elif choice==4:
        search()
    elif choice==5:
        display()
    elif choice==6:
        length()
    elif choice==7:
        print("Program ended")
        break
    else:
        print("Invalid option")




        
        print("Invalid option")
