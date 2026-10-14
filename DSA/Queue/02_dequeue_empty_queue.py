queue=[10,20,30]
if len(queue)>0:
    removed=queue.pop(0)
    print("Removed:",removed)
    print("Queue:",queue)
else:
    print("Queue is Empty")