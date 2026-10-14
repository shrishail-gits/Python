queue1=[]
queue2=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    value=int(input("Enter value:"))
    queue1.append(value)
print("Queue 1:",queue1)
print("Queue 2:",queue2)
while len(queue1)>1:
    queue2.append(queue1.pop(0))
removed=queue1.pop(0)
print("Poped:",removed)
queue1,queue2=queue2,queue1
print("Remaining elements:",queue1)