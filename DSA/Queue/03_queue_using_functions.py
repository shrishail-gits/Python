queue=[]
def enqueue(value):
    queue.append(value)

def dequeue():
    if len(queue)>0:
        removed=queue.pop(0)
        print("Removed:",removed)
    else:
        print("Queue is empty")
def display():
    print("queue:",queue)
enqueue(10)
enqueue(20)
enqueue(30)
display()
dequeue()
display()