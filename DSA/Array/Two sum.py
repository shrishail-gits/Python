n = int(input("Enter the number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter the number: "))
    arr.append(num)

target = int(input("Enter the target: "))

found = False

for i in range(n):
    for j in range(i + 1, n):

        if arr[i] + arr[j] == target:
            print("Pair found:", arr[i], "+", arr[j], "=", target)
            print("Indices:", i, j)
            found = True
            break

    if found:
        break

if found == False:
    print("Pair not found")