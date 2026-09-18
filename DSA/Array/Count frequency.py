n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

visited = []

for i in range(n):

    if arr[i] in visited:
        continue

    count = 0

    for j in range(n):

        if arr[i] == arr[j]:
            count += 1

    print(arr[i], "->", count)

    visited.append(arr[i])