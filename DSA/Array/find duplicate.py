n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

found = False

for i in range(n):

    for j in range(i + 1, n):

        if arr[i] == arr[j]:
            print("Duplicate =", arr[i])
            found = True
            break

    if found:
        break

if not found:
    print("No duplicate")