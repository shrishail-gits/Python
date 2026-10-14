# queue=[10,20,30,40,50]
# print("Original Queue:",queue)
# print("Reversed Queue:",queue[::-1])
queue=[10,20,30,40,50]
print("Original Queue:",queue)
reversed_queue=[]
for i in range(len(queue)-1,-1,-1):
    reversed_queue.append(queue[i])
print("Reversed Queue:",reversed_queue)