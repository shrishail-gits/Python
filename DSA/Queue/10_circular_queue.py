size = int(input("Enter queue size: "))
queue = [None] * size

front = -1
rear = -1

def enqueue(value):
    global front, rear

    if (rear + 1) % size == front:
        print("Queue is full")
        return

    if front == -1:
        front = 0

    rear = (rear + 1) % size
    queue[rear] = value

def dequeue():
    global front, rear

    if front == -1:
        print("Queue is empty")
        return

    print("Removed:", queue[front])

    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % size

def display():
    if front == -1:
        print("Queue is empty")
        return

    print("Queue:", end=" ")
    i = front

    while True:
        print(queue[i], end=" ")

        if i == rear:
            break

        i = (i + 1) % size

    print()

while True:
    print("\n1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        value = int(input("Enter value: "))
        enqueue(value)
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print("Invalid choice")