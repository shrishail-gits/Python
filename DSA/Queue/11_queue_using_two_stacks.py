
stack1 = []
stack2 = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter value: "))
    stack1.append(value)

while len(stack1) > 0:
    stack2.append(stack1.pop())

if len(stack2) > 0:
    print("Removed:", stack2.pop())
else:
    print("Queue is empty")
