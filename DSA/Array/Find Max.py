n = int(input("Enter number of elements: "))

arr = []

for i in range(n):
    num = int(input("Enter number: "))
    arr.append(num)

largest = arr[0]

for i in range(1, n):
    if arr[i] > largest:
        largest = arr[i]

print("Largest =", largest)