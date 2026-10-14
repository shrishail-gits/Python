n=int(input("Enter the number:"))
queue=["1"]
for i in range(n):
    current=queue.pop(0)
    print(current)
    queue.append(current+"0")
    queue.append(current+"1")