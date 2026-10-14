queue=[10,20,30,40,50]
k=3
print("Original Queue:",queue)

modified_queue=[]
for i in range(k -1,-1,-1):
    modified_queue.append(queue[i])
for i in range(k,len(queue)):
    modified_queue.append(queue[i])
print("Modified Queue:",modified_queue)